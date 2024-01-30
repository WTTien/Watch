from watch import Watch
from time import sleep

Watch = Watch()

def Draw(ColorR, ColorG, ColorB):
    Watch.WriteData(ColorR)
    Watch.WriteData(ColorG)
    Watch.WriteData(ColorB)

if __name__ == '__main__':
    Watch.Initialise()
    Watch.SetFrame((0,0), (239,239))

    Watch.DISP_PIN.value = 0.5
   
    DrawColor = 239*239
    ColorR = 255 & 0xFF
    ColorG = 165 & 0xFF
    ColorB = 0 & 0xFF

    #Continuously draw a color on the screen
    Watch.WriteCommand(0x2C)
    for i in range(DrawColor):
        Draw(ColorR, ColorG, ColorB)

    sleep(1)
    
    #Draw half canvas with one color and continue another half with another color
    ColorR = 0
    ColorG = 165
    ColorB = 150
    Watch.WriteCommand(0x2C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)
    
    ColorR = 150
    ColorG = 165
    ColorB = 0
    Watch.WriteCommand(0x3C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)

    sleep(1)

    #Draw half canvas with one color and continue with another color that paint whole canvas
    ColorR = 15
    ColorG = 15
    ColorB = 15
    Watch.WriteCommand(0x2C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)
    
    ColorR = 255
    ColorG = 165
    ColorB = 255
    Watch.WriteCommand(0x3C)
    for i in range (DrawColor):
        Draw(ColorR, ColorG, ColorB)

    sleep(1)

    #Draw half canvas with one color and draw whole canvas from the beginning from another color
    ColorR = 165
    ColorG = 0
    ColorB = 165
    Watch.WriteCommand(0x2C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)
    
    ColorR = 165
    ColorG = 0
    ColorB = 165
    Watch.WriteCommand(0x2C)
    for i in range (DrawColor):
        Draw(ColorR, ColorG, ColorB)

    sleep(5)
