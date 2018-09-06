import os
import pandas as pd
import numpy as np
os.chdir('filepath')
filelist = os.listdir('filepath')
#read binary files function
def readpkl(filename):
    df = pd.read_pickle(filename)
    df.columns = ['X', 'Y', 'Z', 'POINT', 'STROKE', 'CHARACTER', 'SAMPLE']
    df = df[['CHARACTER', 'STROKE', 'POINT','X', 'Y']]
    df = df.round(0).astype(int)
    return df
for fil in filelist:
    raw = readpkl(fil)
    new = pd.DataFrame(columns = ['CHARACTER', 'STROKE', 'POINT','X', 'Y'])
    new = new.append(raw.iloc[0])
    count = 0
    #drop the points too close to each other
    while count < raw.shape[0]:    
        x0 = raw.iloc[0]['X']
        y0 = raw.iloc[0]['Y']
        if x0-10 < raw.iloc[count][3] < x0+10 and y0-10 < raw.iloc[count][4] < y0+10:
            count += 1        
        else:
            new = new.append(raw.iloc[count])
            raw = raw.iloc[count+1:]
            count = 0
    #take difference and calculate angle
    new['X_diff'] = np.nan
    new['Y_diff'] = np.nan
    new['Angle'] = np.nan
    for i in range(1,new.shape[0]):
        if new.iloc[i,1] == new.iloc[i-1,1]:
            new.iloc[i,5] = new.iloc[i,3]-new.iloc[i-1,3]
            new.iloc[i,6] = new.iloc[i,4]-new.iloc[i-1,4]
    for i in range(1,new.shape[0]):
        new.iloc[i,7] = round(np.angle(complex(new.iloc[i,5],new.iloc[i,6]),deg = True))
    new.to_csv('str(fil)[len(fil)-4]'+'.csv')
