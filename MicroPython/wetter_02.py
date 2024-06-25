import time
import random
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

#Matrix und Buffer initialisieren
matrix = Interstate75(display = DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

#Höhe und Breite der Matrix
width = matrix.width
height = matrix.height

#Startkoordinaten für die Clipping-Schablone
clipping_x = 14
clipping_y = 7


#sun mit 23x23 Pixeln
sun = [0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,
         0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,
         0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,2,0,0,0,0,0,
         0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
         0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
         0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
         0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
         2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,
         0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
         0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
         0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
         0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
         0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,2,0,0,0,0,0,
         0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,
         0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

sun_width = 23
sun_height = 23
sun_pos_x = 27
sun_pos_y = 10


#Grosse cloud mit 38x18 Pixeln
cloud = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,3,3,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,3,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,3,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,3,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,
         0,0,0,0,0,3,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,
         0,0,0,0,0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,0,0,0,0,
         0,0,0,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,3,0,0,0,
         0,0,3,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,3,0,0,
         0,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,
         3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,
         3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
         3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
         3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
         3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
         0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,
         0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0]

cloud_width = 32
cloud_height = 18
cloud_pos_x = 14
cloud_pos_y = 25


#Kleine cloud mit 20x8 Pixeln
cloud_2 = [0,0,0,0,3,3,3,0,0,0,0,3,3,3,0,0,0,0,0,0,
           0,0,0,3,1,1,1,3,3,0,3,1,1,1,3,0,0,0,0,0,
           0,0,3,3,1,1,1,1,1,3,1,1,1,1,1,3,0,0,0,0,
           0,3,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,3,3,0,
           3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,3,
           3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
           3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
           0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0]

cloud_2_width = 20
cloud_2_height = 8
cloud_2_pos_x = 50
cloud_2_pos_y = random.randint(34,36)

#Zweite kleine cloud mit 22x10 Pixeln
cloud_3 = [0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,3,1,1,3,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,3,3,3,3,1,1,1,1,3,0,0,0,0,0,0,
           0,0,0,0,0,0,3,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,
           0,0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,3,3,3,0,0,0,
           0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,3,0,0,
           3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,3,0,
           3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
           0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
           0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,]

cloud_3_width = 22
cloud_3_height = 10
cloud_3_pos_x = 50
cloud_3_pos_y = random.randint(32,35)

#Farbendefinitionen
black = buffer.create_pen(0, 0, 0)
white = buffer.create_pen(200, 200, 200)
yellow = buffer.create_pen(201, 168, 0)
grey = buffer.create_pen(128, 128, 128)

#Einstellungen für die Temperaturanzeige
temp = random.randrange(-20,40)
temp_width = buffer.measure_text(str(temp)+"°C")
text_pos_x = int(width/2 - (temp_width-2)/2)

#Zeitstempel für die cloudnbewegung
cloud_old_ticks = time.ticks_ms()
cloud_2_old_ticks = time.ticks_ms()
cloud_3_old_ticks = time.ticks_ms()

#############################################################
#Diese Funktion zeigt ein Array auf der Matrix als Grafik an.
def show_array(icon_array, icon_pos_x, icon_pos_y, icon_width, icon_height):
    
    icon_array_x = 0
    icon_array_y = 0
    
    for pixel in range(len(icon_array)):
        
        if icon_array[pixel] == 1:
            buffer.set_pen(grey)
        elif icon_array[pixel] == 2:
            buffer.set_pen(yellow)
        elif icon_array[pixel] == 3:
            buffer.set_pen(white)
    
        if icon_array[pixel] != 0:
            buffer.pixel(icon_array_x+icon_pos_x, icon_array_y+icon_pos_y)
        
        if icon_array_x < (icon_width - 1):
            icon_array_x += 1
        else:
            icon_array_x = 0
            icon_array_y += 1


##############################################
#Diese Funktion bewegt die cloudn durchs Bild.
def clouds_move():
    
    global cloud_old_ticks
    global cloud_pos_x
    global cloud_pos_y
    global cloud_2_old_ticks
    global cloud_2_pos_x
    global cloud_2_pos_y
    global cloud_3_old_ticks
    global cloud_3_pos_x
    global cloud_3_pos_y
    
    cloud_waiting_time = 200
    cloud_2_waiting_time = 100
    cloud_3_waiting_time = 50
    
    if ((time.ticks_ms() - cloud_old_ticks) >= cloud_waiting_time):
        cloud_old_ticks = time.ticks_ms()
        cloud_pos_x -= 1
        
    if ((time.ticks_ms() - cloud_2_old_ticks) >= cloud_2_waiting_time):
        cloud_2_old_ticks = time.ticks_ms()
        cloud_2_pos_x -= 1
        
    if ((time.ticks_ms() - cloud_3_old_ticks) >= cloud_3_waiting_time):
        cloud_3_old_ticks = time.ticks_ms()    
        cloud_3_pos_x -= 1
        
    if cloud_pos_x < 0-cloud_width:
        cloud_pos_x = 65
        cloud_pos_y = random.randint(25,29)
        
    if cloud_2_pos_x < 0-cloud_2_width:
        cloud_2_pos_x = 65
        cloud_2_pos_y = random.randint(34,37)
    
    if cloud_3_pos_x < 0-cloud_3_width:
        cloud_3_pos_x = 65
        cloud_3_pos_y = random.randint(30,35)
        print("random set")
        print(cloud_3_pos_y)
        
while True:

    #Die Matrix mit Schwarz löschen
    buffer.set_pen(black)
    buffer.clear()

    #Die Clipping-Schablone für die Wetter-Darstellung festlegen
    buffer.set_clip(0, 0, 64, 46)
    
    #Farbe des Himmels einstellen und Hintergrund damit füllen
    buffer.set_pen(buffer.create_pen(16,63,84))
    buffer.clear()
    
    #sun und cloudn malen (Array, x, y, w, h)
    show_array(sun, sun_pos_x, sun_pos_y, sun_width, sun_height)
    show_array(cloud, cloud_pos_x, cloud_pos_y, cloud_width, cloud_height)
    show_array(cloud_2, cloud_2_pos_x, cloud_2_pos_y, cloud_2_width, cloud_2_height)
    show_array(cloud_3, cloud_3_pos_x, cloud_3_pos_y, cloud_3_width, cloud_3_height)
    
    print(cloud_3_pos_y)
    #Clipping entfernen, damit als Nächstes der Text
    #darunter dargestellt werden kann.
    buffer.remove_clip()

    #Farbe für Temperatur-Anzeige auswählen und Text ausgeben
    buffer.set_pen(white)
    buffer.text(str(temp)+"°C",text_pos_x,48,scale=2)

    #cloudn-Position um den festgelegten Wert bewegen (erst beim nächsten Durchlauf sichtbar)
    clouds_move()
        
    #Grafik im Puffer auf der Matrix ausgeben      
    matrix.update(buffer)