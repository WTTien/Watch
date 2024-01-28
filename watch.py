import spidev
from gpiozero import *
from time import sleep

class Watch:
    def __init__ (self):
        self.SPI = spidev.SpiDev(0, 0)
        self.SPI.max_speed_hz = 40000000
        self.SPI.mode = 0b01

        self.DC_PIN = DigitalOutputDevice(25, active_high = True, initial_value = False)
        self.RST_PIN = DigitalOutputDevice(27, active_high = True, initial_value = False)
        self.DISP_PIN = PWMOutputDevice(18, active_high = True, initial_value = 0, frequency=100000)

    def WriteData(self, data):
        self.DC_PIN.on()
        self.SPI.writebytes(data)

    def WriteCommand(self, data):
        self.DC_PIN.off()
        self.SPI.writebytes(data)

    def Initialise(self):
        self.RST_PIN.on()
        sleep(0.05)
        self.RST_PIN.off()
        sleep(0.05)

        self.WriteCommand(0xEF)     #INREGEN2
    
        self.WriteCommand(0xEB)
        self.WriteData(0x14)
        
        self.WriteCommand(0xFE)     #INREGEN1
        self.WriteCommand(0xEF)     #INREGEN1
        
        self.WriteCommand(0xEB)
        self.WriteData(0x14)
        
        self.WriteCommand(0x84)
        self.WriteData(0x40)
        
        self.WriteCommand(0x85)
        self.WriteData(0xFF)
        
        self.WriteCommand(0x86)
        self.WriteData(0xFF)
        
        self.WriteCommand(0x87)
        self.WriteData(0xFF)
        
        self.WriteCommand(0x88)
        self.WriteData(0x0A)
        
        self.WriteCommand(0x89)
        self.WriteData(0x21)
        
        self.WriteCommand(0x8A)
        self.WriteData(0x00)
        
        self.WriteCommand(0x8B)
        self.WriteData(0x80)
        
        self.WriteCommand(0x8C)
        self.WriteData(0x01)
        
        self.WriteCommand(0x8D)
        self.WriteData(0x01)
        
        self.WriteCommand(0x8E)
        self.WriteData(0xFF)
        
        self.WriteCommand(0x8F)
        self.WriteData(0xFF)
        
        
        self.WriteCommand(0xB6)
        self.WriteData(0x00)
        self.WriteData(0x00)
        
        self.WriteCommand(0x36)
        self.WriteData(0x18) #MADCTL_MX and RGB/BGR

        self.WriteCommand(0x3A)
        self.WriteData(0x06) #ColorModeData

        self.WriteCommand(0x90)
        self.WriteData(0x08)
        self.WriteData(0x08)
        self.WriteData(0x08)
        self.WriteData(0x08)
        
        self.WriteCommand(0xBD)
        self.WriteData(0x06)
        
        self.WriteCommand(0xBC)
        self.WriteData(0x00)
        
        self.WriteCommand(0xFF)
        self.WriteData(0x60)
        self.WriteData(0x01)
        self.WriteData(0x04)
    
        self.WriteCommand(0xC3) #Power
        self.WriteData(0x13)
        
        self.WriteCommand(0xC4) #Power
        self.WriteData(0x13)
        
        self.WriteCommand(0xC9) #Power
        self.WriteData(0x22)

        self.WriteCommand(0xBE)
        self.WriteData(0x11)
        
        self.WriteCommand(0xE1)
        self.WriteData(0x10)
        self.WriteData(0x0E)
        
        self.WriteCommand(0xDF)
        self.WriteData(0x21)
        self.WriteData(0x0c)
        self.WriteData(0x02)

        self.WriteCommand(0xF0) #Gamma
        self.WriteData(0x45)
        self.WriteData(0x09)
        self.WriteData(0x08)
        self.WriteData(0x08)
        self.WriteData(0x26)
        self.WriteData(0x2A)

        self.WriteCommand(0xF1) #Gamma
        self.WriteData(0x43)
        self.WriteData(0x70)
        self.WriteData(0x72)
        self.WriteData(0x36)
        self.WriteData(0x37)
        self.WriteData(0x6F)
        
        self.WriteCommand(0xF2) #Gamma
        self.WriteData(0x45)
        self.WriteData(0x09)
        self.WriteData(0x08)
        self.WriteData(0x08)
        self.WriteData(0x26)
        self.WriteData(0x2A)
        
        self.WriteCommand(0xF3) #Gamma
        self.WriteData(0x43)
        self.WriteData(0x70)
        self.WriteData(0x72)
        self.WriteData(0x36)
        self.WriteData(0x37)
        self.WriteData(0x6F)

        self.WriteCommand(0xED)
        self.WriteData(0x1B)
        self.WriteData(0x0B)
        
        self.WriteCommand(0xAE)
        self.WriteData(0x77)
        
        self.WriteCommand(0xCD)
        self.WriteData(0x63)

        self.WriteCommand(0x70)
        self.WriteData(0x07)
        self.WriteData(0x07)
        self.WriteData(0x04)
        self.WriteData(0x0E)
        self.WriteData(0x0F)
        self.WriteData(0x09)
        self.WriteData(0x07)
        self.WriteData(0x08)
        self.WriteData(0x03)

        self.WriteCommand(0xE8) #Frame Rate
        self.WriteData(0x34)

        self.WriteCommand(0x62)
        self.WriteData(0x18)
        self.WriteData(0x0D)
        self.WriteData(0x71)
        self.WriteData(0xED)
        self.WriteData(0x70)
        self.WriteData(0x70)
        self.WriteData(0x18)
        self.WriteData(0x0F)
        self.WriteData(0x71)
        self.WriteData(0xEF)
        self.WriteData(0x70)
        self.WriteData(0x70)
        
        self.WriteCommand(0x63)
        self.WriteData(0x18)
        self.WriteData(0x11)
        self.WriteData(0x71)
        self.WriteData(0xF1)
        self.WriteData(0x70)
        self.WriteData(0x70)
        self.WriteData(0x18)
        self.WriteData(0x13)
        self.WriteData(0x71)
        self.WriteData(0xF3)
        self.WriteData(0x70)
        self.WriteData(0x70)
        
        self.WriteCommand(0x64)
        self.WriteData(0x28)
        self.WriteData(0x29)
        self.WriteData(0xF1)
        self.WriteData(0x01)
        self.WriteData(0xF1)
        self.WriteData(0x00)
        self.WriteData(0x07)
        
        self.WriteCommand(0x66)
        self.WriteData(0x3C)
        self.WriteData(0x00)
        self.WriteData(0xCD)
        self.WriteData(0x67)
        self.WriteData(0x45)
        self.WriteData(0x45)
        self.WriteData(0x10)
        self.WriteData(0x00)
        self.WriteData(0x00)
        self.WriteData(0x00)
        
        self.WriteCommand(0x67)
        self.WriteData(0x00)
        self.WriteData(0x3C)
        self.WriteData(0x00)
        self.WriteData(0x00)
        self.WriteData(0x00)
        self.WriteData(0x01)
        self.WriteData(0x54)
        self.WriteData(0x10)
        self.WriteData(0x32)
        self.WriteData(0x98)

        self.WriteCommand(0x74)
        self.WriteData(0x10)
        self.WriteData(0x85)
        self.WriteData(0x80)
        self.WriteData(0x00)
        self.WriteData(0x00)
        self.WriteData(0x4E)
        self.WriteData(0x00)
        
        self.WriteCommand(0x98)
        self.WriteData(0x3e)
        self.WriteData(0x07)

        self.WriteCommand(0x35) #TEON
        self.WriteCommand(0x21) #INVON
        self.WriteCommand(0x11) #SLPOUT
        self.WriteCommand(0x29) #DISPON

    def SetFrame(self, start, end):

        startX, startY = start
        endX, endY = end
        
        self.WriteCommand(0x2A)
        self.WriteData((startX >> 8) & 0xFF)
        self.WriteData((startX) & 0xFF)
        self.WriteData((endX >> 8) & 0xFF)
        self.WriteData((endX) & 0xFF)
        
        self.WriteCommand(0x2B)
        self.WriteData((startY >> 8) & 0xFF)
        self.WriteData((startY) & 0xFF)
        self.WriteData((endY >> 8) & 0xFF)
        self.WriteData((endY) & 0xFF)
        
