import pandas as pd
import numpy as np
from PIL import Image
import os
os.chdir('C:/Users/mengqili/Documents/Binary_new/')
filelist = os.listdir('C:/Users/mengqili/Documents/Binary_new/')

def readpkl(filename):
    df = pd.read_pickle(filename)
    dic = {}
    for a in range(90):
        dic[a] = []
    #df.columns = ['X', 'Y', 'Z', 'POINT', 'STROKE', 'CHARACTER', 'SAMPLE']
    df = df[['CHARACTER', 'STROKE','X', 'Y']]
    df['X'] = df['X']/20 - 180
    df['Y'] = (df['Y'] - 10000)/20
    return df

def post(df,colour,thearray):
    if colour != 3: 
        for index, row in df.iterrows():
            thearray[row['Y'], row['X'], colour] = 0 # paint the colours:
            # Cyan when red = 0; Yellow when blue = 0; Magenta when Green = 0; 
    else:
        for index, row in df.iterrows():
            thearray[row['Y'], row['X'], 0] = 127
            thearray[row['Y'], row['X'], 1] = 127
            thearray[row['Y'], row['X'], 2] = 127
            # paint the 4th colour Gray
    return thearray
            

def paintthefile(filename):
            
    dataint = readpkl(filename).round(0).astype(int) #read dataframe from pkl fil and convert to int

    rgb_array = np.ones((900, 900, 3), 'uint8') * 255 # build a "white" array // shape: 1200 * 900

    for i in range(0,90):
        rgb_array = post(dataint[dataint['CHARACTER']==i],i%4,rgb_array) # post each character to the array
    
    img = Image.fromarray(rgb_array) #convert array to image
    img.save(filename[0:len(filename)-3]+'png') #save the image

# how to use the fuctions:
#for fil in filelist:
#    paintthefile(fil)
def charprocess(wholedf, charnumber):
    chardf = wholedf[wholedf.iloc[:,0] == charnumber]
    chardf['Y'] -= int(charnumber/9)*80
    chardf['X'] -= charnumber%9*80
    chardf = chardf.round(0).astype(int)
    return chardf
    
def strokeprocess(chardf):
    strokenum = max(chardf.iloc[:,1]) + 1
    rgb_array = np.ones((900, 900, 3), 'uint8') * 255 # build a "white" array // shape: 1200 * 900

    for i in range(strokenum):
        strokedf = chardf[chardf.iloc[:,0] == i]
        strokedf['Y'] += int(i/9)*80
        strokedf['X'] += i%9*80
        rgb_array = post(strokedf[strokedf['STROKE']==i],3,rgb_array) # post each character to the array
    
    img = Image.fromarray(rgb_array) #convert array to image
    img.save('x'+'.png') #save the image
    
char = charprocess(readpkl('10.pkl'),0)
strokeprocess(char)
