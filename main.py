from . import watch

if __name__ == '__main__':
    Watch = watch.Watch()
    Watch.Initialise()
    Watch.SetFrame((0,0), (239,239))

    Watch.WriteCommand(0x2C)
    
    DrawColor = 239
    ColorR = round(255*63/255) & 0x3F
    ColorG = (round(165*63/255) & 0x3F) << 6
    ColorB = (round(0*63/255) & 0x3F) << 12

    Color = ColorB | ColorG | ColorR

    for i in range(DrawColor):
        Watch.WriteData(Color)
