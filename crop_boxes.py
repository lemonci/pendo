from PIL import Image
filename = [f for f in os.listdir("filepath") if f.endswith('.png')]
print(filename)
for a in filename:
    img = Image.open(a)
    for hc in list(range(0, 9)):
        hs = 16 + hc * 69
        for wc in list(range(0, 8)):
            ws = 16 + wc * 69
            #(85, 16, 152, 83) == chu
            img.crop((ws, hs, ws + 67, hs + 67)).save(str(wc)+str(hc)+"_"+ a )
