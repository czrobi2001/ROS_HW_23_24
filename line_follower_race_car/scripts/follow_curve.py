#!/usr/bin/env python3

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CompressedImage
from geometry_msgs.msg import Twist
import rospy
try:
    from queue import Queue
except ImportError:
    from Queue import Queue
import threading
import numpy as np
from scipy.optimize import minimize

class BufferQueue(Queue):
    """Slight modification of the standard Queue that discards the oldest item
    when adding an item and the queue is full.
    """
    def put(self, item, *args, **kwargs):
        # The base implementation, for reference:
        # https://github.com/python/cpython/blob/2.7/Lib/Queue.py#L107
        # https://github.com/python/cpython/blob/3.8/Lib/queue.py#L121
        with self.mutex:
            if self.maxsize > 0 and self._qsize() == self.maxsize:
                self._get()
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()

class cvThread(threading.Thread):
	"""
	Thread that displays and processes the current image
	It is its own thread so that all display can be done
	in one thread to overcome imshow limitations and
	https://github.com/ros-perception/image_pipeline/issues/85
	"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.image = None

		# Initialize published Twist message
		self.cmd_vel = Twist()
		self.cmd_vel.linear.x = 0
		self.cmd_vel.angular.z = 0

	def run(self):
		# Create a single OpenCV window
		cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
		cv2.resizeWindow("frame", 800,600)

		while True:
			self.image = self.queue.get()

			# Process the current image
			mask, contour, crosshair = self.processImage(self.image)

			# Add processed images as small images on top of main image
			result = self.addSmallPictures(self.image, [mask, contour, crosshair])
			cv2.imshow("frame", result)

			# Check for 'q' key to exit
			k = cv2.waitKey(6) & 0xFF
			if k in [27, ord('q')]:
				rospy.signal_shutdown('Quit')

	def processImage(self, img):
		# Get thet number of rows and columns of the image
		rows,cols = img.shape[:2]

		yellowMask = self.thresholdBinary(img)
		stackedMask = np.dstack((yellowMask, yellowMask, yellowMask))
		contourMask = stackedMask.copy()
		crosshairMask = stackedMask.copy()

		# return value of findContours depends on OpenCV version
		contours,_ = cv2.findContours(yellowMask.copy(), 1, cv2.CHAIN_APPROX_NONE)

		# Find the biggest contour (if detected)
		if len(contours) > 0:
			c = max(contours, key=cv2.contourArea)
			M = cv2.moments(c)

			# Make sure that "m00" won't cause ZeroDivisionError: float division by zero
			if M["m00"] != 0:
				cx = int(M["m10"] / M["m00"])
				cy = int(M["m01"] / M["m00"])
			else:
				cx, cy = 0, 0

			# Show contour and centroid
			cv2.drawContours(contourMask, contours, -1, (40,164,182), 10)
			cv2.circle(contourMask, (cx, cy), 10, (40,164,182), -1)

			# Show crosshair and difference from middle point
			cv2.line(crosshairMask,(cx,0),(cx,rows),(40,164,182),10) # middle of the contour
			cv2.line(crosshairMask,(0,cy),(cols,cy),(40,164,182),10) # middle of the contour
			cv2.line(crosshairMask,(int(cols/2),0),(int(cols/2),rows),(120,120,120),10) # middle of the camera

			# print("Distance from center: %d" % (cols/2 - cx))

			# Apply speed and rotation based on the distance from the center
			if abs(cols/2 - cx) >= 20:
				self.cmd_vel.linear.x = 0.05
				if cols/2 > cx:
					self.cmd_vel.angular.z = 0.2
				else:
					self.cmd_vel.angular.z = -0.2

			if abs(cols/2 - cx) >= 50:
				self.cmd_vel.linear.x = 0.05
				if cols/2 > cx:
					self.cmd_vel.angular.z = 0.5
				else:
					self.cmd_vel.angular.z = -0.5

			if abs(cols/2 - cx) >= 100:
				self.cmd_vel.linear.x = 0
				if cols/2 > cx:
					self.cmd_vel.angular.z = 1
				else:
					self.cmd_vel.angular.z = -1
			else: # Distance is <20
				self.cmd_vel.linear.x = 0.5
				self.cmd_vel.angular.z = 0
		else: # If no contour is detected, stop the robot
			self.cmd_vel.linear.x = 0
			self.cmd_vel.angular.z = 0

		# Publish cmd_vel
		pub.publish(self.cmd_vel)

		# Return processed frames
		return yellowMask, contourMask, crosshairMask
	
	def thresholdBinary(self, image):
		# Convert the image to HSV color space
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
			
		# Define the range for the color of the track (yellow)
		lower_yellow = np.array([20, 100, 100])
		upper_yellow = np.array([30, 255, 255])
			
		# Create a binary mask where yellow pixels are white and all other pixels are black
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

		return mask

	# Add small images to the top row of the main image
	def addSmallPictures(self, img, small_images, size=(160, 120)):
		'''
		:param img: main image
		:param small_images: array of small images
		:param size: size of small images
		:return: overlayed image
		'''

		x_base_offset = 40
		y_base_offset = 10

		x_offset = x_base_offset
		y_offset = y_base_offset

		for small in small_images:
			small = cv2.resize(small, size)
			if len(small.shape) == 2:
				small = np.dstack((small, small, small))

			img[y_offset: y_offset + size[1], x_offset: x_offset + size[0]] = small

			x_offset += size[0] + x_base_offset

		return img

def queueMonocular(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2Img = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        qMono.put(cv2Img)

print("OpenCV version: %s" % cv2.__version__)

queueSize = 1      
qMono = BufferQueue(queueSize)

cvThreadHandle = cvThread(qMono)
cvThreadHandle.setDaemon(True)
cvThreadHandle.start()

bridge = CvBridge()

rospy.init_node('ball_chaser')
# Define your image topic
image_topic = "/head_camera/image_raw"
# Set up your subscriber and define its callback
rospy.Subscriber(image_topic, Image, queueMonocular)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# Spin until Ctrl+C
rospy.spin()