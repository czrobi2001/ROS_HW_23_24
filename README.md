[//]: # (Image References)

[image1]: ./assets/race_car_cad.png "Race car"
[image2]: ./assets/track_cad.png "Monaco track"
[image3]: ./assets/gazebo_model_tree.png "Gazebo model - Monaco"
[image4]: ./assets/Gazebo_sim.png "Gazebo szimuláció"
[image5]: ./assets/rqt_cam.png "Kamera kép - rqt"

# Robotrendszerek laboratórium projekt feladat
Robotrendszerek laboratórium tárgynak féléves projekt feladata, ahol ROS Noetic környezetben fejlesztettünk egy mobil robotot.

A projektet készített:
* Czémán Róbert
* Nyuli Barnabás
* Kurucz István

## Tartalomjegyzék
- [Robotrendszerek laboratórium projekt feladat](#robotrendszerek-laboratórium-projekt-feladat)
  - [Tartalomjegyzék](#tartalomjegyzék)
  - [Feladatleírás](#feladatleírás)
  - [Telepítési útmutató](#telepítési-útmutató)
  - [Szimuláció futtatása](#szimuláció-futtatása)
  - [Versenypálya megtervezése](#versenypálya-megtervezése)
    - [Gazebo szimuláció](#gazebo-szimuláció)
  - [Versenyautó megtervezése](#versenyautó-megtervezése)
    - [RViz szimuláció](#rviz-szimuláció)
  - [Alkalmazott szenzorok](#alkalmazott-szenzorok)
    - [Kamera](#kamera)
  - [Kormányzás](#kormányzás)
  - [Képfeldolgozás](#képfeldolgozás)
    - [Képfeldolgozás lépései](#képfeldolgozás-lépései)
    - [Nehézségek a képfeldolgozás során](#nehézségek-a-képfeldolgozás-során)
    - [A problémák megoldása](#a-problémák-megoldása)
    - [Az alkalmazott megoldások hátrányai](#az-alkalmazott-megoldások-hátrányai)

## Feladatleírás
A feladat megvalósítása során a következő pontoknak kellett eleget tennünk:
* méretarányosan kicsinyített versenypálya készítése,
* versenyautó modell készítése,
* a robot autonóm vezetése saját ROS node segítségével.

## Telepítési útmutató
1. A repositoryt az alábbi paranccsal tudjuk megszerezni:
    ```console
    git clone https://github.com/czrobi2001/ROS_HW_23_24.git
    ```
2. WSL használata esetén: XServer telepítése (grafikus alkalmazás futtatása miatt)
    * a telepítés megtehető például a következő linkre kattintva: [XServer](https://sourceforge.net/projects/vcxsrv/)
    * XServer konfigurálása: Az *Extra settings* oldalon pipáljuk be a *Disable access control* opciót, valamint az *Additional parameters for VcXsrx* felirítú mezőbe gépeljük be a következők:
    ```console
    -nowgl
    ```
3. Szükséges függőségek (dependency) telepítése:
   
    * Pythonhoz a scipy könytár az alábbi parancs segítségével:
    ```console
    pip install scipy
    ```
    *  Az alábbi ROS package-ek:
    * `ros-noetic-actionlib`
    * `ros-noetic-rospy`
    * `ros-noetłc-theora-image-transport`
    * `ros-noetic-urdf`
    * `ros-noetic-xacro`
    * `ros-noetic-roslaunch`
    * `ros-noetic-joint-state-publisher`
    * `ros-noetic-joint-state-publishér-gui`
    * `ros-noetic-robot-state-publisher`
    * `ros-noetic-rviz`
    * `ros-noetic-ackermann-steering-controller`
    * `ros-noetic-controller-manager`
    * `ros-noetic-joint-state-controller`
    * `ros-noetic-ros-control`
    * `ros-noetic-ros-controllers`
    * `ros-noetic-control-toolbox`
    * `ros-noetic-gazebo-ros-control`
    * `ros-noetic-joint-limits-interface`
    * `ros-noetic-gazebo-ros`
    * `ros-noetic-rqt-robot-steering`
    * `ros-noetic-hector-trajectory-server`
  
    Ezek telepíthetők, az alábbi paranccsal:
    ```console
    rosdep install -y --from-paths src --ignore-src --rosdistro noetic -r
    ```

  4. Legvégül futtassuk le a workspace gyökérkönyvtárában a `catkin_make` parancsot.

A lépések teljesítésével már képesek leszünk a szimulációt futtatni. Ennek a lépéseit a követkeező fejezet tartalmazza.

## Szimuláció futtatása
A szimuláció elindításhoz először a mobil robotot kell megnyitni **gazebo**-ban, amit az alábbi paranccsal tehetünk meg.
  ```console
  roslaunch line_follower_race_car spawn_robot.launch
  ```

Majd miután elindult a szimuláció elindíthatjuk a `follow_curve.py` scriptet, ami a képfeldogozást végzi.
  ```console
  rosrun line_follower_race_car follow_curve.py
  ```

Ha az irányításhoz használt paraméterekre is kíváncsiak vagyunk, akkor egy 3. terminál ablakba írjuk be a következőt:
  ```console
  rqt
  ```

Miután megnyílt az **rqt** a Plugins > Topics > Topic Monitor menüpontra kattintás után keressük ki a *cmd_vel* topicot és pipáljuk be. Ezen belül a *linear* és *angular* opciókat lenyitva láthatók a pontos értékek.

## Versenypálya megtervezése
A versenypályát Solidworks-ben egy letöltött, és importált kép segítségével terveztük meg, aminek kontúrját körberajzoltam Besier görbékkel, és kiexportáltam egy `.stl` fájlt.

A pálya kontrúja
![alt text][image2] 

Blenderbe beimportálva készítettem egy a gazebo által is kezelhető collada mesht, ami tartalmazza a blenderben beállított színeket is. Ahhoz, hogy a Gazebo megnyitáskor lássa a modellt, az alábbi sort kell a `.bashrc`-hez hozzá adni.

```console
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/bme_catkin_ws/src/ROS_HW_23_24/gazebo_models
```

### Gazebo szimuláció

A modellt a szimulációs környezetben, vagyis a **gazebo**-ban is megtekinthetjük, ehhez az alábbi parancsot futtassuk:
```console
roslaunch line_follower_race_car world.launch 
```

A szimuláció elindításához egy `.world` kiterejesztésű fájlra van szükségünk, ami tartalmazza a világ, szimulációhoz szükséges fizikai beállításait, valamint a hozzáadott további modelleket.

  ![alt text][image4]

A kocsi beimportálása a világba a `spawn_robot.launch` fájl elindításával történik, ahol argumentumként a robot kezdeti pozícióját is megadhatjuk.


## Versenyautó megtervezése
A versenyautó tervezésnék ötletét internetes forrásból vettük, ami egy kis lego kocsi, amit Solidworks-ben az egyszerűbb kezelhetőség érdekében módosítottam.

  ![alt text][image1]

Ezekután blenderben beállítottam a megfelelő színeket, majd exportáltam egyenként a mozgó komponenseket. A mobil robot vázát illetve a szimulációhoz szükséges paraméterek beállítását a `mogi_bot.xacro` fájlban tettük meg, a robot irányításáért és a kamera képért felelős gazebo plug-in-ket a `mogi_bot.gazebo` fájlban adtuk hozzá.

### RViz szimuláció

A robot modellt megtekinthetjük **RViz**-ben az alábbi parancs segítségével:
```console
roslaunch line_follower_race_car check_urdf.launch
```

## Alkalmazott szenzorok
A képfeldogozáshoz egy kamera került elhelyezésre a versenykocsi elején, aminek paramétereit az órán használtak alapján állítottuk be.

### Kamera

  A kamerát az alábbi plugin valósítja meg. 
  ```xml
  <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
    <alwaysOn>true</alwaysOn>
    <updateRate>0.0</updateRate>
    <cameraName>head_camera</cameraName>
    <imageTopicName>image_raw</imageTopicName>
    <cameraInfoTopicName>camera_info</cameraInfoTopicName>
    <frameName>camera_link_optical</frameName>
    <hackBaseline>0.07</hackBaseline>
    <distortionK1>0.0</distortionK1>
    <distortionK2>0.0</distortionK2>
    <distortionK3>0.0</distortionK3>
    <distortionT1>0.0</distortionT1>
    <distortionT2>0.0</distortionT2>
  </plugin>
  ```

  Módosítást hajtottunk végre azonban a kamera felszerelésénél, ugyanis 45°-ban megdöntöttük a vízszinteshez képest. Ennek oka, hogy így a későbbiekben a képfeldolgozás során a robot irányítása sokkal pontosabban tehető meg.

  <img src="./assets/rqt_cam.png" width="300"/> <img src="./assets/rqt_cam_45.png" width="300"/> 
  
  Baloldalt a kezdeti, jobboldalt a megdöntött kamerakép látható.
  
## Kormányzás
A kormányzás megtervezése volt az egyik fő feladat a projekt során. Fontos volt a megfelelő típus kiválasztása, mivel a pálya és az autó adottságai miatt több szempontnak is meg kellett felelni. Ezek közül például kiemelném azt, hogy az autónak képesnek kell lennie nagyon kis íven is elfordulnia.

Végül a feladatot a `skid-steer` kormányzással valósítottuk meg. Az erre alkalmazott plugin:
```xml
<gazebo>
  <plugin name="ros_force_based_move" filename="libgazebo_ros_force_based_move.so">
    <commandTopic>cmd_vel</commandTopic>
    <odometryTopic>odom</odometryTopic>
    <odometryFrame>odom</odometryFrame>
    <torque_yaw_velocity_p_gain>10000.0</torque_yaw_velocity_p_gain>
    <force_x_velocity_p_gain>10000.0</force_x_velocity_p_gain>
    <force_y_velocity_p_gain>10000.0</force_y_velocity_p_gain>
    <robotBaseFrame>base_footprint</robotBaseFrame>
    <odometryRate>50.0</odometryRate>
    <publishOdometryTf>true</publishOdometryTf>
  </plugin>
</gazebo>
```
A controller a `/cmd_vel` topicról olvas twist típusú üzeneteket, melyeket felhasználva a robot bal és jobboldali kerekeit kezeli, gyakorlatilag differenciálhajtásként. A haladáshoz szükséges a súrlódás megfelelő szimulációja. Ehhez a `mogi_bot.xacro` fileban a kerekek súrlódási tényezői minden kerék esetén, a következőképp lettek beállítva:
```xml
<gazebo reference="front_left_wheel">
    <!-- kp and kd for rubber -->
    <kp>1000000.0</kp>
    <kd>100.0</kd>
    <mu1>1.5</mu1>
    <mu2>1.5</mu2>
    <fdir1>1 0 0</fdir1>
    <maxVel>1.0</maxVel>
    <minDepth>0.00</minDepth>
  </gazebo>
```
Hasonlóképp a `monaco.world` fileban is a megfelelő paraméterek beállításra kerültek:
```sdf
<surface>
        <friction>
            <ode>
              <mu>100</mu>
              <mu2>50</mu2>
              <fdir1>1 0 0</fdir1>
              <slip1>0.5</slip1>
              <slip2>0</slip2>
            </ode>
```
Ezeknek köszönhetően az autó kielégítő manőverezési képességekkel rendelkezik.

## Képfeldolgozás
A képfeldolgozást [OpenCV](https://opencv.org/ "OpenCV") segítségével tettük meg.  

### Képfeldolgozás lépései
A robot irányításáért a `follow_curve.py` nevű Python script felel, ennek a működése a következő:  
1. a kamerakép alapján egy bináris kép készítése, amin a pályát képező pixelek lesznek 1 (v. 255) értékűek
    * először a kapott képett HSV (Hue-Saturation-Value) színtérbe konvertáljuk   
    ```python
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ```  
    * definiálunk egy alsó (`hsv(20, 100, 100)`) és felső (`hsv(30, 255, 255)`) határértéket, amik között a pálya színét keressük
    * elvégezzük a binarizálást
    ```python
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    ```

2. kontúrok keresésése a bináris képen
    * erre a célra az OpenCV `findContours()` függvényét alkalmaztuk, ami visszadaja a képen található kontúrokat
    * első lépésben megvizsgáljuk, hogy a képen található-e kontúr (ha nem, akkor a robot nem indul el)
    * legnagyobb kontúr kiválasztása és annak a középpontjának a meghatározása
    ```python
    max_contour = max(contours, key=cv2.contourArea) # find the biggest contour

    M = cv2.moments(max_contour)
    cx = int(M["m10"] / M["m00"]) # x coord of center point
    cy = int(M["m01"] / M["m00"]) # y coord of center point
    ```

3. "gépi látás" megjelenítése
    * 3 feldolgozott kép egymás melletti megjelenítése a kameraképen, ezek:
    * az 1. pontban létrehozott bináris kép
    * a 2. pontban megtalált kontúrnak a körvonala
    * a 2. pontban meghatározott legnagyobb kontúr középpontjának és a kamerakép közepe közötti távolság vizualizációja

4. robot irányításához szükséges paraméterek meghatározása
    * ezek a paraméterek a robot sebessége az x-tengelye mentén (`linear.x`) és az elfordulása a z-tengelye mentén (`angular.z`)
    * a paraméterek meghatározása a kamerakép x-tengely menti középpontja (`cols/2`) és a talált legnagyobb kontúr x-tengely menti középpontja (`cx`) alapján, valamint tesztelések alapján történt, végül az alábbi megoldás vált be a legjobban:

    ```python
    if abs(cols/2 - cx) >= 20:            # distance >= 20 px
      self.cmd_vel.linear.x = 0.05        # apply 0.05 speed
      if cols/2 > cx:                     # rotate in positive direction
        self.cmd_vel.angular.z = 0.2      # apply 0.2 rotation
      else:                               # rotate in negative direction
        self.cmd_vel.angular.z = -0.2     # apply -0.2 rotation
    if abs(cols/2 - cx) >= 50:            # distance >= 50 px
      self.cmd_vel.linear.x = 0.05
      if cols/2 > cx:
        self.cmd_vel.angular.z = 0.5
      else:
        self.cmd_vel.angular.z = -0.5
    if abs(cols/2 - cx) >= 100:           # distance >= 100 px
      self.cmd_vel.linear.x = 0
      if cols/2 > cx:
        self.cmd_vel.angular.z = 1
      else:
        self.cmd_vel.angular.z = -1
    else:                                # distance < 20 px
      self.cmd_vel.linear.x = 0.5
      self.cmd_vel.angular.z = 0
    ```
5. a meghatározott paraméterek közlése
    * a paramétereket a *cmd_vel* topic-ba küldjük `Twist` üzenet formájában

### Nehézségek a képfeldolgozás során
Sok-sok kísérletezést követően eljutottunk oda, hogy a robot képes végighaladni a teljes pályán hiba nélkül, egész jó tempóban. A korábbi verziókban az alábbi hibák álltak fenn:
1. a kanyarokat nagyon lassan veszi be
2. visszafordító kanyarokban elhagyja a pályát

### A problémák megoldása
Az előző részben említett problémákra végül a következő megoldásokat eszközöltük:
1. több határértéket is felvettünk a kamerakép és a kontúr középpontja közötti távolság alapján és ezen távolságnak megfelelően vettük fel a sebesség és elfordulás mértéket (a pontos sebesség és elfordulás értékek tesztelések során lettek meghatározva)
2. a problémát az idézte elő, hogy a kameraképen nagyon előrefelé lehetett csak látni (ekkor még a vízszintes síkkal párhuzamosan volt felszerelve), emiatt amikor egy visszafordító kanyarhoz ért a robot, akkor sokszor a pálya robot alatti része kikerült a képből és egy másik, távolabbi kontúr került a célpontjába - erre a megoldást a kamera megdöntése jelentette -45°-ban a vízszinteshez képest 

### Az alkalmazott megoldások hátrányai
1. az meghatározott határértékek alapvetően a jelenlegi pálya alapján lettek kikísérletezve, így nem garantálható, hogy minden más esetben megfelleően fog működni
2. így csak a pályának a közvetlenül a robot előtti része látható, emiatt a későbbi fejlesztések nehezebbek lehetnek, ha a pálya későbbi részeinek megfelelően szeretnénk mondjuk egy adott ívett követni vagy egy meghatározott sebesség görbét, hogy a robot köridejét javítsuk a pályán

<video src="./assets/gazebo.mp4" width="320" height="240" controls></video>