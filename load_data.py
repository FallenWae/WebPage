#import sys
#sys.path.insert(0, 'C:\\Users\\SORickCH\\Desktop\\web\\pages')

#Import Librays from External Modules
import pandas as pd
from typing import List
import pathlib
import math
import matplotlib.pyplot as plt
import os
import getpass
import sys
import openpyxl
import warnings
import traceback
from time import sleep
import datetime
from datetime import timedelta , date
import string
from matplotlib.ticker import MaxNLocator
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, dash_table

# Print the App Name
print (r'''

  _____  _    _ __  __            _               _____  __  __  _____ 
 |  __ \| |  | |  \/  |     /\   | |        /\   |  __ \|  \/  |/ ____|
 | |__) | |__| | \  / |    /  \  | |       /  \  | |__) | \  / | (___  
 |  ___/|  __  | |\/| |   / /\ \ | |      / /\ \ |  _  /| |\/| |\___ \ 
 | |    | |  | | |  | |  / ____ \| |____ / ____ \| | \ \| |  | |____) |
 |_|    |_|  |_|_|  |_| /_/    \_\______/_/    \_\_|  \_\_|  |_|_____/ 
                                                                                                                                        
                                                                Designed by : Ricky So
''')


# In[2]:




# Define function for identifying the Current Platform
def map_id(idxx):
    if idxx == 33:
        return 'PL 1'
    elif idxx == 34:
        return 'PL 2'
    elif idxx == 35:
        return 'PL 3'
    elif idxx == 49:
        return 'PL 1'
    elif idxx == 50:
        return 'PL 2'
    elif idxx == 65:
        return 'PL 1'
    elif idxx == 66:
        return 'PL 2'
    elif idxx == 81:
        return 'PL 1'
    elif idxx == 82:
        return 'PL 2'
    elif idxx == 83:
        return 'PL 3'
    elif idxx == 84:
        return 'PL 4'
    elif idxx == 97:
        return 'PL 1'
    elif idxx == 98:
        return 'PL 2/3'
    elif idxx == 100:
        return 'PL 4'
    elif idxx == 113:
        return 'PL 1'
    elif idxx == 114:
        return 'PL 2'
    elif idxx == 129:
        return 'PL 1'
    elif idxx == 130:
        return 'PL 2'
    elif idxx == 145:
        return 'PL 1'
    elif idxx == 146:
        return 'PL 2/3'
    elif idxx == 148:
        return 'PL 4'
    elif idxx == 161:
        return 'PL1'
    elif idxx == 162:
        return 'PL 2'
    elif idxx == 177:
        return 'PL 1'
    elif idxx == 178:
        return 'PL 2'
    elif idxx == 193:
        return 'PL 1'
    elif idxx == 194:
        return 'PL 2'
    elif idxx == 209:
        return 'PL 1/2'
    elif idxx == 211:
        return 'PL 3/4'
    elif idxx == 225:
        return 'PL 1'
    elif idxx == 226:
        return 'PL 2'
    elif idxx == 337:
        return 'PL 1'
    elif idxx == 340:
        return 'PL 4'
    elif idxx == 353:
        return 'PL 1'
    elif idxx == 354:
        return 'PL 2'
    elif idxx == 375:
        return 'PL 7'
    elif idxx == 376:
        return 'PL 8'


# In[3]:


# Define function for identifying the Current Station Name
def map_stname(name):
    if name == 33:
        return 'Mong Kok'
    elif name == 34:
        return 'Mong Kok'
    elif name == 35:
        return 'Mong Kok'
    elif name == 49:
        return 'Kowloon Tong'
    elif name == 50:
        return 'Kowloon Tong'
    elif name == 65:
        return 'Tai Wai'
    elif name == 66:
        return 'Tai Wai'
    elif name == 81:
        return 'Sha Tin'
    elif name == 82:
        return 'Sha Tin'
    elif name == 83:
        return 'Sha Tin'
    elif name == 84:
        return 'Sha Tin'
    elif name == 97:
        return 'Fo Tan'
    elif name == 98:
        return 'Fo Tan'
    elif name == 100:
        return 'Fo Tan'
    elif name == 113:
        return 'Racecourse'
    elif name == 114:
        return 'Racecourse'
    elif name == 129:
        return 'University'
    elif name == 130:
        return 'University'
    elif name == 145:
        return 'Tai Po Market'
    elif name == 146:
        return 'Tai Po Market'
    elif name == 148:
        return 'Tai Po Market'
    elif name == 161:
        return 'Tai Wo'
    elif name == 162:
        return 'Tai Wo'
    elif name == 177:
        return 'Fanling'
    elif name == 178:
        return 'Fanling'
    elif name == 193:
        return 'Sheung Shui'
    elif name == 194:
        return 'Sheung Shui'
    elif name == 209:
        return 'Lo Wu'
    elif name == 211:
        return 'Lo Wu'
    elif name == 225:
        return 'Lok Ma Chau'
    elif name == 226:
        return 'Lok Ma Chau'
    elif name == 337:
        return 'New Hung Hom'
    elif name == 340:
        return 'New Hung Hom'
    elif name == 353:
        return 'Exhibition'
    elif name == 354:
        return 'Exhibition'
    elif name == 375:
        return 'Admiralty'
    elif name == 376:
        return 'Admiralty'


# Define function for extracting Opening_Closing_Time Data in a designated range
def opening_range(op_range):
    if (op_range >= 25.0) and (op_range < 30.0):
        return '25.0-29.9'
    elif (op_range >= 20.0) and (op_range < 25.0):
        return '20.0-24.9'
    elif (op_range >= 15.0) and (op_range < 20.0):
        return '15.0-19.9'
    elif (op_range >= 10.0) and (op_range < 15.0):
        return '10.0-14.9'
    elif (op_range >= 9.0) and (op_range < 10.0):
        return '9.0-9.9'
    elif (op_range >= 8.0) and (op_range < 9.0):
        return '8.0-8.9'
    elif (op_range >= 7.0) and (op_range < 8.0):
        return '7.0-7.9'
    elif (op_range >= 6.0) and (op_range < 7.0):
        return '6.0-6.9'
    elif (op_range >= 5.0) and (op_range < 6.0) :
        return '5.0-5.9'
    elif (op_range >= 4.0) and (op_range < 5.0):
        return '4.0-4.9'
    elif (op_range >= 3.0) and (op_range < 4.0):
        return '3.0-3.9'
    

# Get the current computer user's name
user = getpass.getuser()

# In[4]:


# Define function for calculating the date range
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


# In[5]:


# Taking the Date between StartDate and EndDate (Datetime Format Vaildation --> User Input )
date_format = '%Y-%m-%d'
StartDate = '2023-02-01'
EndDate = '2023-02-20'
#StartDate = str(input("Start From ? \n"))
#EndDate = str(input('End In ? \n'))
dt_list = []
today = pd.to_datetime(date.today())
constrain = pd.to_datetime(datetime.datetime(2000,1,1)) 


#while True:
try:
    
        sdate= datetime.datetime.strptime(StartDate, date_format)
        edate= datetime.datetime.strptime(EndDate, date_format)
        StartDate = pd.to_datetime(StartDate)
        EndDate = pd.to_datetime(EndDate)
        if  ((StartDate > constrain) & (EndDate < today)) == True:
     
             for dt in daterange(StartDate, EndDate):
                val = dt.strftime("%Y-%m-%d")
                dt_list.append(val)
        else:
            print('Invaild Date Range!!!')
            sleep(2)
            #os.system('python index_example.py')
            exit()

    
except:
            traceback.print_exc()
            sleep(2)
            #os.system('python index_example.py')
            #exit()
        #break

# In[6]:


try:
 df =[]

 def find_excel_files_in(directory:pathlib.Path) -> List[pathlib.Path]:
     files:List[pathlib.Path] = list()

     for filepath in directory.rglob('*.xlsx'):
         if filepath.is_file ():
             files.append(filepath)

     return files



 #List of your directories
 directories:List[str] = ['Alarms/']

 found_files:List[pathlib.Path] = list()

 for directory in directories:
     directory:pathlib.Path = pathlib.Path(directory)
     found_files.extend(find_excel_files_in(directory))
    
 with warnings.catch_warnings(record=True):
     warnings.simplefilter("always")
     for filepath in found_files:
         for dt1 in dt_list:
             if dt1 in filepath.stem:
                 print('Loading file {0}...'.format(filepath))
                 df.append(pd.read_excel(os.path.join(filepath),engine = 'openpyxl',skiprows = 1))

                
 df6 = pd.concat(df,axis = 0).reset_index()        
 df6 = pd.DataFrame(df6)
 df6 = df6.drop(df6[df6['预警状态'] == '恢复'].index, axis = 'rows')
 df6 = df6.drop(df6[df6['预警状态'] == '终止'].index, axis = 'rows')
 df6 = df6.drop(columns=["事件编码","模型来源","预警级别","特征名称","特征点位","特征点位数值","速度（km/h）","室外温度（℃）","index"],axis = 1)
    
except:
    traceback.print_exc()
    sleep(2)
    #exit()


# In[ ]:

def get_dataframe():
    return df6


# <! -- df6 --> original file (combined) || df7 --> After sorting by 车组 -- !> 
# DCU 1 --> df7 (OpeningTime) 
try:
 df7 = df6.copy()
 df7['sortout'] = df7['车组'].str.slice(1,3)
 df7['sortout'] = df7['sortout'].astype("int")
 df7 = df7.sort_values(by=['sortout'],ignore_index = True)
 df7.sort_values(by=['车组'],ignore_index = True, inplace = True)
 df7.loc[(df7['预警描述'].str.contains('DCU1_Door Opening Time') == True),'DCU1 Opening Time'] = "X"
 df7 = df7.dropna(axis=0 ,how = 'any')
    
except:
    df7 = df7.dropna(axis=0 ,how = 'any')
    pass


# DCU 2 --> df9 (OpeningTime)
try:
 df9 = df6.copy()
 df9['sortout'] = df9['车组'].str.slice(1,3)
 df9['sortout'] = df9['sortout'].astype("int")
 df9 = df9.sort_values(by=['sortout'],ignore_index = True)
 df9.loc[(df9['预警描述'].str.contains('DCU2_Door Opening Time') == True),'DCU2 Opening Time'] = "X"
 df9 = df9.dropna(axis=0 ,how = 'any')

except:
    df9 = df9.dropna(axis=0 ,how = 'any')
    pass


# DCU 3 --> df10 (OpeningTime)
try:
 df10 = df6.copy()
 df10['sortout'] = df10['车组'].str.slice(1,3)
 df10['sortout'] = df10['sortout'].astype("int")
 df10 = df10.sort_values(by=['sortout'],ignore_index = True)
 df10.loc[(df10['预警描述'].str.contains('DCU3_Door Opening Time') == True),'DCU3 Opening Time'] = "X"
 df10 = df10.dropna(axis=0 ,how = 'any')

except:
    df10 = df10.dropna(axis=0 ,how = 'any')
    pass



# DCU 4 --> df11 (OpeningTime)
try:
 df11 = df6.copy()
 df11['sortout'] = df11['车组'].str.slice(1,3)
 df11['sortout'] = df11['sortout'].astype("int")
 df11 = df11.sort_values(by=['sortout'],ignore_index = True) 
 df11.loc[(df11['预警描述'].str.contains('DCU4_Door Opening Time') == True),'DCU4 Opening Time'] = "X"
 df11 = df11.dropna(axis=0 ,how = 'any')

except:
    df11 = df11.dropna(axis=0 ,how = 'any')
    pass


# DCU 5 --> df12 (OpeningTime)
try:
 df12 = df6.copy()
 df12['sortout'] = df12['车组'].str.slice(1,3)
 df12['sortout'] = df12['sortout'].astype("int")
 df12 = df12.sort_values(by=['sortout'],ignore_index = True)
 df12.loc[(df12['预警描述'].str.contains('DCU5_Door Opening Time') == True),'DCU5 Opening Time'] = "X"
 df12 = df12.dropna(axis=0 ,how = 'any')

except:
    df12 = df12.dropna(axis=0 ,how = 'any')
    pass


# DCU 6 --> df13 (OpeningTime)
try:
 df13 = df6.copy()
 df13['sortout'] = df13['车组'].str.slice(1,3)
 df13['sortout'] = df13['sortout'].astype("int")
 df13 = df13.sort_values(by=['sortout'],ignore_index = True)
 df13.loc[(df13['预警描述'].str.contains('DCU6_Door Opening Time') == True),'DCU6 Opening Time'] = "X"
 df13 = df13.dropna(axis=0 ,how = 'any')

except:
    df13 = df13.dropna(axis=0 ,how = 'any')
    pass


# DCU 7 --> df14 (OpeningTime)
try:
 df14 = df6.copy()
 df14['sortout'] = df14['车组'].str.slice(1,3)
 df14['sortout'] = df14['sortout'].astype("int")
 df14 = df14.sort_values(by=['sortout'],ignore_index = True)
 df14.loc[(df14['预警描述'].str.contains('DCU7_Door Opening Time') == True),'DCU7 Opening Time'] = "X"
 df14 = df14.dropna(axis=0 ,how = 'any')

except:
    df14 = df14.dropna(axis=0 ,how = 'any')
    pass


# DCU 8 --> df15 (OpeningTime)
try:
 df15 = df6.copy()
 df15['sortout'] = df15['车组'].str.slice(1,3)
 df15['sortout'] = df15['sortout'].astype("int")
 df15 = df15.sort_values(by=['sortout'],ignore_index = True)
 df15.loc[(df15['预警描述'].str.contains('DCU8_Door Opening Time') == True),'DCU8 Opening Time'] = "X"
 df15 = df15.dropna(axis=0 ,how = 'any')

except:
    df15 = df15.dropna(axis=0 ,how = 'any')
    pass


# DCU 9 --> df16 (OpeningTime)
try:
 df16 = df6.copy()
 df16['sortout'] = df16['车组'].str.slice(1,3)
 df16['sortout'] = df16['sortout'].astype("int")
 df16 = df16.sort_values(by=['sortout'],ignore_index = True)
 df16.loc[(df16['预警描述'].str.contains('DCU9_Door Opening Time') == True),'DCU9 Opening Time'] = "X"
 df16 = df16.dropna(axis=0 ,how = 'any')

except:
    df16 = df16.dropna(axis=0 ,how = 'any')
    pass


# DCU 10 --> df17 (OpeningTime)
try:
 df17 = df6.copy()
 df17['sortout'] = df17['车组'].str.slice(1,3)
 df17['sortout'] = df17['sortout'].astype("int")
 df17 = df17.sort_values(by=['sortout'],ignore_index = True)
 df17.loc[(df17['预警描述'].str.contains('DCU10_Door Opening Time') == True),'DCU10 Opening Time'] = "X"
 df17 = df17.dropna(axis=0 ,how = 'any')

except:
    df17 = df17.dropna(axis=0 ,how = 'any')
    pass


# DCU 11 --> df18 (OpeningTime)
try:
 df18 = df6.copy()
 df18['sortout'] = df18['车组'].str.slice(1,3)
 df18['sortout'] = df18['sortout'].astype("int")
 df18 = df18.sort_values(by=['sortout'],ignore_index = True)
 df18.loc[(df18['预警描述'].str.contains('DCU11_Door Opening Time') == True),'DCU11 Opening Time'] = "X"
 df18 = df18.dropna(axis=0 ,how = 'any')

except:
    df18 = df18.dropna(axis=0 ,how = 'any')
    pass


# DCU 12 --> df19 (OpeningTime)
try:
 df19 = df6.copy()
 df19['sortout'] = df19['车组'].str.slice(1,3)
 df19['sortout'] = df19['sortout'].astype("int")
 df19 = df19.sort_values(by=['sortout'],ignore_index = True)
 df19.loc[(df19['预警描述'].str.contains('DCU12_Door Opening Time') == True),'DCU12 Opening Time'] = "X"
 df19 = df19.dropna(axis=0 ,how = 'any')

except:
    df19 = df19.dropna(axis=0 ,how = 'any')
    pass


