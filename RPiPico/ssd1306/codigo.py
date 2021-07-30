from machine import Pin, SPI
import ssd1306
import framebuf
from time import sleep_ms
import os
spi = SPI(0, baudrate=1000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 64, spi, machine.Pin(4), machine.Pin(3), machine.Pin(5))
oled.invert(True)
numero_imagenes=len(os.listdir("imagenes"))
def Abrir_Icono(ruta):
    doc = open(ruta,"rb")
    doc.readline()
    xy = doc.readline()
    x = int(xy.split()[0])
    y = int(xy.split()[1])
    icono = bytearray(doc.read())
    doc.close()
    return framebuf.FrameBuffer(icono,x,y,framebuf.MONO_HLSB)    
while True:
    for i in range(1,numero_imagenes):
        oled.blit(Abrir_Icono("imagenes/imagen{}.pbm".format(i)),0,0)
        oled.show()
        #fps=10, 1000/10=100
        sleep_ms(100)
