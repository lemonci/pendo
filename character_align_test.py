import os
from scipy import misc
import numpy as np
import pandas as pd
import xlsxwriter
os.chdir(“<crop image path>")
dfo = pd.DataFrame([], columns=['top', 'bottom', 'left', 'right'])
filename = [f for f in os.listdir("<crop image path>") if f.endswith('.png')]
for a in filename:
    face = misc.imread(a)
    np.set_printoptions(threshold=np.inf)
    data = np.argwhere(face != [0])
    df = pd.DataFrame({'Row':data[:,0],'Column':data[:,1]})
    df = df.drop_duplicates(subset=None, keep= 'first', inplace=False)
    top = df['Row'].min()
    bottom = df['Row'].max()
    left = df['Column'].min()
    right = df['Column'].max()
    dfp = pd.DataFrame([[top, bottom, left, right]], index=[a], columns=['top', 'bottom', 'left', 'right'])
    dfo = dfo.append(dfp)
out_path = "<crop image path>/temp-excel.xlsx”
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
dfo.to_excel(writer, sheet_name='Sheet1')
writer.save()
