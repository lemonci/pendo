#import libraries and change to file directory
import os
import codecs
import re
import ast
import pandas as pd
import numpy as np
filelist = os.listdir('C:/Users/mengqili/Documents/Binary')
os.chdir('C:/Users/mengqili/Documents/Binary')
#preparation
df_final = pd.DataFrame()
df_grid = pd.DataFrame({'Grid_right_Xmax':np.tile([5250,6750,8250,9750,11250,12750,14250,15750, 17250], 10),\
                        'Grid_down_Ymax': np.repeat([12100,13600,15100,16600,18100,19600,21100,22600,24100,25600], 9), \
                        'Grid_left_Xmin':np.tile([3750, 5250,6750,8250,9750,11250,12750,14250,15750], 10), \
                        'Grid_up_Ymin': np.repeat([10600,12100,13600,15100,16600,18100,19600,21100,22600,24100], 9)
                       })
df_grid['Grid_Xcentre'] = df_grid[['Grid_right_Xmax', 'Grid_left_Xmin']].mean(axis=1)
df_grid['Grid_Ycentre'] = df_grid[['Grid_down_Ymax', 'Grid_up_Ymin']].mean(axis=1)
#read binary files function
def readpkl(filename):
    df = pd.read_pickle(filename)
    df.columns = ['X', 'Y', 'Z', 'POINT', 'STROKE', 'CHARACTER', 'SAMPLE']
    df = df[['SAMPLE', 'CHARACTER', 'STROKE','X', 'Y', 'Z']]
    df = df.set_index('CHARACTER', drop=False)
    df = df.round(0).astype(int)
    return df
for file in filelist:
    df_a = readpkl(file)
# create dataframe of max and min for XY cordinates
    df_max = pd.DataFrame(columns=['SAMPLE', 'CHARACTER', 'STROKE','X', 'Y', 'Z'])
    cmax = []
    cmin = []
    for char in range(0,90):
        subdf=df_a[ df_a.iloc[:,1]  == char]
        lmax = list(subdf.max())
        lmin = list(subdf.min())
        cmax.append(lmax)
        cmin.append(lmin)
    df_max = pd.DataFrame(cmax, columns=['SAMPLE', 'CHARACTER', 'STROKE','Xmax','Ymax','Zmax'])
    df_max = df_max.drop(['STROKE','Zmax'], axis=1)
    df_min = pd.DataFrame(cmin, columns=['SAMPLE', 'CHARACTER', 'STROKE','Xmin','Ymin','Zmin'])
    df_min = df_min.drop(['SAMPLE', 'CHARACTER', 'STROKE','Zmin'], axis=1)
    df_write = df_max.join(df_min)
#    df_wrtie = df_write.round(0).astype(int)
#calculate area
    df_area = pd.DataFrame()
    df_area['Xlen'] = df_write.Xmax - df_write.Xmin
    df_area['Ylen'] = df_write.Ymax-df_write.Ymin
    df_area['Area'] = df_area.Xlen*df_area.Ylen
#judge if the character is out of grid on a specific direction
    df_outofgrid = pd.DataFrame()
    df_outofgrid['out_right'] = ((df_grid.Grid_right_Xmax - df_write.Xmax)<0)*(df_write.Xmax - df_grid.Grid_right_Xmax)
    df_outofgrid['out_down'] = ((df_grid.Grid_down_Ymax - df_write.Ymax)<0)*(df_write.Ymax - df_grid.Grid_down_Ymax)
    df_outofgrid['out_left'] = ((df_grid.Grid_left_Xmin - df_write.Xmin)>0)*(df_write.Xmin - df_grid.Grid_left_Xmin)
    df_outofgrid['out_up'] = ((df_grid.Grid_up_Ymin - df_write.Ymin)>0)*(df_write.Ymin - df_grid.Grid_up_Ymin)
#    df_outofgrid = df_outofgrid.round(0).astype(int)
#create grid centre and calculate distance between the character centre and the gird centre on X and Y axes.
    df_centre = pd.DataFrame()
    df_centre['Xcentre'] = df_write[['Xmax', 'Xmin']].mean(axis=1)
    df_centre['Ycentre'] = df_write[['Ymax', 'Ymin']].mean(axis=1)
    df_centre['Xdistance'] = df_grid.Grid_Xcentre - df_centre.Xcentre
    df_centre['Ydistance'] = df_grid.Grid_Ycentre - df_centre.Ycentre
#    df_centre = df_centre.round(0).astype(int)
#calculate character spacing
    df_space = pd.DataFrame()
    df_space['Xspace'] = df_write['Xmin']-df_write['Xmax'].shift(1)
    df_space['Xspace'] = df_space['Xspace'].mask(df_space['Xspace'] < -10000)
    df_space['Yspace'] = df_write['Ymin']-df_write['Ymax'].shift(9)
#output for an accessment
    df_item = pd.concat([df_write, df_grid, df_outofgrid, df_area, df_centre, df_space], axis=1)
    df_final = df_final.append(df_item)
df_final.to_csv('result.csv')
