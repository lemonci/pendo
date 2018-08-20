import os
from scipy import misc
import numpy as np
import pandas as pd
import xlsxwriter


#establish the output dataframe dfo
dfo = pd.DataFrame([], columns=['top', 'bottom', 'left', 'right'])
# visit cropped image files
os.chdir(“<crop image path>")
filename = [f for f in os.listdir("<crop image path>") if f.endswith('.png')]
for a in filename:
    #read the image as an array
    face = misc.imread(a)
    np.set_printoptions(threshold=np.inf)
    #return the positions of all points not equal to zero
    data = np.argwhere(face != [0])
    #dispose layer information, leave x axis and y axis only
    df = pd.DataFrame({'Row':data[:,0],'Column':data[:,1]})
    #remove duplicate information (same point, different layers)
    df = df.drop_duplicates(subset=None, keep= 'first', inplace=False)
    #identify the most top, bottom, left and right cordinates of the image
    top = df['Row'].min()
    bottom = df['Row'].max()
    left = df['Column'].min()
    right = df['Column'].max()
    #append the above cordinates to the output dataframe
    dfp = pd.DataFrame([[top, bottom, left, right]], index=[a], columns=['top', 'bottom', 'left', 'right'])
    dfo = dfo.append(dfp)
# save the output dataframe to excel file
out_path = "<crop image path>/temp-excel.xlsx”
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
dfo.to_excel(writer, sheet_name='Sheet1')
writer.save()
