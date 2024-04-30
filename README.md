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
1. [Kezdőcsomag](#Kezdőcsomag)  
2. [Versenyautó megtervezése](#Versenyautó-megtervezése)
3. [Versenypálya](#Versenypálya)
4. [Gazebo szimuláció](#Gazebo-szimuláció)
5. [Alaklmazott szenzorok](#Alaklmazott-szenzorok)  
5.1. [Kamera](#Kamera)
6. [Ackermann kormányzás](#Ackerman-kormányzás)
7. [Képfeldolgozás OpenCV-vel](#Képfeldolgozás-OpenCV-vel])
8. [Szimuláció futtatása](#Szimuláció-futtatása)

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

A színek megfelelő megjelenítéséhez egy megfelelő Gazebo modell is készült, amit az alapértelmezett Gazebo modellek telepítési könyvtárában kell elhelyezni, hogy megtalálja a modell behíváskor a gazebo a `.dae` és `.stl` fájlokat. Amennyiben nem látjuk a .gazebo könyvtárat akkor láthatóá kell tenni a rejtett könyvtárakat is a számítógép beállításaiban.


  A sikeres futtatáshoz az alábbi fájlokat kell a pálya neve alatti Gazebo modell  könyvtárban létrehozni. A `Gazebo_modell` mappában `monaco` néven találjuk meg azt a modellt amit ide kell beilleszteni:

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

# Képfeldolgozás OpenCV-vel

# Szimuláció futtatása
