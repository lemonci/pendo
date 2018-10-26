
# coding: utf-8

# In[1]:


import time
start_time = time.time()
import os
import pandas as pd
import numpy as np
from os import path
READPATH = '/home/staff/mengqili/Linear/'
SAVEPATH = '/home/staff/mengqili/Linear/'
#read binary files function
def readpkl(filename):
        df = pd.read_pickle(READPATH+str(filename)+'.pkl')
        #df.columns = ['X', 'Y', 'Z', 'POINT', 'STROKE', 'CHARACTER', 'SAMPLE']
        df = df[['CHARACTER', 'STROKE', 'X', 'Y','Vertical']]
        #df = df.round(0).astype(int)
        return df

for fil in range(80,160):
    if path.isfile(READPATH+str(fil)+'.pkl'):
        raw = readpkl(fil)
        new = pd.DataFrame(columns = ['CHARACTER', 'STROKE', 'X', 'Y','Vertical'])
        #0->CHARACTER, 1->STROKE, 2->X, 3->Y, 4->Vertical, 5->X_diff, 6->Y_diff, 7_Angle
        new = new.append(raw.iloc[0])
        #drop the points too close to each other
        count = 0
        while count < raw.shape[0]:    
            x0 = raw.iloc[0]['X']
            y0 = raw.iloc[0]['Y']
            if (raw.iloc[count][2] - x0)**2 + (raw.iloc[count][3] - y0)**2 < 225:
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
                new.iloc[i,5] = new.iloc[i,2]-new.iloc[i-1,2]
                new.iloc[i,6] = new.iloc[i,3]-new.iloc[i-1,3]
                new.iloc[i,7] = round(np.angle(complex(new.iloc[i,5],new.iloc[i,6]),deg = True))
        new.to_pickle(SAVEPATH+str(fil)+".pkl")
    else:
        print(str(fil)+' does not exist')
print("--- %s seconds ---" % (time.time() - start_time))

