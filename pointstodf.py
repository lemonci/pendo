#import libraries and change to file directory
import os
import codecs
import re
import pandas as pd
import ast
os.chdir('filepath')
#read the 243rd line of the html where the writing data is stored.
data = codecs.open('2.htm','r','utf-8').readlines()[242]
#split the data to the student hand writing part
real = re.split(',&quot;virtual', data, maxsplit=0, flags=0)[0]
real = re.split('&quot;:', real)[1]
real = ast.literal_eval(real)
#real = [re.split(r'real&quot;:\[(\[\[\[.+?\]\]\])\]',data)]

#test if the list conversion is successful.
'''for char in real:
    for stroke in char:
        for point in stroke:
            for axis in point:
                print(type(axis))
'''

#convert the hand writing data into dataframe
#accessment level
df_a = pd.DataFrame(columns=['character','stroke','X','Y','Z'])
#character level
c_count = 0
for char in real:
    df_c = pd.DataFrame(columns=['stroke','X','Y','Z'])
#stroke level
    s_count = 0
    for stroke in char:
        df_s = pd.DataFrame(stroke, columns=['X','Y','Z'])
        #add stroke count column
        df_s.insert(0, 'stroke', s_count)
        df_c = df_c.append(df_s)
        s_count += 1
    df_c.insert(0, 'character', c_count)
    df_a = df_a.append(df_c)
    c_count += 1

#get max and min values and join them to a new dataframe
df_max = pd.DataFrame(columns=['character','stroke','Xmax','Ymax','Zmax'])
cmax = []
cmin = []
for char in range(0,90):
    subdf=df_a[ df_a.iloc[:,0]  == char].copy()
    lmax = list(subdf.max())
    lmin = list(subdf.min())
    cmax.append(lmax)
    cmin.append(lmin)
df_max = pd.DataFrame(cmax, columns=['character','stroke','Xmax','Ymax','Zmax'])
df_max = df_max.drop(['stroke','Zmax'], axis=1)
df_min = pd.DataFrame(cmin, columns=['character','stroke','Xmin','Ymin','Zmin'])
df_min = df_min.drop(['character','stroke','Zmin'], axis=1)
df_out = df_max.join(df_min)
df_out = df_out.round(0).astype(int)

#Calculate spacing
df_out['Xspace'] = df_out['Xmin']-df_out['Xmax'].shift(1)
df_out['Xspace'] = df_out['Xspace'].mask(df_out['Xspace'] < -10000)
df_out['Yspace'] = df_out['Ymin']-df_out['Ymax'].shift(9)
