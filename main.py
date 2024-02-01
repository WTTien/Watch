from watch import Watch
from time import sleep
from math import floor
import argparse

watch = Watch()
parser = argparse.ArgumentParser()
parser.add_argument('--run', type = int)
args = parser.parse_args()
    

def Draw(ColorR, ColorG, ColorB):
    watch.WriteData(ColorR)
    watch.WriteData(ColorG)
    watch.WriteData(ColorB)

def FirstTry29JanSuccess():
    DrawColor = 240*240
    ColorR = 255 & 0xFF
    ColorG = 165 & 0xFF
    ColorB = 0 & 0xFF

    #Continuously draw a color on the screen
    watch.WriteCommand(0x2C)
    for i in range(DrawColor):
        Draw(ColorR, ColorG, ColorB)

    sleep(1)
    
    #Draw half canvas with one color and continue another half with another color
    ColorR = 0
    ColorG = 165
    ColorB = 150
    watch.WriteCommand(0x2C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)
    
    ColorR = 150
    ColorG = 165
    ColorB = 0
    watch.WriteCommand(0x3C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)

    sleep(1)

    #Draw half canvas with one color and continue with another color that paint whole canvas
    ColorR = 15
    ColorG = 15
    ColorB = 15
    watch.WriteCommand(0x2C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)
    
    ColorR = 255
    ColorG = 165
    ColorB = 255
    watch.WriteCommand(0x3C)
    for i in range (DrawColor):
        Draw(ColorR, ColorG, ColorB)

    sleep(1)

    #Draw half canvas with one color and draw whole canvas from the beginning from another color
    ColorR = 165
    ColorG = 0
    ColorB = 165
    watch.WriteCommand(0x2C)
    for i in range (round(DrawColor/2)):
        Draw(ColorR, ColorG, ColorB)
    
    ColorR = 165
    ColorG = 0
    ColorB = 165
    watch.WriteCommand(0x2C)
    for i in range (DrawColor):
        Draw(ColorR, ColorG, ColorB)

def CheckScreenLocations():
    BoxSize = 48
    FrameSize = 240

    for i in range(FrameSize):
        for j in range(FrameSize):
            if (floor(i/BoxSize) % 2) == (floor(j/BoxSize)%2):
                if args.run == 1:
                    ColorR = 0
                    ColorG = 0
                    ColorB = 0
                else:
                    ColorR = 255
                    ColorG = 255
                    ColorB = 255
            else:
                if args.run == 1:
                    ColorR = 255
                    ColorG = 255
                    ColorB = 255
                else:
                    ColorR = 0
                    ColorG = 0
                    ColorB = 0
            
            if i==0 and j==0:
                watch.WriteCommand(0x2C)
            else:
                watch.WriteCommand(0x3C)
            
            Draw(ColorR,ColorG,ColorB)

if __name__ == '__main__':
    watch.Initialise()
    watch.SetFrame((0,0), (239,239))

    watch.DISP_PIN.value = 0.5
    
    CheckScreenLocations()
    sleep(5)