# Merge all files into a single file (OpeningTime Only)
df21 = pd.concat([df7,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19],axis = 0)
df21 = df21.sort_values(by=['sortout'])
df21.drop(columns=['sortout'], axis = 1, inplace = True)
df21['Current_Station_Opening'] = df21['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df21['Current_Station_Opening'] = df21['Current_Station_Opening'].astype("int")
df21 = df21.reindex(columns=['车组','车厢','预警时间','Current_Station_Opening','DCU1 Opening Time','DCU2 Opening Time','DCU3 Opening Time','DCU4 Opening Time','DCU5 Opening Time','DCU6 Opening Time','DCU7 Opening Time','DCU8 Opening Time','DCU9 Opening Time','DCU10 Opening Time','DCU11 Opening Time','DCU12 Opening Time'])
df21 = df21.fillna(' ')


# Count the amount of Opening Time Alarm
df22 = pd.DataFrame(df21.loc[df21['DCU1 Opening Time'].astype(str).str.contains('X')]['DCU1 Opening Time'].agg(['count']))
df22['DCU2 Opening Time'] = df21.loc[df21['DCU2 Opening Time'].astype(str).str.contains('X')]['DCU2 Opening Time'].agg(['count'])
df22['DCU3 Opening Time'] = df21.loc[df21['DCU3 Opening Time'].astype(str).str.contains('X')]['DCU3 Opening Time'].agg(['count'])
df22['DCU4 Opening Time'] = df21.loc[df21['DCU4 Opening Time'].astype(str).str.contains('X')]['DCU4 Opening Time'].agg(['count'])
df22['DCU5 Opening Time'] = df21.loc[df21['DCU5 Opening Time'].astype(str).str.contains('X')]['DCU5 Opening Time'].agg(['count'])
df22['DCU6 Opening Time'] = df21.loc[df21['DCU6 Opening Time'].astype(str).str.contains('X')]['DCU6 Opening Time'].agg(['count'])
df22['DCU7 Opening Time'] = df21.loc[df21['DCU7 Opening Time'].astype(str).str.contains('X')]['DCU7 Opening Time'].agg(['count'])
df22['DCU8 Opening Time'] = df21.loc[df21['DCU8 Opening Time'].astype(str).str.contains('X')]['DCU8 Opening Time'].agg(['count'])
df22['DCU9 Opening Time'] = df21.loc[df21['DCU9 Opening Time'].astype(str).str.contains('X')]['DCU9 Opening Time'].agg(['count'])
df22['DCU10 Opening Time'] = df21.loc[df21['DCU10 Opening Time'].astype(str).str.contains('X')]['DCU10 Opening Time'].agg(['count'])
df22['DCU11 Opening Time'] = df21.loc[df21['DCU11 Opening Time'].astype(str).str.contains('X')]['DCU11 Opening Time'].agg(['count'])
df22['DCU12 Opening Time'] = df21.loc[df21['DCU12 Opening Time'].astype(str).str.contains('X')]['DCU12 Opening Time'].agg(['count'])


# Merge all files into a single file (OpeningTime with Count)
df23 = pd.concat([df21,df22],axis = 0)
df23 = df23.fillna(' ')
df23 = df23.set_axis(['车组 (Opening)','车厢 (Opening)','预警时间 (Opening)','Current_Station_Opening','DCU1 Opening Time','DCU2 Opening Time','DCU3 Opening Time','DCU4 Opening Time','DCU5 Opening Time','DCU6 Opening Time','DCU7 Opening Time','DCU8 Opening Time','DCU9 Opening Time','DCU10 Opening Time','DCU11 Opening Time','DCU12 Opening Time'],axis = 'columns')
df23 = df23.reset_index(drop = True)

# DCU 1 --> df24 (ClosingTime)
try:
 df24 = df6.copy()
 df24['sortout'] = df24['车组'].str.slice(1,3)
 df24['sortout'] = df24['sortout'].astype("int")
 df24 = df24.sort_values(by=['sortout'],ignore_index = True)
 df24.loc[(df24['预警描述'].str.contains('DCU1_Door Closing Time') == True),'DCU1 Closing Time'] = "X"
 #df7 = df7.drop(columns=['预警描述'],axis = 0)
 df24 = df24.dropna(axis=0 ,how = 'any')

except:
    df24 = df24.dropna(axis=0 ,how = 'any')
    pass


# DCU 2 --> df25 (ClosingTime)
try:
 df25 = df6.copy()
 df25['sortout'] = df25['车组'].str.slice(1,3)
 df25['sortout'] = df25['sortout'].astype("int")
 df25 = df25.sort_values(by=['sortout'],ignore_index = True)
 df25.loc[(df25['预警描述'].str.contains('DCU2_Door Closing Time') == True),'DCU2 Closing Time'] = "X"
 df25 = df25.dropna(axis=0 ,how = 'any')

except:
    df25 = df25.dropna(axis=0 ,how = 'any')
    pass


# DCU 3 --> df26 (ClosingTime)
try:
 df26 = df6.copy()
 df26['sortout'] = df26['车组'].str.slice(1,3)
 df26['sortout'] = df26['sortout'].astype("int")
 df26 = df26.sort_values(by=['sortout'],ignore_index = True)
 df26.loc[(df26['预警描述'].str.contains('DCU3_Door Closing Time') == True),'DCU3 Closing Time'] = "X"
 df26 = df26.dropna(axis=0 ,how = 'any')
    
except:
    df26 = df26.dropna(axis=0 ,how = 'any')
    pass


# DCU 4 --> df27 (ClosingTime)
try:
 df27 = df6.copy()
 df27['sortout'] = df27['车组'].str.slice(1,3)
 df27['sortout'] = df27['sortout'].astype("int")
 df27 = df27.sort_values(by=['sortout'],ignore_index = True)
 df27.loc[(df27['预警描述'].str.contains('DCU4_Door Closing Time') == True),'DCU4 Closing Time'] = "X"
 df27 = df27.dropna(axis=0 ,how = 'any')

except:
    df27 = df27.dropna(axis=0 ,how = 'any')
    pass


# DCU 5 --> df28 (ClosingTime)
try:
 df28 = df6.copy()
 df28['sortout'] = df28['车组'].str.slice(1,3)
 df28['sortout'] = df28['sortout'].astype("int")
 df28 = df24.sort_values(by=['sortout'],ignore_index = True)
 df28.loc[(df28['预警描述'].str.contains('DCU5_Door Closing Time') == True),'DCU5 Closing Time'] = "X"
 df28 = df28.dropna(axis=0 ,how = 'any')
    
except:
    df28 = df28.dropna(axis=0 ,how = 'any')
    pass


# DCU 6 --> df29 (ClosingTime)
try:
 df29 = df6.copy()
 df29['sortout'] = df29['车组'].str.slice(1,3)
 df29['sortout'] = df29['sortout'].astype("int")
 df29 = df29.sort_values(by=['sortout'],ignore_index = True)
 df29.loc[(df29['预警描述'].str.contains('DCU6_Door Closing Time') == True),'DCU6 Closing Time'] = "X"
 df29 = df29.dropna(axis=0 ,how = 'any')

except:
    df29 = df29.dropna(axis=0 ,how = 'any')
    pass  


# DCU 7 --> df30 (ClosingTime)
try:
 df30 = df6.copy()
 df30['sortout'] = df30['车组'].str.slice(1,3)
 df30['sortout'] = df30['sortout'].astype("int")
 df30 = df30.sort_values(by=['sortout'],ignore_index = True)
 df30.loc[(df30['预警描述'].str.contains('DCU7_Door Closing Time') == True),'DCU7 Closing Time'] = "X"
 df30 = df30.dropna(axis=0 ,how = 'any')
    
except:
    df30 = df30.dropna(axis=0 ,how = 'any')
    pass


# DCU 8 --> df31 (ClosingTime)
try:
 df31 = df6.copy()
 df31['sortout'] = df31['车组'].str.slice(1,3)
 df31['sortout'] = df31['sortout'].astype("int")
 df31 = df31.sort_values(by=['sortout'],ignore_index = True)
 df31.loc[(df31['预警描述'].str.contains('DCU8_Door Closing Time') == True),'DCU8 Closing Time'] = "X"
 df31 = df31.dropna(axis=0 ,how = 'any')

except:
    df31 = df31.dropna(axis=0 ,how = 'any')
    pass


# DCU 9 --> df32 (ClosingTime)
try:
 df32 = df6.copy()
 df32['sortout'] = df32['车组'].str.slice(1,3)
 df32['sortout'] = df32['sortout'].astype("int")
 df32 = df32.sort_values(by=['sortout'],ignore_index = True)
 df32.loc[(df32['预警描述'].str.contains('DCU9_Door Closing Time') == True),'DCU9 Closing Time'] = "X"
 df32 = df32.dropna(axis=0 ,how = 'any')

except:
    df32 = df32.dropna(axis=0 ,how = 'any')
    pass


# DCU 10 --> df33 (ClosingTime)
try:
 df33 = df6.copy()
 df33['sortout'] = df33['车组'].str.slice(1,3)
 df33['sortout'] = df33['sortout'].astype("int")
 df33 = df33.sort_values(by=['sortout'],ignore_index = True)
 df33.loc[(df33['预警描述'].str.contains('DCU10_Door Closing Time') == True),'DCU10 Closing Time'] = "X"
 df33 = df33.dropna(axis=0 ,how = 'any')

except:
    df33 = df33.dropna(axis=0 ,how = 'any')
    pass


# DCU 11 --> df34 (ClosingTime)
try:
 df34 = df6.copy()
 df34['sortout'] = df34['车组'].str.slice(1,3)
 df34['sortout'] = df34['sortout'].astype("int")
 df34 = df34.sort_values(by=['sortout'],ignore_index = True)
 df34.loc[(df34['预警描述'].str.contains('DCU11_Door Closing Time') == True),'DCU11 Closing Time'] = "X"
 df34 = df34.dropna(axis=0 ,how = 'any')
    
except:
    df34 = df34.dropna(axis=0 ,how = 'any')
    pass


# DCU 12 --> df35 (ClosingTime)
try:
 df35 = df6.copy()
 df35['sortout'] = df35['车组'].str.slice(1,3)
 df35['sortout'] = df35['sortout'].astype("int")
 df35 = df35.sort_values(by=['sortout'],ignore_index = True)
 df35.loc[(df35['预警描述'].str.contains('DCU12_Door Closing Time') == True),'DCU12 Closing Time'] = "X"
 df35 = df35.dropna(axis=0 ,how = 'any')
    
except:
    df35 = df35.dropna(axis=0 ,how = 'any')
    pass


# Opening Speed Alarm --> df56
df56 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df56['Current_Station_Opening'] = df56['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df56 = df56.dropna(axis = 0, how='any')
df56['Current_Station_Opening'] = df56['Current_Station_Opening'].astype("int")
df56['Opening DCU'] = df56['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Door Opening)')
df56['Opening Speed'] = df56['预警描述'].str.extract('(?:.*Door Opening Time)([0.0-9.0]+)')
df56['Opening Speed'] = df56['Opening Speed'].astype("float")
df56 = df56.drop(columns = '预警描述',axis = 1)
df56 = df56.reindex(columns=['车组','车厢','预警时间','Current_Station_Opening','Opening DCU','Opening Speed'])
df56 = df56.dropna(axis = 0 ,how = 'any')
df56 = df56.reset_index(drop=True)


# Closing Speed Alarm --> df57
df57 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df57['Current_Station_Closing'] = df57['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df57 = df57.dropna(axis = 0, how='any')
df57['Current_Station_Closing'] = df57['Current_Station_Closing'].astype("int")
df57['Closing DCU'] = df57['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Door Closing)')
df57['Closing Speed'] = df57['预警描述'].str.extract('(?:.*Door Closing Time)([0.0-9.0]+)')
df57['Closing Speed'] = df57['Closing Speed'].astype("float")
df57 = df57.drop(columns = '预警描述',axis = 1)
df57 = df57.reindex(columns=['车组','车厢','预警时间','Current_Station_Closing','Closing DCU','Closing Speed'])
df57 = df57.dropna(axis = 0 ,how = 'any')
df57 = df57.reset_index(drop=True)


# Opening Time Criteria  -->  df61
df61 = df6.copy()
df61['Hi'] = df61['预警描述'].str.extract('(?:.*>)([0.0-9.0]+)(?:)')
df61 = df61.drop(df61[df61['Hi'] == '0'].index, axis = 'rows')
df61 = df61.dropna(axis=0,how='any')
df61.loc[(df61['预警描述'].str.contains('Door Opening Time') == True),'Opening Standard'] = '> ' + df61['Hi']
df61 = df61.dropna(axis = 0, how = 'any')
df61 = pd.DataFrame(df61['Opening Standard'])[:1]
df61 = df61.reset_index(drop = True)


# Closing Time Criteria  -->  df62
df62 = df6.copy()
df62['Hi'] = df62['预警描述'].str.extract('(?:.*>)([0.0-9.0]+)(?:)')
df62 = df62.drop(df62[df62['Hi'] == '0'].index, axis = 'rows')
df62 = df62.dropna(axis=0,how='any')
df62.loc[(df62['预警描述'].str.contains('Door Closing Time') == True),'Closing Standard'] = '> ' + df62['Hi']
df62 = df62.dropna(axis = 0, how = 'any')
df62 = pd.DataFrame(df62['Closing Standard'])[:1]
df62 = df62.reset_index(drop = True)


# Counting the amount of Opening Time and Closing Time Value (Using Groupby)
# Opening Time --> df58  ||  Closing Time --> df59  ||  Overall Opening Time with standard --> df60
df58 = df56.copy()
df58 = pd.DataFrame(df58.groupby(['Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
df59 = df57.copy()
df59 = pd.DataFrame(df59.groupby(['Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
df167 = pd.DataFrame(pd.concat([df58,df59],axis=1))
df167 = df167.set_axis(['Opening Speed (Group_Count)','Opening Time Count','Closing Speed (Group_Count)','Closing Time Count'],axis = 'columns')
df60 = pd.DataFrame(pd.concat([df56,df61],axis=1))
df60 = df60.set_axis(['车组 (Opening)', '车厢 (Opening)','预警时间 (Opening)', 'Current_Station_Opening','Opening DCU','Opening Speed','Opening Standard'], axis= 'columns')

# Overall Closing Time with standard   -->   df63
df63 = pd.DataFrame(pd.concat([df57,df62],axis=1))
df63 = df63.set_axis(['车组 (Closing)','车厢 (Closing)','预警时间 (Closing)','Current_Station_Closing','Closing DCU','Closing Speed','Closing Standard'],axis = 'columns')


# Generate Graph for analyzing OpeningTime Alarm (Normal) -->  df58
try:
    df138 = df58.copy()
    df214 = df58.copy()
    df215 = df58.copy()
    df58 = df58[(df58['Opening Speed'] >3) & (df58['Opening Speed'] <= 4 )]
    df58.plot.barh(x='Opening Speed',y = 'Opening Time Count', rot=0, width = 0.7,figsize = (12,12))
    plt.title('Opening Time Distribution (Believed to be Normal Cases)')
    plt.xlabel('Count')
    plt.ylabel('Opening Speed')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Opening_Time_Distribution (Believed to be Normal Cases).png')
    plt.close()
    
except:
    print('No Opening Time Alarm Graph (Believed to be Normal Cases)')
    plt.close()


# Generate Graph for analyzing OpeningTime Alarm (Potentially Problematic) -->  df214
try:
    df214 = df214[(df214['Opening Speed'] > 4) & (df214['Opening Speed'] < 8 )]
    df214.plot.barh(x='Opening Speed',y = 'Opening Time Count', rot=0, width = 0.7,figsize = (12,12))
    plt.title('Opening Time Distribution (Potentially Problematic)')
    plt.xlabel('Count')
    plt.ylabel('Opening Speed')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Opening_Time_Distribution (Potentially Problematic).png')
    plt.close()
    
except:
    print('No Opening Time Alarm Graph (Potentially Problematic)')
    plt.close()


# Generate Graph for analyzing OpeningTime Alarm (Abnormal) -->  df215
try:
    df215 = df215[(df215['Opening Speed'] >=8)]
    df215.plot.barh(x='Opening Speed',y = 'Opening Time Count', rot=0, width = 0.7,figsize = (12,12))
    plt.title('Opening Time Distribution (Abnormal)')
    plt.xlabel('Count')
    plt.ylabel('Opening Speed')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Opening_Time_Distribution (Abnormal).png')
    plt.close()
    
except:
    print('No Opening Time Alarm Graph (Abnoraml)')
    plt.close()


# Generate Graph for analyzing OpeningTime Alarm (Zero) --> df138
try:
 df138 = df138.drop(df138[df138['Opening Time Count'] < 100].index, axis = 'rows')
 #df138.loc[(df138['Opening Time Count'].index > 100)]
 df138.plot.barh(x='Opening Speed',y = 'Opening Time Count', rot=0, width = 0.7,figsize = (12,12))
 plt.title('Opening Time Distribution (Zero)')
 plt.xlabel('Count')
 plt.ylabel('Opening Speed')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Opening_Time_Distribution (Zero).png')
 plt.close()
    
except:
    print('No Opening Time Alarm Graph (Zero)')
    plt.close()


# Generate Graph for analyzing ClosingTime Alarm (Normal) --> df59
try:
 
 df153 = df59.copy()
 df242 = df59.copy()
 df243 = df59.copy()   
 df59 = df59[(df59['Closing Speed'] >3) & (df59['Closing Speed'] <= 4 )]
 df59.plot.barh(x='Closing Speed',y = 'Closing Time Count', rot=0, width = 0.7,figsize = (12,12))
 plt.title('Closing Time Distribution (Believed to be Normal Cases)')
 plt.xlabel('Count')
 plt.ylabel('Closing Speed')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Closing_Time_Distribution (Believed to be Normal Cases).png')
 plt.close()
    
except:
    print('No Closing Time Alarm Graph (Believed to be Normal Cases)')
    plt.close()


# Generate Graph for analyzing ClosingTime Alarm (Potentially Problematic) --> df242
try:
  
 df242 = df242[(df242['Closing Speed'] > 4) & (df242['Closing Speed'] < 8 )]
 df242.plot.barh(x='Closing Speed',y = 'Closing Time Count', rot=0, width = 0.7,figsize = (12,12))
 new_list = range(math.floor(min(list(df242['Closing Time Count']))), math.ceil(max(list(df242['Closing Time Count']))+1))
 plt.xticks(new_list)
 plt.title('Closing Time Distribution (Potentially Problematic)')
 plt.xlabel('Count')
 plt.ylabel('Closing Speed')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Closing_Time_Distribution (Potentially Problematic).png')
 plt.close()
    
except:
    print('No Closing Time Alarm Graph (Potentially Problematic)')
    plt.close()


# Generate Graph for analyzing ClosingTime Alarm (Abnormal) --> df243
try:
  
 df243 = df243[(df243['Closing Speed'] >=8)]
 df243.plot.barh(x='Closing Speed',y = 'Closing Time Count', rot=0, width = 0.7,figsize = (12,12))
 new_list = range(math.floor(min(list(df243['Closing Time Count']))), math.ceil(max(list(df243['Closing Time Count']))+1))
 plt.xticks(new_list)
 plt.title('Closing Time Distribution (Abnormal)')
 plt.xlabel('Count')
 plt.ylabel('Closing Speed')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Closing_Time_Distribution (Abnormal).png')
 plt.close()
    
except:
    print('No Closing Time Alarm Graph (Abnormal)')
    plt.close()


# Generate Graph for analyzing ClosingTime Alarm (Zero)
try:
    
 df153 = df153.drop(df153[df153['Closing Speed'] > 3.5].index, axis = 'rows')
 df153.plot.barh(x='Closing Speed',y = 'Closing Time Count', rot=0, width = 0.7,figsize = (12,12))
 plt.title('Closing Time Distribution (Zero)')
 plt.xlabel('Count')
 plt.ylabel('Closing Speed')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Closing_Time_Distribution (Zero).png')
 plt.close()
    
except:
    print('No Closing Time Alarm Graph (Zero)')
    plt.close()


#####################################################################################################################################################################################

# Believed to be Normal Cases (Opening Time)  --> df139
df139 = df56.copy()
df139 = df139[(df139['Opening Speed'] >3) & (df139['Opening Speed'] <= 4 )]


# Top Ten DCU Opening Time Excel File (Normal) --> df114 
df114 = df139.copy()
df114['车厢'] = df114['车厢'].astype(str).str.zfill(2)
df114['Source'] = df114['车组']+ '_' + df114['车厢'] + '_' + df114['Opening DCU']
df114['预警时间'] = df114['预警时间'].str.slice(0,10)
df114 = pd.DataFrame(df114.groupby(['Source','Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
df114 = df114.reindex(columns=['Source','Opening Speed','Opening Time Count'])


# Top Ten DCU Opening Time Graph (Normal) --> df115
try:   
 df115 = df114.nlargest(n = 10 , columns =['Opening Time Count'])
 df115 = df115.sort_values(by='Opening Time Count',ignore_index = True, ascending = False)
 colors = {3.8: 'r' , 3.9: 'b' , 4.0: 'g'}
 colos = list(df115['Opening Speed'].map(colors))
 df115.plot.barh(x = 'Source', y= 'Opening Time Count', color= colos,figsize = (12,12))
 new_list = range(math.floor(min(list(df115['Opening Time Count']))), math.ceil(max(list(df115['Opening Time Count']))+1))
 plt.xticks(new_list)
 plt.title('Top Ten Opening Time DCU')
 plt.legend(['3.8: Red \n3.9: Blue\n4.0: Green'],loc='best',edgecolor = 'black',prop = {'size':15})
 plt.xlabel('Count')
 plt.ylabel('Opening Time DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Top_Ten_Opening_Time_DCU (Normal).png')
 plt.close()
except:
    print('No Top Ten Opening Time Result (Normal)')
    plt.close()


# Top 1 No. of Opening Time Trend (Normal) --> df118
try:
 top1 = df115.iloc[0]['Source']
 t1_speed= df115.iloc[0]['Opening Speed']
 df118 = df56.copy()
 df118['车厢'] = df118['车厢'].astype(str).str.zfill(2)
 df118['Source'] = df118['车组']+ '_' + df118['车厢'] + '_' + df118['Opening DCU']
 df118 = df118.loc[(df118['Source'] == top1) & (df118['Opening Speed'] == t1_speed)]
 df118['预警时间'] = df118['预警时间'].str.slice(0,10)
 df118= pd.DataFrame(df118.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df118 = df118.sort_values(by=['预警时间'])
 ax = df118.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df118.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df118['Opening Time Count']))), math.ceil(max(list(df118['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top1 +' '+ 'Opening Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Opening Time Trend (Normal)')
    plt.close()


#Top 2 No. of Opening Time Trend (Normal) --> df119
try:
 top2 = df115.iloc[1]['Source']
 t2_speed= df115.iloc[1]['Opening Speed']
 df119 = df56.copy()
 df119['车厢'] = df119['车厢'].astype(str).str.zfill(2)
 df119['Source'] = df119['车组']+ '_' + df119['车厢'] + '_' + df119['Opening DCU']
 df119 = df119.loc[(df119['Source'] == top2) & (df119['Opening Speed'] == t2_speed)]
 df119['预警时间'] = df119['预警时间'].str.slice(0,10)
 df119= pd.DataFrame(df119.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df119 = df119.sort_values(by=['预警时间'])
 ax = df119.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df119.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df119['Opening Time Count']))), math.ceil(max(list(df119['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top2 +' '+ 'Opening Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Opening Time Trend (Normal)')
    plt.close()


#Top 3 No. of Opening Time Trend (Normal) --> df120
try:
 top3 = df115.iloc[2]['Source']
 t3_speed= df115.iloc[2]['Opening Speed']
 df120 = df56.copy()
 df120['车厢'] = df120['车厢'].astype(str).str.zfill(2)
 df120['Source'] = df120['车组']+ '_' + df120['车厢'] + '_' + df120['Opening DCU']
 df120 = df120.loc[(df120['Source'] == top3) & (df120['Opening Speed'] == t3_speed)]
 df120['预警时间'] = df120['预警时间'].str.slice(0,10)
 df120= pd.DataFrame(df120.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df120 = df120.sort_values(by=['预警时间'])
 ax = df120.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df120.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df120['Opening Time Count']))), math.ceil(max(list(df120['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top3 +' '+ 'Opening Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Opening Time Trend (Normal)')
    plt.close()


#Top 4 No. of Opening Time Trend (Normal) --> df121
try:
 top4 = df115.iloc[3]['Source']
 t4_speed= df115.iloc[3]['Opening Speed']
 df121 = df56.copy()
 df121['车厢'] = df121['车厢'].astype(str).str.zfill(2)
 df121['Source'] = df121['车组']+ '_' + df121['车厢'] + '_' + df121['Opening DCU']
 df121 = df121.loc[(df121['Source'] == top4) & (df121['Opening Speed'] == t4_speed)]
 df121['预警时间'] = df121['预警时间'].str.slice(0,10)
 df121= pd.DataFrame(df121.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df121 = df121.sort_values(by=['预警时间'])
 ax = df121.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df121.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df121['Opening Time Count']))), math.ceil(max(list(df121['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top4 +' '+ 'Opening Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Opening Time Trend (Normal)')
    plt.close()


#Top 5 No. of Opening Time Trend (Normal) --> df122
try:
 top5 = df115.iloc[4]['Source']
 t5_speed= df115.iloc[4]['Opening Speed']
 df122 = df56.copy()
 df122['车厢'] = df122['车厢'].astype(str).str.zfill(2)
 df122['Source'] = df122['车组']+ '_' + df122['车厢'] + '_' + df122['Opening DCU']
 df122 = df122.loc[(df122['Source'] == top5) & (df122['Opening Speed'] == t5_speed)]
 df122['预警时间'] = df122['预警时间'].str.slice(0,10)
 df122= pd.DataFrame(df122.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df122 = df122.sort_values(by=['预警时间'])
 ax = df122.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df122.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df122['Opening Time Count']))), math.ceil(max(list(df122['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top5 +' '+ 'Opening Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Opening Time Trend (Normal)')
    plt.close()


#Top 6 No. of Opening Time Trend (Normal) --> df123
try:
 top6 = df115.iloc[5]['Source']
 t6_speed= df115.iloc[5]['Opening Speed']
 df123 = df56.copy()
 df123['车厢'] = df123['车厢'].astype(str).str.zfill(2)
 df123['Source'] = df123['车组']+ '_' + df123['车厢'] + '_' + df123['Opening DCU']
 df123 = df123.loc[(df123['Source'] == top6) & (df123['Opening Speed'] == t6_speed)]
 df123['预警时间'] = df123['预警时间'].str.slice(0,10)
 df123= pd.DataFrame(df123.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df123 = df123.sort_values(by=['预警时间'])
 ax = df123.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df123.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df123['Opening Time Count']))), math.ceil(max(list(df123['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top6 +' '+ 'Opening Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Opening Time Trend (Normal)')
    plt.close()


#Top 7 No. of Opening Time Trend (Normal) --> df124
try:
 top7 = df115.iloc[6]['Source']
 t7_speed= df115.iloc[6]['Opening Speed']
 df124 = df56.copy()
 df124['车厢'] = df124['车厢'].astype(str).str.zfill(2)
 df124['Source'] = df124['车组']+ '_' + df124['车厢'] + '_' + df124['Opening DCU']
 df124 = df124.loc[(df124['Source'] == top7) & (df124['Opening Speed'] == t7_speed)]
 df124['预警时间'] = df124['预警时间'].str.slice(0,10)
 df124= pd.DataFrame(df124.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df124 = df124.sort_values(by=['预警时间'])
 ax = df124.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df124.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df124['Opening Time Count']))), math.ceil(max(list(df124['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top7 +' '+ 'Opening Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()

except:
    print('No Top7 Opening Time Trend (Normal)')
    plt.close()


#Top 8 No. of Opening Time Trend (Normal) --> df125
try:
 top8 = df115.iloc[7]['Source']
 t8_speed= df115.iloc[7]['Opening Speed']
 df125 = df56.copy()
 df125['车厢'] = df125['车厢'].astype(str).str.zfill(2)
 df125['Source'] = df125['车组']+ '_' + df125['车厢'] + '_' + df125['Opening DCU']
 df125 = df125.loc[(df125['Source'] == top8) & (df125['Opening Speed'] == t8_speed)]
 df125['预警时间'] = df125['预警时间'].str.slice(0,10)
 df125= pd.DataFrame(df125.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df125 = df125.sort_values(by=['预警时间'])
 ax = df125.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df125.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df125['Opening Time Count']))), math.ceil(max(list(df125['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top8 +' '+ 'Opening Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()

except:
    print('No Top8 Opening Time Trend (Normal)')
    plt.close()


#Top 9 No. of Opening Time Trend (Normal) --> df126
try:
 top9 = df115.iloc[8]['Source']
 t9_speed= df115.iloc[8]['Opening Speed']
 df126 = df56.copy()
 df126['车厢'] = df126['车厢'].astype(str).str.zfill(2)
 df126['Source'] = df126['车组']+ '_' + df126['车厢'] + '_' + df126['Opening DCU']
 df126 = df126.loc[(df126['Source'] == top9) & (df126['Opening Speed'] == t9_speed)]
 df126['预警时间'] = df126['预警时间'].str.slice(0,10)
 df126= pd.DataFrame(df126.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df126 = df126.sort_values(by=['预警时间'])
 ax = df126.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df126.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df126['Opening Time Count']))), math.ceil(max(list(df126['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top9 +' '+ 'Opening Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Opening Time Trend (Normal)')
    plt.close()


#Top 10 No. of Opening Time Trend (Normal) --> df127
try:
 top10 = df115.iloc[9]['Source']
 t10_speed= df115.iloc[9]['Opening Speed']
 df127 = df56.copy()
 df127['车厢'] = df127['车厢'].astype(str).str.zfill(2)
 df127['Source'] = df127['车组']+ '_' + df127['车厢'] + '_' + df127['Opening DCU']
 df127 = df127.loc[(df127['Source'] == top10) & (df127['Opening Speed'] == t10_speed)]
 df127['预警时间'] = df127['预警时间'].str.slice(0,10)
 df127= pd.DataFrame(df127.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df127 = df127.sort_values(by=['预警时间'])
 ax = df127.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df127.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df127['Opening Time Count']))), math.ceil(max(list(df127['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top10 +' '+ 'Opening Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Believed_To_Be_Normal\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Opening Time Trend (Normal)')
    plt.close()


# Believed to be Potentially Problematic Cases (Opening Time)  --> df140
df216 = df56.copy()
df216 = df216[(df216['Opening Speed'] > 4) & (df216['Opening Speed'] < 8 )]


# Top Ten DCU Opening Time Excel File (Potentially Problematic) --> df217 
df217 = df216.copy()
df217['车厢'] = df217['车厢'].astype(str).str.zfill(2)
df217['Source'] = df217['车组']+ '_' + df217['车厢'] + '_' + df217['Opening DCU']
df217['预警时间'] = df217['预警时间'].str.slice(0,10)
df217 = pd.DataFrame(df217.groupby(['Source','Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
df217 = df217.reindex(columns=['Source','Opening Speed','Opening Time Count'])
df217 = df217.sort_values(by=['Opening Speed'])


# Top Ten DCU Opening Time Graph (Potentially Problematic) --> df218

try:
    df218 = df217.nlargest(n = 10 , columns =['Opening Time Count'])
    df218 = df218.sort_values(by=['Opening Time Count'],ignore_index = True, ascending = False)
    colors = {4.1: 'r' , 4.2: 'g', 4.3: 'b', 4.4: '#F700FF',4.5: '#FF9100' , 4.6: '#AB00FF' ,4.7: '#00F5D4'}
    colos = list(df218['Opening Speed'].map(colors)) 
    df218.plot.barh(x = 'Source', y= 'Opening Time Count', color= colos ,figsize = (12,12))
    new_list = range(math.floor(min(list(df218['Opening Time Count']))), math.ceil(max(list(df218['Opening Time Count']))+1))
    plt.xticks(new_list)
    plt.title('Top Ten Opening Time DCU (Potentially Problematic)')
    plt.legend(['4.1: Red \n4.2: Green\n4.3: Blue\n4.4: Pink\n4.5: Orange \n4.6: Purple\n4.7: Cyan'],loc='best',edgecolor = 'black',prop = {'size':15})
    plt.xlabel('Count')
    plt.ylabel('Opening Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Top_Ten_Opening_Time_DCU (Potentially Problematic).png')
    plt.close()
    
except:
    print('No Top Ten Opening Time Result (Potentially Problematic)')
    plt.close()


# Top 1 No. of Opening Time Trend (Potentially Problematic) --> df219
try:
 top1 = df218.iloc[0]['Source']
 t1_speed= df218.iloc[0]['Opening Speed']
 df219 = df56.copy()
 df219['车厢'] = df219['车厢'].astype(str).str.zfill(2)
 df219['Source'] = df219['车组']+ '_' + df219['车厢'] + '_' + df219['Opening DCU']
 df219 = df219.loc[(df219['Source'] == top1) & (df219['Opening Speed'] == t1_speed)]
 df219['预警时间'] = df219['预警时间'].str.slice(0,10)
 df219= pd.DataFrame(df219.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df219 = df219.sort_values(by=['预警时间'])
 ax = df219.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df219.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df219['Opening Time Count']))), math.ceil(max(list(df219['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top1 +' '+ 'Opening Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 2 No. of Opening Time Trend (Potentially Problematic) --> df220
try:
 top2 = df218.iloc[1]['Source']
 t2_speed= df218.iloc[1]['Opening Speed']
 df220 = df56.copy()
 df220['车厢'] = df220['车厢'].astype(str).str.zfill(2)
 df220['Source'] = df220['车组']+ '_' + df220['车厢'] + '_' + df220['Opening DCU']
 df220 = df220.loc[(df220['Source'] == top2) & (df220['Opening Speed'] == t2_speed)]
 df220['预警时间'] = df220['预警时间'].str.slice(0,10)
 df220= pd.DataFrame(df220.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df220 = df220.sort_values(by=['预警时间'])
 ax = df220.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df220.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df220['Opening Time Count']))), math.ceil(max(list(df220['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top2 +' '+ 'Opening Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 3 No. of Opening Time Trend (Potentially Problematic) --> df221
try:
 top3 = df218.iloc[2]['Source']
 t3_speed= df218.iloc[2]['Opening Speed']
 df221 = df56.copy()
 df221['车厢'] = df221['车厢'].astype(str).str.zfill(2)
 df221['Source'] = df221['车组']+ '_' + df221['车厢'] + '_' + df221['Opening DCU']
 df221 = df221.loc[(df221['Source'] == top3) & (df221['Opening Speed'] == t3_speed)]
 df221['预警时间'] = df221['预警时间'].str.slice(0,10)
 df221= pd.DataFrame(df221.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df221 = df221.sort_values(by=['预警时间'])
 ax = df221.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df221.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df221['Opening Time Count']))), math.ceil(max(list(df221['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top3 +' '+ 'Opening Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 4 No. of Opening Time Trend (Potentially Problematic) --> df222
try:
 top4 = df218.iloc[3]['Source']
 t4_speed= df218.iloc[3]['Opening Speed']
 df222 = df56.copy()
 df222['车厢'] = df222['车厢'].astype(str).str.zfill(2)
 df222['Source'] = df222['车组']+ '_' + df222['车厢'] + '_' + df222['Opening DCU']
 df222 = df222.loc[(df222['Source'] == top4) & (df222['Opening Speed'] == t4_speed)]
 df222['预警时间'] = df222['预警时间'].str.slice(0,10)
 df222= pd.DataFrame(df222.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df222 = df222.sort_values(by=['预警时间'])
 ax = df222.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df222.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df222['Opening Time Count']))), math.ceil(max(list(df222['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top4 +' '+ 'Opening Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 5 No. of Opening Time Trend (Potentially Problematic) --> df223
try:
 top5 = df218.iloc[4]['Source']
 t5_speed= df218.iloc[4]['Opening Speed']
 df223 = df56.copy()
 df223['车厢'] = df223['车厢'].astype(str).str.zfill(2)
 df223['Source'] = df223['车组']+ '_' + df223['车厢'] + '_' + df223['Opening DCU']
 df223 = df223.loc[(df223['Source'] == top5) & (df223['Opening Speed'] == t5_speed)]
 df223['预警时间'] = df223['预警时间'].str.slice(0,10)
 df223= pd.DataFrame(df223.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df223 = df223.sort_values(by=['预警时间'])
 ax = df223.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df223.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df223['Opening Time Count']))), math.ceil(max(list(df223['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top5 +' '+ 'Opening Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 6 No. of Opening Time Trend (Potentially Problematic) --> df224
try:
 top6 = df218.iloc[5]['Source']
 t6_speed= df218.iloc[5]['Opening Speed']
 df224 = df56.copy()
 df224['车厢'] = df224['车厢'].astype(str).str.zfill(2)
 df224['Source'] = df224['车组']+ '_' + df224['车厢'] + '_' + df224['Opening DCU']
 df224 = df224.loc[(df224['Source'] == top6) & (df224['Opening Speed'] == t6_speed)]
 df224['预警时间'] = df224['预警时间'].str.slice(0,10)
 df224= pd.DataFrame(df224.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df224 = df224.sort_values(by=['预警时间'])
 ax = df224.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df224.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df224['Opening Time Count']))), math.ceil(max(list(df224['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top6 +' '+ 'Opening Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 7 No. of Opening Time Trend (Potentially Problematic) --> df225
try:
 top7 = df218.iloc[6]['Source']
 t7_speed= df218.iloc[6]['Opening Speed']
 df225 = df56.copy()
 df225['车厢'] = df225['车厢'].astype(str).str.zfill(2)
 df225['Source'] = df225['车组']+ '_' + df225['车厢'] + '_' + df225['Opening DCU']
 df225 = df225.loc[(df225['Source'] == top7) & (df225['Opening Speed'] == t7_speed)]
 df225['预警时间'] = df225['预警时间'].str.slice(0,10)
 df225= pd.DataFrame(df225.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df225 = df225.sort_values(by=['预警时间'])
 ax = df225.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df225.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df225['Opening Time Count']))), math.ceil(max(list(df225['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top7 +' '+ 'Opening Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 8 No. of Opening Time Trend (Potentially Problematic) --> df226
try:
 top8 = df218.iloc[7]['Source']
 t8_speed= df218.iloc[7]['Opening Speed']
 df226 = df56.copy()
 df226['车厢'] = df226['车厢'].astype(str).str.zfill(2)
 df226['Source'] = df226['车组']+ '_' + df226['车厢'] + '_' + df226['Opening DCU']
 df226 = df226.loc[(df226['Source'] == top8) & (df226['Opening Speed'] == t8_speed)]
 df226['预警时间'] = df226['预警时间'].str.slice(0,10)
 df226= pd.DataFrame(df226.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df226 = df226.sort_values(by=['预警时间'])
 ax = df226.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df226.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df226['Opening Time Count']))), math.ceil(max(list(df226['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top8 +' '+ 'Opening Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 9 No. of Opening Time Trend (Potentially Problematic) --> df227
try:
 top9 = df218.iloc[8]['Source']
 t9_speed= df218.iloc[8]['Opening Speed']
 df227 = df56.copy()
 df227['车厢'] = df227['车厢'].astype(str).str.zfill(2)
 df227['Source'] = df227['车组']+ '_' + df227['车厢'] + '_' + df227['Opening DCU']
 df227 = df227.loc[(df227['Source'] == top9) & (df227['Opening Speed'] == t9_speed)]
 df227['预警时间'] = df227['预警时间'].str.slice(0,10)
 df227= pd.DataFrame(df227.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df227 = df227.sort_values(by=['预警时间'])
 ax = df227.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df227.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df227['Opening Time Count']))), math.ceil(max(list(df227['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top9 +' '+ 'Opening Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Top 10 No. of Opening Time Trend (Potentially Problematic) --> df228
try:
 top10 = df218.iloc[9]['Source']
 t10_speed= df218.iloc[9]['Opening Speed']
 df228 = df56.copy()
 df228['车厢'] = df228['车厢'].astype(str).str.zfill(2)
 df228['Source'] = df228['车组']+ '_' + df228['车厢'] + '_' + df228['Opening DCU']
 df228 = df228.loc[(df228['Source'] == top10) & (df228['Opening Speed'] == t10_speed)]
 df228['预警时间'] = df228['预警时间'].str.slice(0,10)
 df228= pd.DataFrame(df228.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df228 = df228.sort_values(by=['预警时间'])
 ax = df228.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df228.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df228['Opening Time Count']))), math.ceil(max(list(df228['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top10 +' '+ 'Opening Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Potentially_Problematic\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Opening Time Trend (Potentially Problematic)')
    plt.close()


# Believed to be Abnormal Cases (Opening Time)  --> df229
df229 = df56.copy()
df229 = df229[(df229['Opening Speed'] >=8)]


# Top Ten DCU Opening Time Excel File (Abnormal) --> df230
df230 = df229.copy()
df230['车厢'] = df230['车厢'].astype(str).str.zfill(2)
df230['Source'] = df230['车组']+ '_' + df230['车厢'] + '_' + df230['Opening DCU']
df230['预警时间'] = df230['预警时间'].str.slice(0,10)
df230 = pd.DataFrame(df230.groupby(['Source','Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
df230 = df230.reindex(columns=['Source','Opening Speed','Opening Time Count'])
df230 = df230.sort_values(by=['Opening Speed'])


# Top Ten DCU Opening Time Graph (Abnormal) --> df231
try:
    df231 = df230.nlargest(n = 10 , columns =['Opening Time Count'])
    df231 = df231.sort_values(by=['Opening Time Count'],ignore_index = True, ascending = False)
    df231.plot.barh(x = 'Source', y= 'Opening Time Count',figsize = (12,12))
    new_list = range(math.floor(min(list(df231['Opening Time Count']))), math.ceil(max(list(df231['Opening Time Count']))+1))
    plt.xticks(new_list)
    plt.title('Top Ten Opening Time DCU (Abnoraml)')
    plt.xlabel('Count')
    plt.ylabel('Opening Time DCU')
    #plt.savefig(fr'C:/Users/{user}/Downloads/location/Opening_Closing_Time/Top_ten/Opening_Time/Abnormal/Top_Ten_Opening_Time_DCU (Abnormal).png')
    plt.close()
    
except:
    print('No Top Ten Opening Time Result (Abnormal)')
    plt.close()


# Top 1 No. of Opening Time Trend (Abnormal) --> df232
try:
 top1 = df231.iloc[0]['Source']
 t1_speed= df231.iloc[0]['Opening Speed']
 df232 = df56.copy()
 df232['车厢'] = df232['车厢'].astype(str).str.zfill(2)
 df232['Source'] = df232['车组']+ '_' + df232['车厢'] + '_' + df232['Opening DCU']
 df232 = df232.loc[(df232['Source'] == top1) & (df232['Opening Speed'] == t1_speed)]
 df232['预警时间'] = df232['预警时间'].str.slice(0,10)
 df232= pd.DataFrame(df232.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df232 = df232.sort_values(by=['预警时间'])
 ax = df232.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df232.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df232['Opening Time Count']))), math.ceil(max(list(df232['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top1 +' '+ 'Opening Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Opening Time Trend (Abnormal)')
    plt.close()


# Top 2 No. of Opening Time Trend (Abnormal) --> df233
try:
 top2 = df231.iloc[1]['Source']
 t2_speed= df231.iloc[1]['Opening Speed']
 df233 = df56.copy()
 df233['车厢'] = df233['车厢'].astype(str).str.zfill(2)
 df233['Source'] = df233['车组']+ '_' + df233['车厢'] + '_' + df233['Opening DCU']
 df233 = df233.loc[(df233['Source'] == top2) & (df233['Opening Speed'] == t2_speed)]
 df233['预警时间'] = df233['预警时间'].str.slice(0,10)
 df233= pd.DataFrame(df233.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df233 = df233.sort_values(by=['预警时间'])
 ax = df233.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df233.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df233['Opening Time Count']))), math.ceil(max(list(df233['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top2 +' '+ 'Opening Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Opening Time Trend (Abnormal)')
    plt.close()


# Top 3 No. of Opening Time Trend (Abnormal) --> df234
try:
 top3 = df231.iloc[2]['Source']
 t3_speed= df231.iloc[2]['Opening Speed']
 df234 = df56.copy()
 df234['车厢'] = df234['车厢'].astype(str).str.zfill(2)
 df234['Source'] = df234['车组']+ '_' + df234['车厢'] + '_' + df234['Opening DCU']
 df234 = df234.loc[(df234['Source'] == top3) & (df234['Opening Speed'] == t3_speed)]
 df234['预警时间'] = df234['预警时间'].str.slice(0,10)
 df234= pd.DataFrame(df234.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df234 = df234.sort_values(by=['预警时间'])
 ax = df234.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df234.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df234['Opening Time Count']))), math.ceil(max(list(df234['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top3 +' '+ 'Opening Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Opening Time Trend (Abnormal)')
    plt.close()


# Top 4 No. of Opening Time Trend (Abnormal) --> df235
try:
 top4 = df231.iloc[3]['Source']
 t4_speed= df231.iloc[3]['Opening Speed']
 df235 = df56.copy()
 df235['车厢'] = df235['车厢'].astype(str).str.zfill(2)
 df235['Source'] = df235['车组']+ '_' + df235['车厢'] + '_' + df235['Opening DCU']
 df235 = df235.loc[(df235['Source'] == top4) & (df235['Opening Speed'] == t4_speed)]
 df235['预警时间'] = df235['预警时间'].str.slice(0,10)
 df235= pd.DataFrame(df235.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df235 = df235.sort_values(by=['预警时间'])
 ax = df235.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df235.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df235['Opening Time Count']))), math.ceil(max(list(df235['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top4 +' '+ 'Opening Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Opening Time Trend (Abnormal)')
    plt.close()


# Top 5 No. of Opening Time Trend (Abnormal) --> df236
try:
 top5 = df231.iloc[4]['Source']
 t5_speed= df231.iloc[4]['Opening Speed']
 df236 = df56.copy()
 df236['车厢'] = df236['车厢'].astype(str).str.zfill(2)
 df236['Source'] = df236['车组']+ '_' + df236['车厢'] + '_' + df236['Opening DCU']
 df236 = df236.loc[(df236['Source'] == top5) & (df236['Opening Speed'] == t5_speed)]
 df236['预警时间'] = df236['预警时间'].str.slice(0,10)
 df236= pd.DataFrame(df236.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df236 = df236.sort_values(by=['预警时间'])
 ax = df236.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df236.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df236['Opening Time Count']))), math.ceil(max(list(df236['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top5 +' '+ 'Opening Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Opening Time Trend (Abnormal)')
    plt.close()


# Top 6 No. of Opening Time Trend (Abnormal) --> df237
try:
 top6 = df231.iloc[5]['Source']
 t6_speed= df231.iloc[5]['Opening Speed']
 df237 = df56.copy()
 df237['车厢'] = df237['车厢'].astype(str).str.zfill(2)
 df237['Source'] = df237['车组']+ '_' + df237['车厢'] + '_' + df237['Opening DCU']
 df237 = df237.loc[(df237['Source'] == top6) & (df237['Opening Speed'] == t6_speed)]
 df237['预警时间'] = df237['预警时间'].str.slice(0,10)
 df237= pd.DataFrame(df237.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df237 = df237.sort_values(by=['预警时间'])
 ax = df237.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df237.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df237['Opening Time Count']))), math.ceil(max(list(df237['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top6 +' '+ 'Opening Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Opening Time Trend (Abnormal)')
    plt.close()


# Top 7 No. of Opening Time Trend (Abnormal) --> df238
try:
 top7 = df231.iloc[6]['Source']
 t7_speed= df231.iloc[6]['Opening Speed']
 df238 = df56.copy()
 df238['车厢'] = df238['车厢'].astype(str).str.zfill(2)
 df238['Source'] = df238['车组']+ '_' + df238['车厢'] + '_' + df238['Opening DCU']
 df238 = df238.loc[(df238['Source'] == top7) & (df238['Opening Speed'] == t7_speed)]
 df238['预警时间'] = df238['预警时间'].str.slice(0,10)
 df238= pd.DataFrame(df238.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df238 = df238.sort_values(by=['预警时间'])
 ax = df238.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df238.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df238['Opening Time Count']))), math.ceil(max(list(df238['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top7 +' '+ 'Opening Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Opening Time Trend (Abnormal)')
    plt.close()


# Top 8 No. of Opening Time Trend (Abnormal) --> df239
try:
 top8 = df231.iloc[7]['Source']
 t8_speed= df231.iloc[7]['Opening Speed']
 df239 = df56.copy()
 df239['车厢'] = df239['车厢'].astype(str).str.zfill(2)
 df239['Source'] = df239['车组']+ '_' + df239['车厢'] + '_' + df239['Opening DCU']
 df239 = df239.loc[(df239['Source'] == top8) & (df239['Opening Speed'] == t8_speed)]
 df239['预警时间'] = df239['预警时间'].str.slice(0,10)
 df239= pd.DataFrame(df239.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df239 = df239.sort_values(by=['预警时间'])
 ax = df239.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df239.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df239['Opening Time Count']))), math.ceil(max(list(df239['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top8 +' '+ 'Opening Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Opening Time Trend (Abnormal)')
    plt.close()


# Top 9 No. of Opening Time Trend (Abnormal) --> df240
try:
 top9 = df231.iloc[8]['Source']
 t9_speed= df231.iloc[8]['Opening Speed']
 df240 = df56.copy()
 df240['车厢'] = df240['车厢'].astype(str).str.zfill(2)
 df240['Source'] = df240['车组']+ '_' + df240['车厢'] + '_' + df240['Opening DCU']
 df240 = df240.loc[(df240['Source'] == top9) & (df240['Opening Speed'] == t9_speed)]
 df240['预警时间'] = df240['预警时间'].str.slice(0,10)
 df240= pd.DataFrame(df240.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df240 = df240.sort_values(by=['预警时间'])
 ax = df240.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df240.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df240['Opening Time Count']))), math.ceil(max(list(df240['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top9 +' '+ 'Opening Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Opening Time Trend (Abnormal)')
    plt.close()


# Top 10 No. of Opening Time Trend (Abnormal) --> df241
try:
 top10 = df231.iloc[9]['Source']
 t10_speed= df231.iloc[9]['Opening Speed']
 df241 = df56.copy()
 df241['车厢'] = df241['车厢'].astype(str).str.zfill(2)
 df241['Source'] = df241['车组']+ '_' + df241['车厢'] + '_' + df241['Opening DCU']
 df241 = df241.loc[(df241['Source'] == top10) & (df241['Opening Speed'] == t10_speed)]
 df241['预警时间'] = df241['预警时间'].str.slice(0,10)
 df241= pd.DataFrame(df241.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df241 = df241.sort_values(by=['预警时间'])
 ax = df241.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df241.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 new_list = range(math.floor(min(list(df241['Opening Time Count']))), math.ceil(max(list(df241['Opening Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top10 +' '+ 'Opening Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Abnormal\Trends\{}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Opening Time Trend (Abnormal)')
    plt.close()


# Believed to be Zero Cases  --> df140
df140 = df56.copy()
df140 = df140.drop(df140[df140['Opening Speed'] > 3.7].index, axis = 'rows')


# Top Ten DCU Opening Time Excel File (Zero)  --> df141
df141 = df140.copy()
df141['车厢'] = df141['车厢'].astype(str).str.zfill(2)
df141['Source'] = df141['车组']+ '_' + df141['车厢'] + '_' + df141['Opening DCU']
df141['预警时间'] = df141['预警时间'].str.slice(0,10)
df141 = pd.DataFrame(df141.groupby(['Source','Opening Speed']).size(),columns=['Opening Time Count']).reset_index()
df141 = df141.reindex(columns=['Source','Opening Speed','Opening Time Count'])


#Top Ten DCU Opening Time Graph (Zero) --> df142
try:   
 df142 = df141.nlargest(n = 10 , columns =['Opening Time Count'])
 df142 = df142.sort_values(by='Opening Time Count',ignore_index = True, ascending = False)
 df142.plot.barh(x = 'Source', y= 'Opening Time Count',figsize = (12,12))
 plt.title('Top Ten Opening Time DCU (Zero)')
 plt.xlabel('Count')
 plt.ylabel('Opening Time DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Top_Ten_Opening_Time_DCU (Zero).png')
 plt.close()
except:
    print('No Top Ten Opening Time Result (Zero)')
    plt.close()


# Top 1 No. of Opening Time Trend (Zero) --> df143
try:
 top1 = df142.iloc[0]['Source']
 t1_speed= df142.iloc[0]['Opening Speed']
 df143 = df56.copy()
 df143['车厢'] = df143['车厢'].astype(str).str.zfill(2)
 df143['Source'] = df143['车组']+ '_' + df143['车厢'] + '_' + df143['Opening DCU']
 df143 = df143.loc[(df143['Source'] == top1) & (df143['Opening Speed'] == t1_speed)]
 df143['预警时间'] = df143['预警时间'].str.slice(0,10)
 df143= pd.DataFrame(df143.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df143 = df143.sort_values(by=['预警时间'])
 ax = df143.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df143.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top1 +' '+ 'Opening Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Opening Time Trend (Zero)')
    plt.close()


# Top 2 No. of Opening Time Trend (Zero) --> df144
try:
 top2 = df142.iloc[1]['Source']
 t2_speed= df142.iloc[1]['Opening Speed']
 df144 = df56.copy()
 df144['车厢'] = df144['车厢'].astype(str).str.zfill(2)
 df144['Source'] = df144['车组']+ '_' + df144['车厢'] + '_' + df144['Opening DCU']
 df144 = df144.loc[(df144['Source'] == top2) & (df144['Opening Speed'] == t2_speed)]
 df144['预警时间'] = df144['预警时间'].str.slice(0,10)
 df144= pd.DataFrame(df144.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df144 = df144.sort_values(by=['预警时间'])
 ax = df144.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df144.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top2 +' '+ 'Opening Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Opening Time Trend (Zero)')
    plt.close()


# Top 3 No. of Opening Time Trend (Zero) --> df145
try:
 top3 = df142.iloc[2]['Source']
 t3_speed= df142.iloc[2]['Opening Speed']
 df145 = df56.copy()
 df145['车厢'] = df145['车厢'].astype(str).str.zfill(2)
 df145['Source'] = df145['车组']+ '_' + df145['车厢'] + '_' + df145['Opening DCU']
 df145 = df145.loc[(df145['Source'] == top3) & (df145['Opening Speed'] == t3_speed)]
 df145['预警时间'] = df145['预警时间'].str.slice(0,10)
 df145= pd.DataFrame(df145.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df145 = df145.sort_values(by=['预警时间'])
 ax = df145.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df145.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top3 +' '+ 'Opening Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Opening Time Trend (Zero)')
    plt.close()


#Top 4 No. of Opening Time Trend (Zero) --> df146
try:
 top4 = df142.iloc[3]['Source']
 t4_speed= df142.iloc[3]['Opening Speed']
 df146 = df56.copy()
 df146['车厢'] = df146['车厢'].astype(str).str.zfill(2)
 df146['Source'] = df146['车组']+ '_' + df146['车厢'] + '_' + df146['Opening DCU']
 df146 = df146.loc[(df146['Source'] == top4) & (df146['Opening Speed'] == t4_speed)]
 df146['预警时间'] = df146['预警时间'].str.slice(0,10)
 df146= pd.DataFrame(df146.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df146 = df146.sort_values(by=['预警时间'])
 ax = df146.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df146.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top4 +' '+ 'Opening Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Opening Time Trend (Zero)')
    plt.close()


#Top 5 No. of Opening Time Trend (Zero) --> df147
try:
 top5 = df142.iloc[4]['Source']
 t5_speed= df142.iloc[4]['Opening Speed']
 df147 = df56.copy()
 df147['车厢'] = df147['车厢'].astype(str).str.zfill(2)
 df147['Source'] = df147['车组']+ '_' + df147['车厢'] + '_' + df147['Opening DCU']
 df147 = df147.loc[(df147['Source'] == top5) & (df147['Opening Speed'] == t5_speed)]
 df147['预警时间'] = df147['预警时间'].str.slice(0,10)
 df147= pd.DataFrame(df147.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df147 = df147.sort_values(by=['预警时间'])
 ax = df147.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df147.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top5 +' '+ 'Opening Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Opening Time Trend (Zero)')
    plt.close()


#Top 6 No. of Opening Time Trend (Zero) --> df148
try:
 top6 = df142.iloc[5]['Source']
 t6_speed= df142.iloc[5]['Opening Speed']
 df148 = df56.copy()
 df148['车厢'] = df148['车厢'].astype(str).str.zfill(2)
 df148['Source'] = df148['车组']+ '_' + df148['车厢'] + '_' + df148['Opening DCU']
 df148 = df148.loc[(df148['Source'] == top6) & (df148['Opening Speed'] == t6_speed)]
 df148['预警时间'] = df148['预警时间'].str.slice(0,10)
 df148= pd.DataFrame(df148.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df148 = df148.sort_values(by=['预警时间'])
 ax = df148.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df148.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top6 +' '+ 'Opening Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Opening Time Trend (Zero)')
    plt.close()


#Top 7 No. of Opening Time Trend (Zero) --> df149
try:
 top7 = df142.iloc[6]['Source']
 t7_speed= df142.iloc[6]['Opening Speed']
 df149 = df56.copy()
 df149['车厢'] = df149['车厢'].astype(str).str.zfill(2)
 df149['Source'] = df149['车组']+ '_' + df149['车厢'] + '_' + df149['Opening DCU']
 df149 = df149.loc[(df149['Source'] == top7) & (df149['Opening Speed'] == t7_speed)]
 df149['预警时间'] = df149['预警时间'].str.slice(0,10)
 df149= pd.DataFrame(df149.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df149 = df149.sort_values(by=['预警时间'])
 ax = df149.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df149.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top7 +' '+ 'Opening Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Opening Time Trend (Zero)')
    plt.close()


#Top 8 No. of Opening Time Trend (Zero) --> df150
try:
 top8 = df142.iloc[7]['Source']
 t8_speed= df142.iloc[7]['Opening Speed']
 df150 = df56.copy()
 df150['车厢'] = df150['车厢'].astype(str).str.zfill(2)
 df150['Source'] = df150['车组']+ '_' + df150['车厢'] + '_' + df150['Opening DCU']
 df150 = df150.loc[(df150['Source'] == top8) & (df150['Opening Speed'] == t8_speed)]
 df150['预警时间'] = df150['预警时间'].str.slice(0,10)
 df150= pd.DataFrame(df150.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df150 = df150.sort_values(by=['预警时间'])
 ax = df150.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df150.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top8 +' '+ 'Opening Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Opening Time Trend (Zero)')
    plt.close()


#Top 9 No. of Opening Time Trend (Zero) --> df151
try:
 top9 = df142.iloc[8]['Source']
 t9_speed= df142.iloc[8]['Opening Speed']
 df151 = df56.copy()
 df151['车厢'] = df151['车厢'].astype(str).str.zfill(2)
 df151['Source'] = df151['车组']+ '_' + df151['车厢'] + '_' + df151['Opening DCU']
 df151 = df151.loc[(df151['Source'] == top9) & (df151['Opening Speed'] == t9_speed)]
 df151['预警时间'] = df151['预警时间'].str.slice(0,10)
 df151= pd.DataFrame(df151.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df151 = df151.sort_values(by=['预警时间'])
 ax = df151.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df151.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top9 +' '+ 'Opening Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Opening Time Trend (Zero)')
    plt.close()


#Top 10 No. of Opening Time Trend (Zero) --> df152
try:
 top10 = df142.iloc[9]['Source']
 t10_speed= df142.iloc[9]['Opening Speed']
 df152 = df56.copy()
 df152['车厢'] = df152['车厢'].astype(str).str.zfill(2)
 df152['Source'] = df152['车组']+ '_' + df152['车厢'] + '_' + df152['Opening DCU']
 df152 = df152.loc[(df152['Source'] == top10) & (df152['Opening Speed'] == t10_speed)]
 df152['预警时间'] = df152['预警时间'].str.slice(0,10)
 df152= pd.DataFrame(df152.groupby(['Source' ,'预警时间']).size(),columns=['Opening Time Count']).reset_index()
 df152 = df152.sort_values(by=['预警时间'])
 ax = df152.plot.scatter(x= '预警时间', y= 'Opening Time Count', style='b',figsize = (12,12))
 df152.plot.line(x= '预警时间', y='Opening Time Count', ax=ax, style='b',rot=25, grid= True)
 plt.title(top10 +' '+ 'Opening Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Opening_Time\Zero\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Opening Time Trend (Zero)')
    plt.close()


# Opening Time Group Count with a particular range (3.8-3.9) -->  df270
try:
    df270 = df56.copy()
    df270 = df270[(df270['Opening Speed'] >= 3.8) & (df270['Opening Speed'] <= 3.9 )]
    df270['车厢'] = df270['车厢'].astype('str')
    df270['Source'] = df270['车组'] + '_' + df270['车厢'] + '_' + df270['Opening DCU']
    df270 = pd.DataFrame(df270.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df270['sort1'] = df270['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df270['sort2'] = df270['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df270['sort3'] = df270['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df270['sort1'] = df270['sort1'].astype("int")
    df270['sort2'] = df270['sort2'].astype("int")
    df270['sort3'] = df270['sort3'].astype("int")
    df270 = df270.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    #df270 = df270.sort_values(by = 'Range Count', ascending = False)
    df270.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Opening Time Range Count (3.8-3.9)')
    plt.xlabel('Count')
    plt.ylabel('Opening Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Range_Count\Opening_Time_Range_Count(3.8-3.9).png')
    plt.close()
    
except:
    print('No Opening Time Range Count (3.8-3.9) Graph')
    plt.close()


# Opening Time Group Count with a particular range (4.0-4.9) -->  df271
try:
    df271 = df56.copy()
    df271 = df271[(df271['Opening Speed'] >= 4.0) & (df271['Opening Speed'] <= 4.9 )]
    df271['车厢'] = df271['车厢'].astype('str')
    df271['Source'] = df271['车组'] + '_' + df271['车厢'] + '_' + df271['Opening DCU']
    df271 = pd.DataFrame(df271.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df271['sort1'] = df271['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df271['sort2'] = df271['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df271['sort3'] = df271['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df271['sort1'] = df271['sort1'].astype("int")
    df271['sort2'] = df271['sort2'].astype("int")
    df271['sort3'] = df271['sort3'].astype("int")
    df271 = df271.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df271.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Opening Time Range Count (4.0-4.9)')
    plt.xlabel('Count')
    plt.ylabel('Opening Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Range_Count\Opening_Time_Range_Count(4.0-4.9).png')
    plt.close()
    
except:
    print('No Opening Time Range Count (4.0-4.9) Graph')
    plt.close()



# Opening Time Group Count with a particular range (5.0-9.9) -->  df272
try:
    df272 = df56.copy()
    df272 = df272[(df272['Opening Speed'] >= 5.0) & (df272['Opening Speed'] <= 9.9 )]
    df272['车厢'] = df272['车厢'].astype('str')
    df272['Source'] = df272['车组'] + '_' + df272['车厢'] + '_' + df272['Opening DCU']
    df272 = pd.DataFrame(df272.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df272['sort1'] = df272['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df272['sort2'] = df272['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df272['sort3'] = df272['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df272['sort1'] = df272['sort1'].astype("int")
    df272['sort2'] = df272['sort2'].astype("int")
    df272['sort3'] = df272['sort3'].astype("int")
    df272 = df272.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df272.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Opening Time Range Count (5.0-9.9)')
    plt.xlabel('Count')
    plt.ylabel('Opening Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Range_Count\Opening_Time_Range_Count(5.0-9.9).png')
    plt.close()
    
except:
    print('No Opening Time Range Count (5.0-9.9) Graph')
    plt.close()



# Opening Time Group Count with a particular range (>9.9) -->  df273
try:
    df273 = df56.copy()
    df273 = df273[(df273['Opening Speed'] > 9.9)]
    df273['车厢'] = df273['车厢'].astype('str')
    df273['Source'] = df273['车组'] + '_' + df273['车厢'] + '_' + df273['Opening DCU']
    df273 = pd.DataFrame(df273.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df273['sort1'] = df273['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df273['sort2'] = df273['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df273['sort3'] = df273['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df273['sort1'] = df273['sort1'].astype("int")
    df273['sort2'] = df273['sort2'].astype("int")
    df273['sort3'] = df273['sort3'].astype("int")
    df273 = df273.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df273.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Opening Time Range Count (>9.9)')
    plt.xlabel('Count')
    plt.ylabel('Opening Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Opening_Time\Range_Count\Opening_Time_Range_Count(9.9...).png')
    plt.close()
    
except:
    print('No Opening Time Range Count (>9.9) Graph')
    plt.close()


# Believed to be Normal Cases (Closing Time) --> df153
df153 = df57.copy()
df153 = df153[(df153['Closing Speed'] >3) & (df153['Closing Speed'] <= 4 )]


# Top Ten DCU Closing Time Excel File (Normal)--> df116 
df116 = df153.copy()
df116['车厢'] = df116['车厢'].astype(str).str.zfill(2)
df116['Source'] = df116['车组']+ '_' + df116['车厢'] + '_' + df116['Closing DCU']
df116['预警时间'] = df116['预警时间'].str.slice(0,10)
df116 = pd.DataFrame(df116.groupby(['Source','Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
df116 = df116.reindex(columns=['Source','Closing Speed','Closing Time Count'])
df116 = df116.sort_values(by='Closing Speed')


# Top Ten DCU Closing Time Graph (Normal) --> df117
try: 
    df117 = df116.nlargest(n = 10 , columns =['Closing Time Count'])
    df117 = df117.sort_values(by='Closing Time Count',ignore_index = True, ascending = False)
    colors = {3.6: 'r' , 3.7: 'g', 3.8: 'b',3.9: '#F700FF',4: '#FF9100'}
    colos = list(df117['Closing Speed'].map(colors)) 
    df117.plot.barh(x = 'Source', y= 'Closing Time Count', color= colos,figsize = (12,12))
    new_list = range(math.floor(min(list(df117['Closing Time Count']))), math.ceil(max(list(df117['Closing Time Count']))+1))
    plt.xticks(new_list)
    plt.title('Top Ten Closing Time DCU (Normal)')
    plt.legend(['3.6: Red \n3.7: Green\n3.8: Blue\n3.9: Pink\n4: Orange'],loc='best',edgecolor = 'black',prop = {'size':15})
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Top_Ten_Closing_Time_DCU (Normal).png')
    plt.close()
except:
    print('No Top Ten Closing Time Result (Normal)')
    plt.close()


#Top 1 No. of Closing Time Trend (Normal) --> df128

try:
 top1 = df117.iloc[0]['Source']
 t1_speed= df117.iloc[0]['Closing Speed']
 df128 = df57.copy()
 df128['车厢'] = df128['车厢'].astype(str).str.zfill(2)
 df128['Source'] = df128['车组']+ '_' + df128['车厢'] + '_' + df128['Closing DCU']
 df128 = df128.loc[(df128['Source'] == top1) & (df128['Closing Speed'] == t1_speed)]
 df128['预警时间'] = df128['预警时间'].str.slice(0,10)
 df128= pd.DataFrame(df128.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df128 = df128.sort_values(by=['预警时间'])
 ax = df128.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df128.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df128['Closing Time Count']))), math.ceil(max(list(df128['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top1 +' '+ 'Closing Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Closing Time Trend (Normal)')
    plt.close()


#Top 2 No. of Closing Time Trend (Normal) --> df129

try:
 top2 = df117.iloc[1]['Source']
 t2_speed= df117.iloc[1]['Closing Speed']
 df129 = df57.copy()
 df129['车厢'] = df129['车厢'].astype(str).str.zfill(2)
 df129['Source'] = df129['车组']+ '_' + df129['车厢'] + '_' + df129['Closing DCU']
 df129 = df129.loc[(df129['Source'] == top2) & (df129['Closing Speed'] == t2_speed)]
 df129['预警时间'] = df129['预警时间'].str.slice(0,10)
 df129= pd.DataFrame(df129.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df129 = df129.sort_values(by=['预警时间'])
 ax = df129.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df129.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df129['Closing Time Count']))), math.ceil(max(list(df129['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top2 +' '+ 'Closing Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Closing Time Trend (Normal)')
    plt.close()


#Top 3 No. of Closing Time Trend (Normal) --> df130

try:
 top3 = df117.iloc[2]['Source']
 t3_speed= df117.iloc[2]['Closing Speed']
 df130 = df57.copy()
 df130['车厢'] = df130['车厢'].astype(str).str.zfill(2)
 df130['Source'] = df130['车组']+ '_' + df130['车厢'] + '_' + df130['Closing DCU']
 df130 = df130.loc[(df130['Source'] == top3) & (df130['Closing Speed'] == t3_speed)]
 df130['预警时间'] = df130['预警时间'].str.slice(0,10)
 df130= pd.DataFrame(df130.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df130 = df130.sort_values(by=['预警时间'])
 ax = df130.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df130.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df130['Closing Time Count']))), math.ceil(max(list(df130['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top3 +' '+ 'Closing Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Closing Time Trend (Normal)')
    plt.close()


#Top 4 No. of Closing Time Trend (Normal) --> df131

try:
 top4 = df117.iloc[3]['Source']
 t4_speed= df117.iloc[3]['Closing Speed']
 df131 = df57.copy()
 df131['车厢'] = df131['车厢'].astype(str).str.zfill(2)
 df131['Source'] = df131['车组']+ '_' + df131['车厢'] + '_' + df131['Closing DCU']
 df131 = df131.loc[(df131['Source'] == top4) & (df131['Closing Speed'] == t4_speed)]
 df131['预警时间'] = df131['预警时间'].str.slice(0,10)
 df131= pd.DataFrame(df131.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df131 = df131.sort_values(by=['预警时间'])
 ax = df131.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df131.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df131['Closing Time Count']))), math.ceil(max(list(df131['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top4 +' '+ 'Closing Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Closing Time Trend (Normal)')
    plt.close()


#Top 5 No. of Closing Time Trend (Normal) --> df132

try:
 top5 = df117.iloc[4]['Source']
 t5_speed= df117.iloc[4]['Closing Speed']
 df132 = df57.copy()
 df132['车厢'] = df132['车厢'].astype(str).str.zfill(2)
 df132['Source'] = df132['车组']+ '_' + df132['车厢'] + '_' + df132['Closing DCU']
 df132 = df132.loc[(df132['Source'] == top5) & (df132['Closing Speed'] == t5_speed)]
 df132['预警时间'] = df132['预警时间'].str.slice(0,10)
 df132= pd.DataFrame(df132.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df132 = df132.sort_values(by=['预警时间'])
 ax = df132.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df132.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df132['Closing Time Count']))), math.ceil(max(list(df132['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top5 +' '+ 'Closing Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Closing Time Trend (Normal)')
    plt.close()


#Top 6 No. of Closing Time Trend (Normal) --> df133

try:
 top6 = df117.iloc[5]['Source']
 t6_speed= df117.iloc[5]['Closing Speed']
 df133 = df57.copy()
 df133['车厢'] = df133['车厢'].astype(str).str.zfill(2)
 df133['Source'] = df133['车组']+ '_' + df133['车厢'] + '_' + df133['Closing DCU']
 df133 = df133.loc[(df133['Source'] == top6) & (df133['Closing Speed'] == t6_speed)]
 df133['预警时间'] = df133['预警时间'].str.slice(0,10)
 df133= pd.DataFrame(df133.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df133 = df133.sort_values(by=['预警时间'])
 ax = df133.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df133.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df133['Closing Time Count']))), math.ceil(max(list(df133['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top6 +' '+ 'Closing Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Closing Time Trend (Normal)')
    plt.close()


#Top 7 No. of Closing Time Trend (Normal) --> df134

try:
 top7 = df117.iloc[6]['Source']
 t7_speed= df117.iloc[6]['Closing Speed']
 df134 = df57.copy()
 df134['车厢'] = df134['车厢'].astype(str).str.zfill(2)
 df134['Source'] = df134['车组']+ '_' + df134['车厢'] + '_' + df134['Closing DCU']
 df134 = df134.loc[(df134['Source'] == top7) & (df134['Closing Speed'] == t7_speed)]
 df134['预警时间'] = df134['预警时间'].str.slice(0,10)
 df134= pd.DataFrame(df134.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df134 = df134.sort_values(by=['预警时间'])
 ax = df134.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df134.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df134['Closing Time Count']))), math.ceil(max(list(df134['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top7 +' '+ 'Closing Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Closing Time Trend (Normal)')
    plt.close()


#Top 8 No. of Closing Time Trend (Normal) --> df135

try:
 top8 = df117.iloc[7]['Source']
 t8_speed= df117.iloc[7]['Closing Speed']
 df135 = df57.copy()
 df135['车厢'] = df135['车厢'].astype(str).str.zfill(2)
 df135['Source'] = df135['车组']+ '_' + df135['车厢'] + '_' + df135['Closing DCU']
 df135 = df135.loc[(df135['Source'] == top8) & (df135['Closing Speed'] == t8_speed)]
 df135['预警时间'] = df135['预警时间'].str.slice(0,10)
 df135= pd.DataFrame(df135.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df135 = df135.sort_values(by=['预警时间'])
 ax = df135.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df135.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df135['Closing Time Count']))), math.ceil(max(list(df135['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top8 +' '+ 'Closing Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Closing Time Trend (Normal)')
    plt.close()


#Top 9 No. of Closing Time Trend (Normal) --> df136

try:
 top9 = df117.iloc[8]['Source']
 t9_speed= df117.iloc[8]['Closing Speed']
 df136 = df57.copy()
 df136['车厢'] = df136['车厢'].astype(str).str.zfill(2)
 df136['Source'] = df136['车组']+ '_' + df136['车厢'] + '_' + df136['Closing DCU']
 df136 = df136.loc[(df136['Source'] == top9) & (df136['Closing Speed'] == t9_speed)]
 df136['预警时间'] = df136['预警时间'].str.slice(0,10)
 df136= pd.DataFrame(df136.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df136 = df136.sort_values(by=['预警时间'])
 ax = df136.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df136.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df136['Closing Time Count']))), math.ceil(max(list(df136['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top9 +' '+ 'Closing Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Closing Time Trend (Normal)')
    plt.close()


#Top 10 No. of Closing Time Trend (Normal) --> df137

try:
 top10 = df117.iloc[9]['Source']
 t10_speed= df117.iloc[9]['Closing Speed']
 df137 = df57.copy()
 df137['车厢'] = df137['车厢'].astype(str).str.zfill(2)
 df137['Source'] = df137['车组']+ '_' + df137['车厢'] + '_' + df137['Closing DCU']
 df137 = df137.loc[(df137['Source'] == top10) & (df137['Closing Speed'] == t10_speed)]
 df137['预警时间'] = df137['预警时间'].str.slice(0,10)
 df137= pd.DataFrame(df137.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df137 = df137.sort_values(by=['预警时间'])
 ax = df137.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df137.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 new_list = range(math.floor(min(list(df137['Closing Time Count']))), math.ceil(max(list(df137['Closing Time Count']))+1))
 plt.yticks(new_list)
 plt.title(top10 +' '+ 'Closing Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Believed_To_Be_Normal\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Closing Time Trend (Normal)')
    plt.close()


# Believed to be Potentially Problematic Cases (Closing Time) --> df244
df244 = df57.copy()
df244 = df244[(df244['Closing Speed'] > 4) & (df244['Closing Speed'] < 8 )]


# Top Ten DCU Closing Time Excel File (Potentially Problematic) --> df245
df245 = df244.copy()
df245['车厢'] = df245['车厢'].astype(str).str.zfill(2)
df245['Source'] = df245['车组']+ '_' + df245['车厢'] + '_' + df245['Closing DCU']
df245['预警时间'] = df245['预警时间'].str.slice(0,10)
df245 = pd.DataFrame(df245.groupby(['Source','Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
df245 = df245.reindex(columns=['Source','Closing Speed','Closing Time Count'])
df245 = df245.sort_values(by = 'Closing Speed')


#Top Ten DCU Closing Time Graph (Potentially Problematic) --> df246
try:   
    df246 = df245.nlargest(n = 10 , columns =['Closing Time Count'])
    df246 = df246.sort_values(by='Closing Time Count',ignore_index = True, ascending = False)
    df246.plot.barh(x = 'Source', y= 'Closing Time Count',figsize = (12,12))
    plt.title('Top Ten Closing Time DCU (Potentially Problematic)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Top_Ten_Closing_Time_DCU (Potentially_Problematic).png')
    plt.close()
except:
    print('No Top Ten Closing Time Result (Potentially_Problematic)')
    plt.close()


# Top 1 No. of Closing Time Trend (Potentially_Problematic) --> df247
try:
 top1 = df246.iloc[0]['Source']
 t1_speed= df246.iloc[0]['Closing Speed']
 df247 = df57.copy()
 df247['车厢'] = df247['车厢'].astype(str).str.zfill(2)
 df247['Source'] = df247['车组']+ '_' + df247['车厢'] + '_' + df247['Closing DCU']
 df247 = df247.loc[(df247['Source'] == top1) & (df247['Closing Speed'] == t1_speed)]
 df247['预警时间'] = df247['预警时间'].str.slice(0,10)
 df247 = pd.DataFrame(df247.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df247 = df247.sort_values(by=['预警时间'])
 ax = df247.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df247.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top1 +' '+ 'Closing Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 2 No. of Closing Time Trend (Potentially_Problematic) --> df248
try:
 top2 = df246.iloc[1]['Source']
 t2_speed= df246.iloc[1]['Closing Speed']
 df248 = df57.copy()
 df248['车厢'] = df248['车厢'].astype(str).str.zfill(2)
 df248['Source'] = df248['车组']+ '_' + df248['车厢'] + '_' + df248['Closing DCU']
 df248 = df248.loc[(df248['Source'] == top2) & (df248['Closing Speed'] == t2_speed)]
 df248['预警时间'] = df248['预警时间'].str.slice(0,10)
 df248 = pd.DataFrame(df248.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df248 = df248.sort_values(by=['预警时间'])
 ax = df248.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df248.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top2 +' '+ 'Closing Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 3 No. of Closing Time Trend (Potentially_Problematic) --> df249
try:
 top3 = df246.iloc[2]['Source']
 t3_speed= df246.iloc[2]['Closing Speed']
 df249 = df57.copy()
 df249['车厢'] = df249['车厢'].astype(str).str.zfill(2)
 df249['Source'] = df249['车组']+ '_' + df249['车厢'] + '_' + df249['Closing DCU']
 df249 = df249.loc[(df249['Source'] == top3) & (df249['Closing Speed'] == t3_speed)]
 df249['预警时间'] = df249['预警时间'].str.slice(0,10)
 df249 = pd.DataFrame(df249.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df249 = df249.sort_values(by=['预警时间'])
 ax = df249.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df249.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top3 +' '+ 'Closing Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 4 No. of Closing Time Trend (Potentially_Problematic) --> df250
try:
 top4 = df246.iloc[3]['Source']
 t4_speed= df246.iloc[3]['Closing Speed']
 df250 = df57.copy()
 df250['车厢'] = df250['车厢'].astype(str).str.zfill(2)
 df250['Source'] = df250['车组']+ '_' + df250['车厢'] + '_' + df250['Closing DCU']
 df250 = df250.loc[(df250['Source'] == top4) & (df250['Closing Speed'] == t4_speed)]
 df250['预警时间'] = df250['预警时间'].str.slice(0,10)
 df250 = pd.DataFrame(df250.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df250 = df250.sort_values(by=['预警时间'])
 ax = df250.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df250.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top4 +' '+ 'Closing Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 5 No. of Closing Time Trend (Potentially_Problematic) --> df251
try:
 top5 = df246.iloc[4]['Source']
 t5_speed= df246.iloc[4]['Closing Speed']
 df251 = df57.copy()
 df251['车厢'] = df251['车厢'].astype(str).str.zfill(2)
 df251['Source'] = df251['车组']+ '_' + df251['车厢'] + '_' + df251['Closing DCU']
 df251 = df251.loc[(df251['Source'] == top5) & (df251['Closing Speed'] == t5_speed)]
 df251['预警时间'] = df251['预警时间'].str.slice(0,10)
 df251 = pd.DataFrame(df251.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df251 = df251.sort_values(by=['预警时间'])
 ax = df251.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df251.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top5 +' '+ 'Closing Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 6 No. of Closing Time Trend (Potentially_Problematic) --> df252
try:
 top6 = df246.iloc[5]['Source']
 t6_speed= df246.iloc[5]['Closing Speed']
 df252 = df57.copy()
 df252['车厢'] = df252['车厢'].astype(str).str.zfill(2)
 df252['Source'] = df252['车组']+ '_' + df252['车厢'] + '_' + df252['Closing DCU']
 df252 = df252.loc[(df252['Source'] == top6) & (df252['Closing Speed'] == t6_speed)]
 df252['预警时间'] = df252['预警时间'].str.slice(0,10)
 df252 = pd.DataFrame(df252.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df252 = df252.sort_values(by=['预警时间'])
 ax = df252.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df252.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top6 +' '+ 'Closing Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 7 No. of Closing Time Trend (Potentially_Problematic) --> df253
try:
 top7 = df246.iloc[6]['Source']
 t7_speed= df246.iloc[6]['Closing Speed']
 df253 = df57.copy()
 df253['车厢'] = df253['车厢'].astype(str).str.zfill(2)
 df253['Source'] = df253['车组']+ '_' + df253['车厢'] + '_' + df253['Closing DCU']
 df253 = df253.loc[(df253['Source'] == top7) & (df253['Closing Speed'] == t7_speed)]
 df253['预警时间'] = df253['预警时间'].str.slice(0,10)
 df253 = pd.DataFrame(df253.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df253 = df253.sort_values(by=['预警时间'])
 ax = df253.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df253.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top7 +' '+ 'Closing Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 8 No. of Closing Time Trend (Potentially_Problematic) --> df254
try:
 top8 = df246.iloc[7]['Source']
 t8_speed= df246.iloc[7]['Closing Speed']
 df254 = df57.copy()
 df254['车厢'] = df254['车厢'].astype(str).str.zfill(2)
 df254['Source'] = df254['车组']+ '_' + df254['车厢'] + '_' + df254['Closing DCU']
 df254 = df254.loc[(df254['Source'] == top8) & (df254['Closing Speed'] == t8_speed)]
 df254['预警时间'] = df254['预警时间'].str.slice(0,10)
 df254 = pd.DataFrame(df254.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df254 = df254.sort_values(by=['预警时间'])
 ax = df254.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df254.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top8 +' '+ 'Closing Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 9 No. of Closing Time Trend (Potentially_Problematic) --> df255
try:
 top9 = df246.iloc[8]['Source']
 t9_speed= df246.iloc[8]['Closing Speed']
 df255 = df57.copy()
 df255['车厢'] = df255['车厢'].astype(str).str.zfill(2)
 df255['Source'] = df255['车组']+ '_' + df255['车厢'] + '_' + df255['Closing DCU']
 df255 = df255.loc[(df255['Source'] == top9) & (df255['Closing Speed'] == t9_speed)]
 df255['预警时间'] = df255['预警时间'].str.slice(0,10)
 df255 = pd.DataFrame(df255.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df255 = df255.sort_values(by=['预警时间'])
 ax = df255.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df255.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top9 +' '+ 'Closing Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Top 10 No. of Closing Time Trend (Potentially_Problematic) --> df256
try:
 top10 = df246.iloc[9]['Source']
 t10_speed= df246.iloc[9]['Closing Speed']
 df256 = df57.copy()
 df256['车厢'] = df256['车厢'].astype(str).str.zfill(2)
 df256['Source'] = df256['车组']+ '_' + df256['车厢'] + '_' + df256['Closing DCU']
 df256 = df256.loc[(df256['Source'] == top10) & (df256['Closing Speed'] == t10_speed)]
 df256['预警时间'] = df256['预警时间'].str.slice(0,10)
 df256 = pd.DataFrame(df256.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df256 = df256.sort_values(by=['预警时间'])
 ax = df256.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df256.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top10 +' '+ 'Closing Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Potentially_Problematic\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Closing Time Trend (Potentially_Problematic)')
    plt.close()


# Believed to be Abnormal Cases (Closing Time) --> df257
df257 = df57.copy()
df257 = df257[(df257['Closing Speed'] >=8)]


# Top Ten DCU Closing Time Excel File (Abnormal) --> df258
df258 = df257.copy()
df258['车厢'] = df258['车厢'].astype(str).str.zfill(2)
df258['Source'] = df258['车组']+ '_' + df258['车厢'] + '_' + df258['Closing DCU']
df258['预警时间'] = df258['预警时间'].str.slice(0,10)
df258 = pd.DataFrame(df258.groupby(['Source','Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
df258 = df258.reindex(columns=['Source','Closing Speed','Closing Time Count'])
df258 = df258.sort_values(by = 'Closing Speed')


#Top Ten DCU Closing Time Graph (Abnormal) --> df259
try:   
    df259 = df258.nlargest(n = 10 , columns =['Closing Time Count'])
    df259 = df259.sort_values(by='Closing Time Count',ignore_index = True, ascending = False)
    df259.plot.barh(x = 'Source', y= 'Closing Time Count',figsize = (12,12))
    plt.title('Top Ten Closing Time DCU (Abnormal)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Top_Ten_Closing_Time_DCU (Abnormal).png')
    plt.close()
except:
    print('No Top Ten Closing Time Result (Abnormal)')
    plt.close()


# Top 1 No. of Closing Time Trend (Abnormal) --> df260
try:
 top1 = df259.iloc[0]['Source']
 t1_speed= df259.iloc[0]['Closing Speed']
 df260 = df57.copy()
 df260['车厢'] = df260['车厢'].astype(str).str.zfill(2)
 df260['Source'] = df260['车组']+ '_' + df260['车厢'] + '_' + df260['Closing DCU']
 df260 = df260.loc[(df260['Source'] == top1) & (df260['Closing Speed'] == t1_speed)]
 df260['预警时间'] = df260['预警时间'].str.slice(0,10)
 df260 = pd.DataFrame(df260.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df260 = df260.sort_values(by=['预警时间'])
 ax = df260.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df260.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top1 +' '+ 'Closing Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Closing Time Trend (Abnormal)')
    plt.close()


# Top 2 No. of Closing Time Trend (Abnormal) --> df261
try:
 top2 = df259.iloc[1]['Source']
 t2_speed= df259.iloc[1]['Closing Speed']
 df261 = df57.copy()
 df261['车厢'] = df261['车厢'].astype(str).str.zfill(2)
 df261['Source'] = df261['车组']+ '_' + df261['车厢'] + '_' + df261['Closing DCU']
 df261 = df261.loc[(df261['Source'] == top2) & (df261['Closing Speed'] == t2_speed)]
 df261['预警时间'] = df261['预警时间'].str.slice(0,10)
 df261 = pd.DataFrame(df261.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df261 = df261.sort_values(by=['预警时间'])
 ax = df261.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df261.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top2 +' '+ 'Closing Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Closing Time Trend (Abnormal)')
    plt.close()


# Top 3 No. of Closing Time Trend (Abnormal) --> df262
try:
 top3 = df259.iloc[2]['Source']
 t3_speed= df259.iloc[2]['Closing Speed']
 df262 = df57.copy()
 df262['车厢'] = df262['车厢'].astype(str).str.zfill(2)
 df262['Source'] = df262['车组']+ '_' + df262['车厢'] + '_' + df262['Closing DCU']
 df262 = df262.loc[(df262['Source'] == top3) & (df262['Closing Speed'] == t3_speed)]
 df262['预警时间'] = df262['预警时间'].str.slice(0,10)
 df262 = pd.DataFrame(df262.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df262 = df262.sort_values(by=['预警时间'])
 ax = df262.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df262.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top3 +' '+ 'Closing Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Closing Time Trend (Abnormal)')
    plt.close()


# Top 4 No. of Closing Time Trend (Abnormal) --> df263
try:
 top4 = df259.iloc[3]['Source']
 t4_speed= df259.iloc[3]['Closing Speed']
 df263 = df57.copy()
 df263['车厢'] = df263['车厢'].astype(str).str.zfill(2)
 df263['Source'] = df263['车组']+ '_' + df263['车厢'] + '_' + df263['Closing DCU']
 df263 = df263.loc[(df263['Source'] == top4) & (df263['Closing Speed'] == t4_speed)]
 df263['预警时间'] = df263['预警时间'].str.slice(0,10)
 df263 = pd.DataFrame(df263.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df263 = df263.sort_values(by=['预警时间'])
 ax = df263.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df263.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top4 +' '+ 'Closing Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Closing Time Trend (Abnormal)')
    plt.close()


# Top 5 No. of Closing Time Trend (Abnormal) --> df264
try:
 top5 = df259.iloc[4]['Source']
 t5_speed= df259.iloc[4]['Closing Speed']
 df264 = df57.copy()
 df264['车厢'] = df264['车厢'].astype(str).str.zfill(2)
 df264['Source'] = df264['车组']+ '_' + df264['车厢'] + '_' + df264['Closing DCU']
 df264 = df264.loc[(df264['Source'] == top5) & (df264['Closing Speed'] == t5_speed)]
 df264['预警时间'] = df264['预警时间'].str.slice(0,10)
 df264 = pd.DataFrame(df264.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df264 = df264.sort_values(by=['预警时间'])
 ax = df264.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df264.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top5 +' '+ 'Closing Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Closing Time Trend (Abnormal)')
    plt.close()


# Top 6 No. of Closing Time Trend (Abnormal) --> df265
try:
 top6 = df259.iloc[5]['Source']
 t6_speed= df259.iloc[5]['Closing Speed']
 df265 = df57.copy()
 df265['车厢'] = df265['车厢'].astype(str).str.zfill(2)
 df265['Source'] = df265['车组']+ '_' + df265['车厢'] + '_' + df265['Closing DCU']
 df265 = df265.loc[(df265['Source'] == top6) & (df265['Closing Speed'] == t6_speed)]
 df265['预警时间'] = df265['预警时间'].str.slice(0,10)
 df265 = pd.DataFrame(df265.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df265 = df265.sort_values(by=['预警时间'])
 ax = df265.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df265.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top6 +' '+ 'Closing Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Closing Time Trend (Abnormal)')
    plt.close()


# Top 7 No. of Closing Time Trend (Abnormal) --> df266
try:
 top7 = df259.iloc[6]['Source']
 t7_speed= df259.iloc[6]['Closing Speed']
 df266 = df57.copy()
 df266['车厢'] = df266['车厢'].astype(str).str.zfill(2)
 df266['Source'] = df266['车组']+ '_' + df266['车厢'] + '_' + df266['Closing DCU']
 df266 = df266.loc[(df266['Source'] == top7) & (df266['Closing Speed'] == t7_speed)]
 df266['预警时间'] = df266['预警时间'].str.slice(0,10)
 df266 = pd.DataFrame(df266.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df266 = df266.sort_values(by=['预警时间'])
 ax = df266.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df266.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top7 +' '+ 'Closing Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Closing Time Trend (Abnormal)')
    plt.close()


# Top 8 No. of Closing Time Trend (Abnormal) --> df267
try:
 top8 = df259.iloc[7]['Source']
 t8_speed= df259.iloc[7]['Closing Speed']
 df267 = df57.copy()
 df267['车厢'] = df267['车厢'].astype(str).str.zfill(2)
 df267['Source'] = df267['车组']+ '_' + df267['车厢'] + '_' + df267['Closing DCU']
 df267 = df267.loc[(df267['Source'] == top8) & (df267['Closing Speed'] == t8_speed)]
 df267['预警时间'] = df267['预警时间'].str.slice(0,10)
 df267 = pd.DataFrame(df267.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df267 = df267.sort_values(by=['预警时间'])
 ax = df267.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df267.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top8 +' '+ 'Closing Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Closing Time Trend (Abnormal)')
    plt.close()


# Top 9 No. of Closing Time Trend (Abnormal) --> df268
try:
 top9 = df259.iloc[8]['Source']
 t9_speed= df259.iloc[8]['Closing Speed']
 df268 = df57.copy()
 df268['车厢'] = df268['车厢'].astype(str).str.zfill(2)
 df268['Source'] = df268['车组']+ '_' + df268['车厢'] + '_' + df268['Closing DCU']
 df268 = df268.loc[(df268['Source'] == top9) & (df268['Closing Speed'] == t9_speed)]
 df268['预警时间'] = df268['预警时间'].str.slice(0,10)
 df268 = pd.DataFrame(df268.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df268 = df268.sort_values(by=['预警时间'])
 ax = df268.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df268.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top9 +' '+ 'Closing Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Closing Time Trend (Abnormal)')
    plt.close()


# Top 10 No. of Closing Time Trend (Abnormal) --> df269
try:
 top10 = df259.iloc[9]['Source']
 t10_speed= df259.iloc[9]['Closing Speed']
 df269 = df57.copy()
 df269['车厢'] = df269['车厢'].astype(str).str.zfill(2)
 df269['Source'] = df269['车组']+ '_' + df269['车厢'] + '_' + df269['Closing DCU']
 df269 = df269.loc[(df269['Source'] == top10) & (df269['Closing Speed'] == t10_speed)]
 df269['预警时间'] = df269['预警时间'].str.slice(0,10)
 df269 = pd.DataFrame(df269.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df269 = df269.sort_values(by=['预警时间'])
 ax = df269.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df269.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top10 +' '+ 'Closing Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Abnormal\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Closing Time Trend (Abnormal)')
    plt.close()


# Believed to be Zero Cases (Closing Time) --> df154
df154 = df57.copy()
df154 = df154.drop(df154[df154['Closing Speed'] > 3.5].index ,axis = 'rows')


# Top Ten DCU Closing Time Excel File (Zero) --> df155
df155 = df154.copy()
df155['车厢'] = df155['车厢'].astype(str).str.zfill(2)
df155['Source'] = df155['车组']+ '_' + df155['车厢'] + '_' + df155['Closing DCU']
df155['预警时间'] = df155['预警时间'].str.slice(0,10)
df155 = pd.DataFrame(df155.groupby(['Source','Closing Speed']).size(),columns=['Closing Time Count']).reset_index()
df155 = df155.reindex(columns=['Source','Closing Speed','Closing Time Count'])
df155 = df155.sort_values(by = 'Closing Speed')


#Top Ten DCU Closing Time Graph (Zero) --> df156
try:   
    df156 = df155.nlargest(n = 10 , columns =['Closing Time Count'])
    df156 = df156.sort_values(by='Closing Time Count',ignore_index = True, ascending = False)
    df156.plot.barh(x = 'Source', y= 'Closing Time Count',figsize = (12,12))
    plt.title('Top Ten Closing Time DCU (Zero)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Top_Ten_Closing_Time_DCU (Zero).png')
    plt.close()
except:
    print('No Top Ten Closing Time Result (Zero)')
    plt.close()


#Top 1 No. of Closing Time Trend (Zero) --> df157
try:
 top1 = df156.iloc[0]['Source']
 t1_speed= df156.iloc[0]['Closing Speed']
 df157 = df57.copy()
 df157['车厢'] = df157['车厢'].astype(str).str.zfill(2)
 df157['Source'] = df157['车组']+ '_' + df157['车厢'] + '_' + df157['Closing DCU']
 df157 = df157.loc[(df157['Source'] == top1) & (df157['Closing Speed'] == t1_speed)]
 df157['预警时间'] = df157['预警时间'].str.slice(0,10)
 df157= pd.DataFrame(df157.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df157 = df157.sort_values(by=['预警时间'])
 ax = df157.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df157.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top1 +' '+ 'Closing Time DCU Trend ({})'.format(t1_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top1.png'.format(user,top1))
 plt.close()
    
except:
    print('No Top1 Closing Time Trend (Zero)')
    plt.close()


#Top 2 No. of Closing Time Trend (Zero) --> df158
try:
 top2 = df156.iloc[1]['Source']
 t2_speed= df156.iloc[1]['Closing Speed']
 df158 = df57.copy()
 df158['车厢'] = df158['车厢'].astype(str).str.zfill(2)
 df158['Source'] = df158['车组']+ '_' + df158['车厢'] + '_' + df158['Closing DCU']
 df158 = df158.loc[(df158['Source'] == top2) & (df158['Closing Speed'] == t2_speed)]
 df158['预警时间'] = df158['预警时间'].str.slice(0,10)
 df158= pd.DataFrame(df158.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df158 = df158.sort_values(by=['预警时间'])
 ax = df158.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df158.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top2 +' '+ 'Closing Time DCU Trend ({})'.format(t2_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top2.png'.format(user,top2))
 plt.close()
    
except:
    print('No Top2 Closing Time Trend (Zero)')
    plt.close()


#Top 3 No. of Closing Time Trend (Zero) --> df159
try:
 top3 = df156.iloc[2]['Source']
 t3_speed= df156.iloc[2]['Closing Speed']
 df159 = df57.copy()
 df159['车厢'] = df159['车厢'].astype(str).str.zfill(2)
 df159['Source'] = df159['车组']+ '_' + df159['车厢'] + '_' + df159['Closing DCU']
 df159 = df159.loc[(df159['Source'] == top3) & (df159['Closing Speed'] == t3_speed)]
 df159['预警时间'] = df159['预警时间'].str.slice(0,10)
 df159= pd.DataFrame(df159.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df159 = df159.sort_values(by=['预警时间'])
 ax = df159.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df159.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top3 +' '+ 'Closing Time DCU Trend ({})'.format(t3_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top3.png'.format(user,top3))
 plt.close()
    
except:
    print('No Top3 Closing Time Trend (Zero)')
    plt.close()


#Top 4 No. of Closing Time Trend (Zero) --> df160
try:
 top4 = df156.iloc[3]['Source']
 t4_speed= df156.iloc[3]['Closing Speed']
 df160 = df57.copy()
 df160['车厢'] = df160['车厢'].astype(str).str.zfill(2)
 df160['Source'] = df160['车组']+ '_' + df160['车厢'] + '_' + df160['Closing DCU']
 df160 = df160.loc[(df160['Source'] == top4) & (df160['Closing Speed'] == t4_speed)]
 df160['预警时间'] = df160['预警时间'].str.slice(0,10)
 df160= pd.DataFrame(df160.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df160 = df160.sort_values(by=['预警时间'])
 ax = df160.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df160.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top4 +' '+ 'Closing Time DCU Trend ({})'.format(t4_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top4.png'.format(user,top4))
 plt.close()
    
except:
    print('No Top4 Closing Time Trend (Zero)')
    plt.close()


#Top 5 No. of Closing Time Trend (Zero) --> df161
try:
 top5 = df156.iloc[4]['Source']
 t5_speed= df156.iloc[4]['Closing Speed']
 df161 = df57.copy()
 df161['车厢'] = df161['车厢'].astype(str).str.zfill(2)
 df161['Source'] = df161['车组']+ '_' + df161['车厢'] + '_' + df161['Closing DCU']
 df161 = df161.loc[(df161['Source'] == top5) & (df161['Closing Speed'] == t5_speed)]
 df161['预警时间'] = df161['预警时间'].str.slice(0,10)
 df161= pd.DataFrame(df161.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df161 = df161.sort_values(by=['预警时间'])
 ax = df161.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df161.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top5 +' '+ 'Closing Time DCU Trend ({})'.format(t5_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top5.png'.format(user,top5))
 plt.close()
    
except:
    print('No Top5 Closing Time Trend (Zero)')
    plt.close()


#Top 6 No. of Closing Time Trend (Zero) --> df162
try:
 top6 = df156.iloc[5]['Source']
 t6_speed= df156.iloc[5]['Closing Speed']
 df162 = df57.copy()
 df162['车厢'] = df162['车厢'].astype(str).str.zfill(2)
 df162['Source'] = df162['车组']+ '_' + df162['车厢'] + '_' + df162['Closing DCU']
 df162 = df162.loc[(df162['Source'] == top6) & (df162['Closing Speed'] == t6_speed)]
 df162['预警时间'] = df162['预警时间'].str.slice(0,10)
 df162= pd.DataFrame(df162.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df162 = df162.sort_values(by=['预警时间'])
 ax = df162.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df162.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top6 +' '+ 'Closing Time DCU Trend ({})'.format(t6_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top6.png'.format(user,top6))
 plt.close()
    
except:
    print('No Top6 Closing Time Trend (Zero)')
    plt.close()


#Top 7 No. of Closing Time Trend (Zero) --> df163
try:
 top7 = df156.iloc[6]['Source']
 t7_speed= df156.iloc[6]['Closing Speed']
 df163 = df57.copy()
 df163['车厢'] = df163['车厢'].astype(str).str.zfill(2)
 df163['Source'] = df163['车组']+ '_' + df163['车厢'] + '_' + df163['Closing DCU']
 df163 = df163.loc[(df163['Source'] == top7) & (df163['Closing Speed'] == t7_speed)]
 df163['预警时间'] = df163['预警时间'].str.slice(0,10)
 df163= pd.DataFrame(df163.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df163 = df163.sort_values(by=['预警时间'])
 ax = df163.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df163.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top7 +' '+ 'Closing Time DCU Trend ({})'.format(t7_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top7.png'.format(user,top7))
 plt.close()
    
except:
    print('No Top7 Closing Time Trend (Zero)')
    plt.close()


#Top 8 No. of Closing Time Trend (Zero) --> df164
try:
 top8 = df156.iloc[7]['Source']
 t8_speed= df156.iloc[7]['Closing Speed']
 df164 = df57.copy()
 df164['车厢'] = df164['车厢'].astype(str).str.zfill(2)
 df164['Source'] = df164['车组']+ '_' + df164['车厢'] + '_' + df164['Closing DCU']
 df164 = df164.loc[(df164['Source'] == top8) & (df164['Closing Speed'] == t8_speed)]
 df164['预警时间'] = df164['预警时间'].str.slice(0,10)
 df164= pd.DataFrame(df164.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df164 = df164.sort_values(by=['预警时间'])
 ax = df164.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df164.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top8 +' '+ 'Closing Time DCU Trend ({})'.format(t8_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top8.png'.format(user,top8))
 plt.close()
    
except:
    print('No Top8 Closing Time Trend (Zero)')
    plt.close()


#Top 9 No. of Closing Time Trend (Zero) --> df165
try:
 top9 = df156.iloc[8]['Source']
 t9_speed= df156.iloc[8]['Closing Speed']
 df165 = df57.copy()
 df165['车厢'] = df165['车厢'].astype(str).str.zfill(2)
 df165['Source'] = df165['车组']+ '_' + df165['车厢'] + '_' + df165['Closing DCU']
 df165 = df165.loc[(df165['Source'] == top9) & (df165['Closing Speed'] == t9_speed)]
 df165['预警时间'] = df165['预警时间'].str.slice(0,10)
 df165= pd.DataFrame(df165.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df165 = df165.sort_values(by=['预警时间'])
 ax = df165.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df165.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top9 +' '+ 'Closing Time DCU Trend ({})'.format(t9_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top9.png'.format(user,top9))
 plt.close()
    
except:
    print('No Top9 Closing Time Trend (Zero)')
    plt.close()


#Top 10 No. of Closing Time Trend (Zero) --> df166
try:
 top10 = df156.iloc[9]['Source']
 t10_speed= df156.iloc[9]['Closing Speed']
 df166 = df57.copy()
 df166['车厢'] = df166['车厢'].astype(str).str.zfill(2)
 df166['Source'] = df166['车组']+ '_' + df166['车厢'] + '_' + df166['Closing DCU']
 df166 = df166.loc[(df166['Source'] == top10) & (df166['Closing Speed'] == t10_speed)]
 df166['预警时间'] = df166['预警时间'].str.slice(0,10)
 df166= pd.DataFrame(df166.groupby(['Source' ,'预警时间']).size(),columns=['Closing Time Count']).reset_index()
 df166 = df166.sort_values(by=['预警时间'])
 ax = df166.plot.scatter(x= '预警时间', y= 'Closing Time Count', style='b',figsize = (12,12))
 df166.plot.line(x= '预警时间', y='Closing Time Count', ax=ax, style='b',rot=25)
 plt.title(top10 +' '+ 'Closing Time DCU Trend ({})'.format(t10_speed))
 plt.ylabel('Count')
 plt.xlabel('Date')
 #plt.savefig(r'C:\Users\{0}\Downloads\location\Opening_Closing_Time\Top_ten\Closing_Time\Zero\Trends\{1}_Top10.png'.format(user,top10))
 plt.close()
    
except:
    print('No Top10 Closing Time Trend (Zero)')
    plt.close()


# Closing Time Group Count with a particular range (3.6-3.9) -->  df274
try:
    df274 = df57.copy()
    df274 = df274[(df274['Closing Speed'] >= 3.6) & (df274['Closing Speed'] <= 3.9 )]
    df274['车厢'] = df274['车厢'].astype('str')
    df274['Source'] = df274['车组'] + '_' + df274['车厢'] + '_' + df274['Closing DCU']
    df274 = pd.DataFrame(df274.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df274['sort1'] = df274['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df274['sort2'] = df274['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df274['sort3'] = df274['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df274['sort1'] = df274['sort1'].astype("int")
    df274['sort2'] = df274['sort2'].astype("int")
    df274['sort3'] = df274['sort3'].astype("int")
    df274 = df274.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df274.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Closing Time Range Count (3.6-3.9)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Range_Count\Closing_Time_Range_Count(3.6-3.9).png')
    plt.close()
    
except:
    print('No Closing Time Range Count (3.6-3.9) Graph')
    plt.close()


# Closing Time Group Count with a particular range (4.0-4.9) -->  df275
try:
    df275 = df57.copy()
    df275 = df275[(df275['Closing Speed'] >= 4.0) & (df275['Closing Speed'] <= 4.9 )]
    df275['车厢'] = df275['车厢'].astype('str')
    df275['Source'] = df275['车组'] + '_' + df275['车厢'] + '_' + df275['Closing DCU']
    df275 = pd.DataFrame(df275.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df275['sort1'] = df275['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df275['sort2'] = df275['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df275['sort3'] = df275['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df275['sort1'] = df275['sort1'].astype("int")
    df275['sort2'] = df275['sort2'].astype("int")
    df275['sort3'] = df275['sort3'].astype("int")
    df275 = df275.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df275.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Closing Time Range Count (4.0-4.9)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Range_Count\Closing_Time_Range_Count(4.0-4.9).png')
    plt.close()
    
except:
    print('No Closing Time Range Count (4.0-4.9) Graph')
    plt.close()


# Closing Time Group Count with a particular range (5.0-9.9) -->  df276
try:
    df276 = df57.copy()
    df276 = df276[(df276['Closing Speed'] >= 5.0) & (df276['Closing Speed'] <= 9.9 )]
    df276['车厢'] = df276['车厢'].astype('str')
    df276['Source'] = df276['车组'] + '_' + df276['车厢'] + '_' + df276['Closing DCU']
    df276 = pd.DataFrame(df276.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df276['sort1'] = df276['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df276['sort2'] = df276['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df276['sort3'] = df276['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df276['sort1'] = df276['sort1'].astype("int")
    df276['sort2'] = df276['sort2'].astype("int")
    df276['sort3'] = df276['sort3'].astype("int")
    df276 = df276.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df276.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Closing Time Range Count (5.0-9.9)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Range_Count\Closing_Time_Range_Count(5.0-9.9).png')
    plt.close()
    
except:
    print('No Closing Time Range Count (5.0-9.9) Graph')
    plt.close()


# Closing Time Group Count with a particular range (>9.9) -->  df277
try:
    df277 = df57.copy()
    df277 = df277[(df277['Closing Speed'] >9.9)]
    df277['车厢'] = df277['车厢'].astype('str')
    df277['Source'] = df277['车组'] + '_' + df277['车厢'] + '_' + df277['Closing DCU']
    df277 = pd.DataFrame(df277.groupby(['Source']).size(),columns=['Range Count']).reset_index()
    df277['sort1'] = df277['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df277['sort2'] = df277['Source'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
    df277['sort3'] = df277['Source'].str.extract('(?:.*DCU)([0-9]+)(?:)')
    df277['sort1'] = df277['sort1'].astype("int")
    df277['sort2'] = df277['sort2'].astype("int")
    df277['sort3'] = df277['sort3'].astype("int")
    df277 = df277.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = False)
    df277.plot.barh(x = 'Source', y= 'Range Count',figsize = (12,12))
    plt.title('Closing Time Range Count (>9.9)')
    plt.xlabel('Count')
    plt.ylabel('Closing Time DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Opening_Closing_Time\Distributions\Closing_Time\Range_Count\Closing_Time_Range_Count(9.9...).png')
    plt.close()
    
except:
    print('No Closing Time Range Count (>9.9) Graph')
    plt.close()


# Main Pressure Rise Alarm Excel Files  -->  df176

df176 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df176['Pressure Rise'] = df176['预警描述'].str.extract('(?:.*Main Pressure rise)([0.0-9.0]+)')
df176['Pressure Rise'] = df176['Pressure Rise'].astype("float")

df176 = df176.reindex(columns=['车组','车厢','预警时间','Pressure Rise','预警描述']) #'Current_Station_Pressure_Rise'
df176 = df176.dropna(axis = 0 ,how = 'any')
df176 = df176.reset_index(drop=True)


# Main Pressure Rise Standard  -->  df177
df177 = df176.copy()
df177['Hi'] = df177['预警描述'].str.extract('(?:.*<)([0.0-9.0]+)(?:)')
df177 = df177.drop(df177[df177['Hi'] == '0'].index, axis = 'rows')
df177 = df177.dropna(axis=0,how='any')
df177.loc[(df177['预警描述'].str.contains('Main Pressure rise') == True),'Main Pressure Rise Standard'] = '< ' + df177['Hi']
df177 = df177.dropna(axis = 0, how = 'any')
df177 = pd.DataFrame(df177['Main Pressure Rise Standard'])[:1]
df177 = df177.reset_index(drop = True)


# Main Pressure Rise with Standard  -->  df178
df178 = pd.DataFrame(pd.concat([df176,df177],axis=1))
df178 = df178.drop(columns='预警描述')
df178 = df178.fillna('               // ')


# Main Pressure Rise (Group_Count)  -->  df179
df179 = df178.copy()
df179 = pd.DataFrame(df179.groupby(['Pressure Rise']).size(),columns=['Pressure Rise Count']).reset_index()
df179 = df179.sort_values(by='Pressure Rise Count',ascending = False)
df179 = df179.reset_index(drop = True)


# Generate Graph for analyzing Pressure Rise -->  df180
try:
 df180 = df179.copy()
 df180 = df180.sort_values(by = 'Pressure Rise', ascending = False)
 df180.plot.barh(x='Pressure Rise',y = 'Pressure Rise Count', rot=0, width = 0.7,figsize = (12,12))

 plt.title('Pressure Rise Distribution')
 plt.xlabel('Count')
 plt.ylabel('Pressure Rise')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Main_Pressure\Distributions\Pressure Rise\Pressure_Rise_Distribution.png')
 plt.close()
    
except:
    print('No Pressure Rise Alarm Distribution Graph')
    plt.close()



# Main Pressure Rise Excel File (Group Count)   -->  df187

df187 = df178.copy()
df187['车厢'] = df187['车厢'].astype(str).str.zfill(2)
df187['Source'] = df187['车组']+ '_' + df187['车厢']
df187['预警时间'] = df187['预警时间'].str.slice(0,10)
df187 = pd.DataFrame(df187.groupby(['Source','Pressure Rise']).size(),columns=['Pressure Rise Count']).reset_index()
df187 = df187.reindex(columns=['Source','Pressure Rise','Pressure Rise Count'])
df187 = df187.sort_values(by='Pressure Rise Count',ascending = False)


# Top Ten Main Pressure Rise Graph  -->  df188 (For Top_Ten_Graph, Sorted) || df203 (For Top_Ten_Trend, unsorted)

try:   
    df188 = df187.nlargest(n = 10 , columns =['Pressure Rise Count'])
    df203 = df188.copy()
    df188['sort1'] = df188['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df188['sort2'] = df188['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
    df188['sort1'] = df188['sort1'].astype("int")
    df188['sort2'] = df188['sort2'].astype("int")
    df188 = df188.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
    colors = {0.009: 'r' , 0.008: 'b' , 0.007: 'g'}
    colos = list(df188['Pressure Rise'].map(colors))
    ax = df188.plot.barh(x = 'Source', y= 'Pressure Rise Count', color= colos,figsize = (12,12))
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.title('Top Ten Main Pressure Rise Train Car')
    plt.legend(['0.009: Red \n0.008: Blue\n0.007: Green'],loc='best',edgecolor = 'black',prop = {'size':15})
    plt.xlabel('Count')
    plt.ylabel('Pressure Rise Train Car')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Main_Pressure\Top_Ten\Pressure Rise\Top_Ten_Pressure_Rise.png')
    plt.close()
    
except:
    print('No Top Ten Pressure Rise Result')
    plt.close()


# Main Pressure Fall Alarm Excel Files  -->  df181
df181 = pd.DataFrame(df6[['预警描述','车组','车厢','预警时间']]).copy()
df181['Pressure Fall'] = df181['预警描述'].str.extract('(?:.*Main Pressure fall)(-[0.0-9.0]+)')
df181['Pressure Fall'] = df181['Pressure Fall'].astype("float")

df181 = df181.reindex(columns=['车组','车厢','预警时间','Pressure Fall','预警描述']) # 'Current_Station_Pressure_Fall'
df181 = df181.dropna(axis = 0 ,how = 'any')
df181 = df181.reset_index(drop=True)


# Main Pressure Fall Standard  -->  df182
df182 = df181.copy()
df182['Hi'] = df182['预警描述'].str.extract('(?:.*<)(-[0.0-9.0]+)(?:)')
df182 = df182.dropna(axis=0,how='any')
df182.loc[(df182['预警描述'].str.contains('Main Pressure fall') == True),'Main Pressure Fall Standard'] = '< ' + df182['Hi']
df182 = df182.dropna(axis = 0, how = 'any')
df182 = pd.DataFrame(df182['Main Pressure Fall Standard'])[:1]
df182 = df182.reset_index(drop = True)


# Main Pressure Fall with Standard  -->  df183
df183 = pd.DataFrame(pd.concat([df181,df182],axis=1))
df183 = df183.drop(columns='预警描述')
df183 = df183.fillna('               // ')


# Main Pressure Fall (Group_Count)  -->  df184
df184 = df183.copy()
df184 = pd.DataFrame(df184.groupby(['Pressure Fall']).size(),columns=['Pressure Fall Count']).reset_index()
df184 = df184.sort_values(by='Pressure Fall Count',ascending = False)
df184 = df184.reset_index(drop = True)


# Generate Graph for analyzing Pressure Fall -->  df185
try:
 df185 = df184.copy()
 df185 = df185.sort_values(by = 'Pressure Fall', ascending = False)
 df185.plot.barh(x='Pressure Fall',y = 'Pressure Fall Count', rot=0, width = 0.7,figsize = (12,12))

 plt.title('Pressure Fall Distribution')
 plt.xlabel('Count')
 plt.ylabel('Pressure Fall')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Main_Pressure\Distributions\Pressure Fall\Pressure_Fall_Distribution.png')
 plt.close()
    
except:
    print('No Pressure Fall Alarm Distribution Graph')
    plt.close()


# Main Pressure Fall Excel File (Group Count)   -->  df199

df199 = df183.copy()
df199['车厢'] = df199['车厢'].astype(str).str.zfill(2)
df199['Source'] = df199['车组']+ '_' + df199['车厢']
df199['预警时间'] = df199['预警时间'].str.slice(0,10)
df199 = pd.DataFrame(df199.groupby(['Source','Pressure Fall']).size(),columns=['Pressure Fall Count']).reset_index()
df199 = df199.reindex(columns=['Source','Pressure Fall','Pressure Fall Count'])
df199 = df199.sort_values(by='Pressure Fall Count',ascending = False)


# Top Ten Main Pressure Fall Graph  -->  df200 (For Top_Ten_Graph, Sorted) || df201 (For Top_Ten_Trend, unsorted)

try:   
    df200 = df199.nlargest(n = 10 , columns =['Pressure Fall Count'])
    df201 = df200
    df200['sort1'] = df200['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
    df200['sort2'] = df200['Source'].str.extract('(?:.*_)([0-9]+)(?:)')
    df200['sort1'] = df200['sort1'].astype("int")
    df200['sort2'] = df200['sort2'].astype("int")
    df200 = df200.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
    colors = {-0.011: 'r' , -0.012: 'b' , -0.014: 'g',-0.015: '#FF6800',-0.016: '#EE82EE',-0.017: '#E00DAB',-0.018: '#FFFF00'}
    colos = list(df200['Pressure Fall'].map(colors))
    ax = df200.plot.barh(x = 'Source', y= 'Pressure Fall Count', color= colos,figsize = (12,12))
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.title('Top Ten Main Pressure Fall Train Car')
    plt.legend(['-0.011: Red\n-0.012: Blue\n-0.014: Green\n-0.015: Orange\n-0.016: Pink\n-0.017 : Purple\n-0.018: Yellow '],loc='best',edgecolor = 'black',prop = {'size':15})
    plt.xlabel('Count')
    plt.ylabel('Pressure Fall Train Car')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Main_Pressure\Top_Ten\Pressure Fall\Top_Ten_Pressure_Fall.png')
    plt.close()
    
except:
    print('No Top Ten Pressure Fall Result')
    plt.close()


# Merge Main Pressure Rise and Fall (Group Count) into a single dataframe  -->  df186
df186 = pd.DataFrame(pd.concat([df179,df184],axis=1))
df186 = df186.fillna('               // ')


#######################################################################################################################################################################################


