[//]: # (Image References)

[image1]: ./assets/race_car_cad.png "Race car"
[image2]: ./assets/track_cad.png "Monaco track"
[image3]: ./assets/gazebo_model_tree.png "Gazebo model - Monaco"

# Robotrendszerek laboratórium projekt feladat
Robotrendszerek laboratórium tárgynak féléves projekt feladata, ahol ROS Noetic környezetben fejlesztettünk egy mobil robotot.

# Vonalkövető versenyautó programozása
A sikeres telepítéshez és futtatáshoz szükséges fontosabb lépések:

# Tartalomjegyzék
1. [Kezdőcsomag](#Kezdőcsomag)  
2. [Versenyautó megtervezése](#Versenyautó-megtervezése)
3. [Versenypálya](#Versenypálya)
4. [Alaklmazott szenzorok](#Alaklmazott-szenzorok)  
4.1. [Kamera](#Kamera)
5. [Képfeldolgozás OpenCV-vel](#Képfeldolgozás-OpenCV-vel])
6. [Szimuláció futtatása](#Szimuláció-futtatása)

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

A színek megfelelő megjelenítéséhez egy megfelelő Gazebo modell is készült, amit az alapértelmezett Gazebo modellek telepítési könyvtárában helyeztem el.

  A sikeres gazebo modell létrehozásáhaz az alábbi fájlokat kell a pálya neve alatti Gazbo modell  könyvtárban létrehozni:

  ![alt text][image3] 


# Alkalmazott szenzorok

## Kamera

# Képfeldolgozás OpenCV-vel

# Szimuláció futtatása
