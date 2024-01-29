from watch import Watch

if __name__ == '__main__':
    Watch = Watch()
    Watch.Initialise()
    Watch.SetFrame((0,0), (239,239))

    Watch.DISP_PIN.value = 0.5

    Watch.WriteCommand(0x2C)
    
    DrawColor = 239
    #ColorR = round(255*63/255) & 0x3F
    ColorR = 255 & 0xFF
    #ColorG = (round(165*63/255) & 0x3F) << 6
    ColorG = 165 & 0xFF
    #ColorB = (round(0*63/255) & 0x3F) << 12
    ColorB = 0 & 0xFF

    #Color = ColorB | ColorG | ColorR

    Watch.WriteData(ColorB)
    Watch.WriteData(ColorG)
    Watch.WriteData(ColorG)

    for i in range(DrawColor):
        Watch.WriteCommand(0x3C)
        Watch.WriteData(ColorB)
        Watch.WriteData(ColorG)
        Watch.WriteData(ColorR)
