[//]: # (Image References)

[image1]: ./assets/race_car_cad.png "Race car"
[image2]: ./assets/track_cad.png "Monaco track"
[image3]: ./assets/gazebo_model_tree.png "Gazebo model - Monaco"
[image4]: ./assets/Gazebo_sim.png "Gazebo szimuláció"
[image5]: ./assets/rqt_cam.png "Kamera kép - rqt"

# Robotrendszerek laboratórium projekt feladat
Robotrendszerek laboratórium tárgynak féléves projekt feladata, ahol ROS Noetic környezetben fejlesztettünk egy mobil robotot.

# Vonalkövető versenyautó programozása
A sikeres telepítéshez és futtatáshoz szükséges fontosabb lépések:

# Tartalomjegyzék
- [Robotrendszerek laboratórium projekt feladat](#robotrendszerek-laboratórium-projekt-feladat)
- [Vonalkövető versenyautó programozása](#vonalkövető-versenyautó-programozása)
- [Tartalomjegyzék](#tartalomjegyzék)
- [Kezdőcsomag](#kezdőcsomag)
- [Versenyautó megtervezése](#versenyautó-megtervezése)
- [Versenypálya](#versenypálya)
- [Gazebo szimuláció](#gazebo-szimuláció)
- [Alkalmazott szenzorok](#alkalmazott-szenzorok)
  - [Kamera](#kamera)
- [Ackermann kormányzás](#ackermann-kormányzás)
- [Képfeldolgozás OpenCV-vel](#képfeldolgozás-opencv-vel)
- [Szimuláció futtatása](#szimuláció-futtatása)
- [Telepítési útmutató](#telepítési-útmutató)

# Kezdőcsomag
A kezdőcsomagban a tantárgy során használt plug-in-ket már tartalmazza, illetve az alapvető .launch fájlokat, amikkel megjeleníthetjük a robotot, pályát, illetve a kettőt egy térben.

# Versenyautó megtervezése
A versenyautó tervezésnék ötletét internetes forrásból vettük, ami egy kis lego kocsi, amit Solidworks-ben az egyszerűbb kezelhetőség érdekében módosítottam.

  Lego verseny kocsi: 

  ![alt text][image1] 

# Versenypálya
A versenypályát szintén Solidworks-ben egy letöltött, és importált kép segítségével terveztem meg, aminek kontúrját körberajzolva jutottam el a Gazeboban használt modellig. 

  A pálya kontrúja:

  ![alt text][image2] 

A színek megfelelő megjelenítéséhez egy megfelelő Gazebo modell is készült, amit az alapértelmezett Gazebo modellek telepítési könyvtárában kell elhelyezni, hogy megtalálja a modell behíváskor a gazebo a `.dae` és `.stl` fájlokat. Amennyiben nem látjuk a `.gazebo` könyvtárat akkor láthatóvá kell tenni a rejtett könyvtárakat is a számítógép beállításaiban.


  A sikeres futtatáshoz az alábbi fájlokat kell a pálya neve alatti Gazebo modell  könyvtárban létrehozni. A `Gazebo_modell` könyvtárban a `monaco` mappát kell ide beilleszteni:

  ![alt text][image3]

# Gazebo szimuláció

  A versenyautó és pálya megjelenítése a szimulációban:

  ![alt text][image4]

# Alkalmazott szenzorok
A képfeldogozáshoz egy kamera került elhelyezésre a versenykocsi elején, aminek paramétereit az órán használtak alapján állítottuk be.

## Kamera
  Az élőkép RQT-ben:

  ![alt text][image5]

# Ackermann kormányzás
  Az Ackermann kormányzás működtetéséhez az ackermann_steering_controller-t használtuk (telepítését ld. később). A controller irányításához a cmd_vel topic-ra érkező twist üzenetek szükségesek, melyek az első kerekek orientációját, és a hátsó kerekek sebességét képesek változtatni.

# Képfeldolgozás OpenCV-vel

# Szimuláció futtatása

# Telepítési útmutató
  (Noetic-re vonatkozó telepítési utasítások)
  
új:
töltsük le az workspace src mappájába [ezt](https://github.com/srmainwaring/steer_bot) a git repot.
Parancssorból:
```console
git clone https://github.com/srmainwaring/steer_bot?tab=readme-ov-file
```

Nézzük meg és telepítsük az esetleges dependencyket:
```console
cd ~/bme_catkin_ws
rosdep check --from-paths src --ignore-src --rosdistro noetic
rosdep install --from-paths src --ignore-src --rosdistro noetic -y
```
Ezt módosítottam...

Majd végül futtassuk le a workspace gyökérkönyvtárában a catkin_make parancsot.



  régi:
  Telepítendő controller az Ackermann-kormányzáshoz elérhető [itt](https://github.com/ros-controls/ros_controllers). Illetve az alábbi parancs futtatásával:

  ```console
  git clone -b noetic-devel https://github.com/ros-controls/ros_controllers/
  ```
  (Sajnos a teljes repo telepítése nélkül nem ment...)

  Valamint szükséges a four_wheel_steering_msgs üzenettípusok és a urdf_geometry_parser telepítése az alábbi kommandokkal:

  ```console
  git clone https://github.com/ros-drivers/four_wheel_steering_msgs

  git clone https://github.com/ros-controls/urdf_geometry_parser
  ```

