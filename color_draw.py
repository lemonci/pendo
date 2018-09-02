#
import os
import pandas as pd
os.chdir('filepath')
filelist = os.listdir('filepath')
def readpkl(filename):
    df = pd.read_pickle(filename)
    dic = {}
    for a in range(90):
        dic[a] = []
    df.columns = ['X', 'Y', 'Z', 'POINT', 'STROKE', 'CHARACTER', 'SAMPLE']
    df = df[['CHARACTER','X', 'Y']]
    df['X'] = df['X']/20
    df['Y'] = (df['Y'] - 10000)/20
    for i in range(90):
        sub = df.loc[df['CHARACTER'] == i]
        sub = sub.drop(columns=['CHARACTER'])
        sub = sub.round(0).astype(int)
        dic[i] = list(zip(sub.X, sub.Y))
#   df = df.set_index('CHARACTER')
#    df = df.round(0).astype(int)
    return dic

data = readpkl('**.pkl')
# draw the image7
from tkinter import *

canvas_width = 900
canvas_height =800

master = Tk()

#scrollbar1 = Scrollbar(master)
#scrollbar1.pack(side=BOTTOM, fill=X)
#scrollbar2 = Scrollbar(master)
#scrollbar2.pack(side=RIGHT, fill=Y)

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()
color = {0 : 'bisque2', 1 : 'blue3', 2 : 'burlywood2', 3 : 'chartreuse', 4 : 'DarkOliveGreen4', 5 : 'blue', 6 : 'DarkOrchid3', 7 : 'dark salmon', 8 : 'azure3', 9 : 'DarkOliveGreen3', 10 : 'DarkOrange2', 11 : 'cyan', 12 : 'cornsilk2', 13 : 'aquamarine3', 14 : 'DarkOrange2', 15 : 'DarkGoldenrod4', 16 : 'deep pink', 17 : 'CadetBlue2', 18 : 'burlywood4', 19 : 'aquamarine', 20 : 'bisque3', 21 : 'coral4', 22 : 'cyan2', 23 : 'bisque4', 24 : 'aquamarine2', 25 : 'cyan3', 26 : 'brown1', 27 : 'chocolate1', 28 : 'DarkGoldenrod2', 29 : 'cadet blue', 30 : 'burlywood', 31 : 'dark sea green', 32 : 'chartreuse2', 33 : 'DarkOrchid3', 34 : 'cornsilk4', 35 : 'aquamarine4', 36 : 'DarkOrange4', 37 : 'dark slate gray', 38 : 'chartreuse3', 39 : 'DarkOrange1', 40 : 'DarkSeaGreen4', 41 : 'DarkSeaGreen3', 42 : 'DarkGoldenrod1', 43 : 'chartreuse4', 44 : 'dark orange', 45 : 'dark violet', 46 : 'dark goldenrod', 47 : 'coral1', 48 : 'blue violet', 49 : 'CadetBlue1', 50 : 'dark magenta', 51 : 'DarkOliveGreen2', 52 : 'brown3', 53 : 'dark slate blue', 54 : 'azure4', 55 : 'brown2', 56 : 'brown4', 57 : 'dark gray', 58 : 'chocolate', 59 : 'dark green', 60 :'chocolate2' , 61 : 'dim gray', 62 : 'coral2', 63 : 'cornsilk3', 64 : 'black', 65 : 'CadetBlue4', 66 : 'dark khaki', 67 : 'dark olive green', 68 : 'brown', 69 : 'DarkSeaGreen2', 70 : 'cyan4', 71 : 'DarkOrchid2', 72 : 'burlywood3', 73 : 'CadetBlue3', 74 : 'chocolate3', 75 : 'DarkOliveGreen1', 76 : 'dark red', 77 : 'DarkGoldenrod3', 78 : 'blue4', 79 : 'azure', 80 : 'dodger blue', 81 : 'dark turquoise', 82 : 'blue2', 83 : 'DarkOrchid1', 84 : 'coral3', 85 : 'dark orchid', 86 : 'cornflower blue', 87 : 'burlywood1', 88 : 'coral', 89 : 'chocolate4'}
for i in range(90):
    for (x, y) in data[i]:
        w.create_oval(x, y, x+1, y + 1, outline = color[i])
    
#scrollbar2.config(command=w.yview)
#scrollbar1.config(command=w.xview)
mainloop()
