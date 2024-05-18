[//]: # (Image References)

[image1]: ./assets/race_car_cad.png "Race car"
[image2]: ./assets/track_cad.png "Monaco track"
[image3]: ./assets/gazebo_model_tree.png "Gazebo model - Monaco"
[image4]: ./assets/Gazebo_sim.png "Gazebo szimuláció"
[image5]: ./assets/rqt_cam.png "Kamera kép - rqt"

# Robotrendszerek laboratórium projekt feladat
Robotrendszerek laboratórium tárgynak féléves projekt feladata, ahol ROS Noetic környezetben fejlesztettünk egy mobil robotot.

## Tartalomjegyzék
1. [Feladatleírás](##Feladatleírás)
1. [Versenyautó megtervezése](#Versenyautó-megtervezése)
2. [Versenypálya](#Versenypálya)
3. [Gazebo szimuláció](#Gazebo-szimuláció)
4. [Alaklmazott szenzorok](#Alaklmazott-szenzorok)  
4.1. [Kamera](#Kamera)
5. [Skid steer kormányzás](#Skid-steer-kormányzás)
6. [Képfeldolgozás OpenCV-vel](#Képfeldolgozás-OpenCV-vel])
7. [Szimuláció futtatása](#Szimuláció-futtatása)
8. [Telepítési útmutató](#Telepítési-útmutató)

## Feladatleírás
A feladat megvalósítása során a következő pontoknak kellett eleget tennünk:
* méretarányosan kicsinyített versenypálya készítése,
* versenyautó modell készítése,
* a robot autonóm vezetése saját ROS node segítségével.

## Vonalkövető versenyautó programozása
A sikeres telepítéshez és futtatáshoz szükséges fontosabb lépések:


# Versenyautó megtervezése
A versenyautó tervezésnék ötletét internetes forrásból vettem, ami egy kis lego kocsi, amit Solidworks-ben az egyszerűbb kezelhetőség érdekében módosítottam.

  Lego verseny kocsi: 

  ![alt text][image1] 

# Versenypálya
A versenypályát szintén Solidworks-ben egy letöltött, és importált kép segítségével terveztem meg, aminek kontúrját körberajzoltam Besier görbékkel, és kiexportáltam egy `.stl` fájlt.

  A pálya kontrúja:

  ![alt text][image2] 

Blenderbe beimportálva készítettem egy a gazebo által is feldolgozható collada mesht, a színek megfelelő megjelenítése érdekében. Ahhoz, hogy a Gazebo megnyitáskor lássa a modellt, az alábbi sort kell a `.bashrc` hozzá adni.

```console
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/bme_catkin_ws/src/ROS_HW_23_24/gazebo_models
```

# Gazebo szimuláció

  A versenyautó és pálya megjelenítése a szimulációban:

  ![alt text][image4]

# Alkalmazott szenzorok
A képfeldogozáshoz egy kamera került elhelyezésre a versenykocsi elején, aminek paramétereit az órán használtak alapján állítottuk be.

## Kamera

  Kamera plug-in

  ![alt text][image5]

# Skid steer kormányzás

  Alkalmazott plug-in

# Képfeldolgozás OpenCV-vel

# Szimuláció futtatása

# Telepítési útmutató
