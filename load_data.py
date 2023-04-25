StartDate = '2023-4-1'
EndDate = '2023-4-24'

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
    elif idxx == 19233:
       return 'G1 (EA)'
    elif idxx == 19234:
       return 'G2 (virtual track behind 5219)'
    elif idxx == 19217:
       return  'DJ'
    elif idxx == 24033:
       return 'G1 (JK)'
    elif idxx == 24034:
       return 'G2 (JJ)'
    elif idxx == 24017:
        return 'virtual track behind point 5511'
    elif idxx == 25617:
       return 'virtual track behind point 5613'
    elif idxx == 11233:
       return 'virtual track on left side of point 5714'
    elif idxx == 1937:
        return 'PL 1'
    elif idxx == 2417:
       return 'G3N (YW2,YX1,YX2)'
    elif idxx == 2577:
        return 'G1N (L015)'
    elif idxx == 2578:
        return 'G2N (L013)'
    elif idxx == 2593:
       return 'L002'
    elif idxx == 2594:
        return 'L026'
    elif idxx == 11217:
       return 'NM'
    elif idxx == 11218:
       return 'NC'
    elif idxx == 11219:
       return 'H166'
    elif idxx == 11221:
       return 'H171'
    elif idxx == 11222:
        return 'PH'
    elif idxx == 1457:
       return '1'
    elif idxx == 1473:
       return '1'
    elif idxx == 14417:
       return '1'
    elif idxx == 3857:
       return 'AAA'
    elif idxx == 273:
       return 'Line B'
    elif idxx == 274:
       return 'Line A'
    elif idxx == 385:
       return 'AAC'
    elif idxx == 241:
       return 'G2S (YY1,YY2)'
    elif idxx == 242:
       return 'G3S (YV)'
    elif idxx == 257:
       return 'G1S (L014)'
    elif idxx == 258 :
       return 'G2S (L012)'
    elif idxx == 17:
       return 'PL1'
    elif idxx == 18:
       return 'PL2'
    elif idxx == 19:
       return 'PL3'
    elif idxx == 20:
       return 'PL4'
    elif idxx == 21:
       return 'PL5'
    elif idxx == 22:
       return 'PL6'
    elif idxx == 1617:
       return 'R7'
    elif idxx == 17617:
       return 'virtual track behind point 5135'

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
    elif name == 19233:
       return 'MKK Freight Yard'
    elif name == 19234:
       return 'MKK Freight Yard'
    elif name == 19217:
       return  'MKK Freight Yard'
    elif name == 24033:
       return 'Sha Tin Freight Terminal'
    elif name == 24034:
       return 'Sha Tin Freight Terminal'
    elif name == 24017:
        return 'Sha Tin Freight Terminal (Neck)'
    elif name == 25617:
       return 'Fo Tan Freight Terminal'
    elif name == 11233:
       return 'Fo Tan Pway Subdepot'
    elif name == 1937:
        return 'SSG_Driver Platform'
    elif name == 2417:
       return 'Abattoir Siding (North)'
    elif name == 2577:
        return 'Lo Wu Marshalling Yard (North)'
    elif name == 2578:
        return 'Lo Wu Marshalling Yard (North)'
    elif name == 2593:
       return 'Lo Wu Marshalling Yard'
    elif name == 2594:
        return 'Lo Wu Marshalling Yard'
    elif name == 11217:
       return 'Dep_E1 (Slot 1)'
    elif name == 11218:
       return 'Dep_E2 (Slot 2)'
    elif name == 11219:
       return 'Dep_E3 (Slot 3)'
    elif name == 11221:
       return 'Dep_E5 (Slot 5)'
    elif name == 11222:
        return 'Dep_E6 (Slot 6)'
    elif name == 1457:
       return 'HTD Test Track 1'
    elif name == 1473:
       return 'HTD Test Track 2'
    elif name == 14417:
       return 'HTD Test Track'
    elif name == 3857:
       return 'ADM turnback siding (stabling location)'
    elif name == 273:
       return 'Mainland China (Tokenless Block)'
    elif name == 274:
       return 'Mainland China (Tokenless Block)'
    elif name == 385:
       return 'ADM turnback siding (turnback location)'
    elif name == 241:
       return 'Abattoir Siding (South)'
    elif name == 242:
       return 'Abattoir Siding (South)'
    elif name == 257:
       return 'Lo Wu Marshalling Yard (South)'
    elif name == 258 :
       return 'Lo Wu Marshalling Yard (South)'
    elif name == 17:
       return 'Old Hung Hom'
    elif name == 18:
       return 'Old Hung Hom'
    elif name == 19:
       return 'Old Hung Hom'
    elif name == 20:
       return 'Old Hung Hom'
    elif name == 21:
       return 'Old Hung Hom'
    elif name == 22:
       return 'Old Hung Hom'
    elif name == 1617:
       return 'Old Hung Hom'
    elif name == 17617:
       return 'Ho Man Tin Siding'


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

#######################################################################################################################################################################################


