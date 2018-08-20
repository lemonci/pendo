
from PIL import Image

os.chdir(“<image path>")
filename = [f for f in os.listdir("<image path>") if f.endswith('.png')]
for a in filename:
    img = Image.open(a) #read all images in filename list
    for hc in list(range(0, 10)):
        hs = 16 + hc * 69 #y axis crop start point
        for wc in list(range(0, 9)):
            ws = 16 + wc * 69 #x axis crop start point
            #(85, 16, 152, 83) == chu
            img.crop((ws, hs, ws + 67, hs + 67)).save(str(wc)+str(hc)+"_"+ a )  #crop image (67*67) and save file
