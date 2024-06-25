import time
import random
from machine import Pin, ADC
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

#Matrix und Buffer initialisieren
matrix = Interstate75(display = DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

#Höhe und Breite der Matrix
width = matrix.width
height = matrix.height


sun_width = 23
sun_height = 23
sun_pos_x = 27
sun_pos_y = 10

sun_frame_0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,
                 0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,2,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 0,0,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,0,0,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,2,0,0,0,0,0,
                 0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

sun_frame_1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,
                 0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 0,2,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,0,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,
                 0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

sun_frame_2 = [0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 2,2,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,2,2,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

sun_frame_3 = [0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,2,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 2,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,2,
                 0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,2,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,]


sun_frames = [sun_frame_0,
                sun_frame_1,
                sun_frame_2,
                sun_frame_1]


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

#Helligkeit über LDR

ldr = ADC(Pin(26))
br_old_ticks = 0

#Farben, Grundeinstellung
black = buffer.create_pen(0, 0, 0)
white = buffer.create_pen(200, 200, 200)
yellow = buffer.create_pen(201, 168, 0)
grey = buffer.create_pen(128, 128, 128)
sky = buffer.create_pen(16, 63, 84)

#Einstellungen für die Temperaturanzeige
temp = random.randrange(-20,40)
temp_width = buffer.measure_text(str(temp)+"°C")
text_pos_x = int(width/2 - (temp_width-2)/2)

#Zeitstempel für die cloudnbewegung
cloud_old_ticks = 0
cloud_2_old_ticks = 0
cloud_3_old_ticks = 0

#Variablen für die Animation der sunngrafik
sun_cur = 0
sun_old_ticks = 0

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
            

def sun_animation():
    
    global sun_frames
    global sun_cur
    global sun_old_ticks
    sun_waiting_time = 500
    
        
    if ((time.ticks_ms() - sun_old_ticks) >= sun_waiting_time):
        sun_old_ticks = time.ticks_ms()
        
        if sun_cur < len(sun_frames)-1:

            sun_cur += 1
            
        else:
        
            sun_cur = 0


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
   
   
def set_brightness():
    
    global br_old_ticks
    global white
    global yellow
    global grey
    global sky
    br_waiting_time = 2000
    
    if ((time.ticks_ms() - br_old_ticks) >= br_waiting_time):
        br_old_ticks = time.ticks_ms()
        
        #Helligkeitswert auslesen und auf brightness anwenden
        read_ldr = ldr.read_u16()
        brightness = read_ldr*0.000015
        print(read_ldr)
        
        #Farben dynamisch an die Umgebungshelligkeit anpassen
        white = buffer.create_pen(int(200*brightness), int(200*brightness), int(200*brightness))
        yellow = buffer.create_pen(int(201*brightness), int(168*brightness), 0)
        grey = buffer.create_pen(int(128*brightness), int(128*brightness), int(128*brightness))
        sky = buffer.create_pen(int(16*brightness), int(63*brightness), int(84*brightness))
        

while True:

    set_brightness()
    
    #Die Matrix mit Schwarz löschen
    buffer.set_pen(black)
    buffer.clear()

    #Die Clipping-Schablone für die Wetter-Darstellung festlegen
    buffer.set_clip(0, 0, 64, 46)
    
    #Farbe des Himmels einstellen und Hintergrund damit füllen
    buffer.set_pen(sky)
    buffer.clear()
    
    #sun und cloudn malen (Array, x, y, w, h)
    show_array(sun_frames[sun_cur], sun_pos_x, sun_pos_y, sun_width, sun_height)
    show_array(cloud, cloud_pos_x, cloud_pos_y, cloud_width, cloud_height)
    show_array(cloud_2, cloud_2_pos_x, cloud_2_pos_y, cloud_2_width, cloud_2_height)
    show_array(cloud_3, cloud_3_pos_x, cloud_3_pos_y, cloud_3_width, cloud_3_height)
    
    #Clipping entfernen, damit als Nächstes der Text
    #darunter dargestellt werden kann.
    buffer.remove_clip()

    #Farbe für Temperatur-Anzeige auswählen und Text ausgeben
    buffer.set_pen(white)
    buffer.text(str(temp)+"°C",text_pos_x,48,scale=2)

    #cloudn-Position um den festgelegten Wert bewegen (erst beim nächsten Durchlauf sichtbar)
    clouds_move()
    
    #sun animieren
    sun_animation()
        
    #Grafik im Puffer auf der Matrix ausgeben      
    matrix.update(buffer)
    
   