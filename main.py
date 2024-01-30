from watch import Watch
from time import sleep

Watch = Watch()

def Draw(ColorR, ColorG, ColorB):
    Watch.WriteData(ColorR)
    Watch.WriteData(ColorG)
    Watch.WriteData(ColorB)

def FirstTry29JanSuccess():
    DrawColor = 240*240
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

def CheckScreenLocations():
    BoxSize = 48
    FrameSize = 240

    for i in range(FrameSize):
        for j in range(FrameSize):
            if ((i/BoxSize) % 2) == ((j/BoxSize)%2):
                ColorR = 0
                ColorG = 0
                ColorB = 0
            else:
                ColorR = 255
                ColorG = 255
                ColorB = 255

            if i==0 and j==0:
                Watch.WriteCommand(0x2C)
            else:
                Watch.WriteCommand(0x3C)
            
            Draw(ColorR,ColorG,ColorB)

if __name__ == '__main__':
    Watch.Initialise()
    Watch.SetFrame((0,0), (239,239))

    Watch.DISP_PIN.value = 0.5
    
    CheckScreenLocations()
    sleep(5)
