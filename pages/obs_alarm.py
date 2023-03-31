
#!/usr/bin/env python
# coding: utf-8

# In[7]:
from app import app
import os 
#import sys
import pandas as pd
import math
import matplotlib.pyplot as plt
import openpyxl
from time import sleep
import string
from matplotlib.ticker import MaxNLocator
import plotly.express as px
#sys.path.insert(0, 'C:\\Users\\SORickCH\\Desktop\\web')
from load_data import get_dataframe , map_id, map_stname, user
from dash import Dash, dcc, html, Input, Output, dash_table


df6 = get_dataframe()

# DCU 1 --> df8 (Obstacle Detected)
try:
 df8 = df6.copy()
 df8['sortout'] = df8['车组'].str.slice(1,3)
 df8['sortout'] = df8['sortout'].astype("int")
 df8 = df8.sort_values(by=['sortout'],ignore_index = True)
 df8.loc[(df8['预警描述'].str.contains('DCU1_Obstacle Detected') == True),'DCU1 Obstacle Detected'] = "X"
 df8 = df8.dropna(axis=0 ,how = 'any')

except:
 df8 = df8.dropna(axis=0 ,how = 'any')
 pass


# In[8]:


#DCU 2 --> df40 (Obstacle Detected)
try:
 df40 = df6.copy()
 df40['sortout'] = df40['车组'].str.slice(1,3)
 df40['sortout'] = df40['sortout'].astype("int")
 df40 = df40.sort_values(by=['sortout'],ignore_index = True)
 df40.loc[(df40['预警描述'].str.contains('DCU2_Obstacle Detected') == True),'DCU2 Obstacle Detected'] = "X"
 df40 = df40.dropna(axis=0 ,how = 'any')
    
except:
    df40 = df40.dropna(axis=0 ,how = 'any')
    pass


# In[9]:


#DCU 3 --> df41 (Obstacle Detected)
try:
 df41 = df6.copy()
 df41['sortout'] = df41['车组'].str.slice(1,3)
 df41['sortout'] = df41['sortout'].astype("int")
 df41 = df41.sort_values(by=['sortout'],ignore_index = True)
 df41.loc[(df41['预警描述'].str.contains('DCU3_Obstacle Detected') == True),'DCU3 Obstacle Detected'] = "X"
 df41 = df41.dropna(axis=0 ,how = 'any')
    
except:
    df41 = df41.dropna(axis=0 ,how = 'any')
    pass


# In[10]:


#DCU 4 --> df42 (Obstacle Detected)
try:
 df42 = df6.copy()
 df42['sortout'] = df42['车组'].str.slice(1,3) 
 df42['sortout'] = df42['sortout'].astype("int")
 df42 = df42.sort_values(by=['sortout'],ignore_index = True)
 df42.loc[(df42['预警描述'].str.contains('DCU4_Obstacle Detected') == True),'DCU4 Obstacle Detected'] = "X"
 df42 = df42.dropna(axis=0 ,how = 'any')
    
except:
    df42 = df42.dropna(axis=0 ,how = 'any')
    pass


# In[11]:


#DCU 5 --> df43 (Obstacle Detected)
try:
 df43 = df6.copy()
 df43['sortout'] = df43['车组'].str.slice(1,3)
 df43['sortout'] = df43['sortout'].astype("int")
 df43 = df43.sort_values(by=['sortout'],ignore_index = True)
 df43.loc[(df43['预警描述'].str.contains('DCU5_Obstacle Detected') == True),'DCU5 Obstacle Detected'] = "X"
 df43 = df43.dropna(axis=0 ,how = 'any')
    
except:
    df43 = df43.dropna(axis=0 ,how = 'any')
    pass


# In[12]:


#DCU 6 --> df44 (Obstacle Detected)
try:
 df44 = df6.copy()
 df44['sortout'] = df44['车组'].str.slice(1,3)
 df44['sortout'] = df44['sortout'].astype("int")
 df44 = df44.sort_values(by=['sortout'],ignore_index = True)
 df44.loc[(df44['预警描述'].str.contains('DCU6_Obstacle Detected') == True),'DCU6 Obstacle Detected'] = "X"
 df44 = df44.dropna(axis=0 ,how = 'any')
    
except:
    df44 = df44.dropna(axis=0 ,how = 'any')
    pass


# In[13]:


#DCU 7 --> df45 (Obstacle Detected)
try:
 df45 = df6.copy()
 df45['sortout'] = df45['车组'].str.slice(1,3)
 df45['sortout'] = df45['sortout'].astype("int")
 df45 = df45.sort_values(by=['sortout'],ignore_index = True)
 df45.loc[(df45['预警描述'].str.contains('DCU7_Obstacle Detected') == True),'DCU7 Obstacle Detected'] = "X"
 df45 = df45.dropna(axis=0 ,how = 'any')
    
except:
    df45 = df45.dropna(axis=0 ,how = 'any')
    pass


# In[14]:


#DCU 8 --> df46 (Obstacle Detected)
try:
 df46 = df6.copy()
 df46['sortout'] = df46['车组'].str.slice(1,3)
 df46['sortout'] = df46['sortout'].astype("int")
 df46 = df46.sort_values(by=['sortout'],ignore_index = True)
 df46.loc[(df46['预警描述'].str.contains('DCU8_Obstacle Detected') == True),'DCU8 Obstacle Detected'] = "X"
 df46 = df46.dropna(axis=0 ,how = 'any')
    
except:
    df46 = df46.dropna(axis=0 ,how = 'any')
    pass


# In[15]:


#DCU 9 --> df47 (Obstacle Detected)
try:
 df47 = df6.copy()
 df47['sortout'] = df47['车组'].str.slice(1,3)
 df47['sortout'] = df47['sortout'].astype("int") 
 df47 = df47.sort_values(by=['sortout'],ignore_index = True)
 df47.loc[(df47['预警描述'].str.contains('DCU9_Obstacle Detected') == True),'DCU9 Obstacle Detected'] = "X"
 df47 = df47.dropna(axis=0 ,how = 'any')
    
except:
    df47 = df47.dropna(axis=0 ,how = 'any')
    pass


# In[16]:


#DCU 10 --> df48 (Obstacle Detected)
try:
 df48 = df6.copy()
 df48['sortout'] = df48['车组'].str.slice(1,3)
 df48['sortout'] = df48['sortout'].astype("int")
 df48 = df48.sort_values(by=['sortout'],ignore_index = True)
 df48.loc[(df48['预警描述'].str.contains('DCU10_Obstacle Detected') == True),'DCU10 Obstacle Detected'] = "X"
 df48 = df48.dropna(axis=0 ,how = 'any')
    
except:
    df48 = df48.dropna(axis=0 ,how = 'any')
    pass


# In[17]:


#DCU 11 --> df49 (Obstacle Detected)
try:
 df49 = df6.copy()
 df49['sortout'] = df49['车组'].str.slice(1,3)
 df49['sortout'] = df49['sortout'].astype("int")
 df49 = df49.sort_values(by=['sortout'],ignore_index = True)
 df49.loc[(df49['预警描述'].str.contains('DCU11_Obstacle Detected') == True),'DCU11 Obstacle Detected'] = "X"
 df49 = df49.dropna(axis=0 ,how = 'any')
    
except:
    df49 = df49.dropna(axis=0 ,how = 'any')
    pass


# In[18]:


#DCU 12 --> df50 (Obstacle Detected)
try:
 df50 = df6.copy()
 df50['sortout'] = df50['车组'].str.slice(1,3)
 df50['sortout'] = df50['sortout'].astype("int")
 df50 = df50.sort_values(by=['sortout'],ignore_index = True)
 df50.loc[(df50['预警描述'].str.contains('DCU12_Obstacle Detected') == True),'DCU12 Obstacle Detected'] = "X"
 df50 = df50.dropna(axis=0 ,how = 'any')
    
except:
    df50 = df50.dropna(axis=0 ,how = 'any')
    pass


# In[19]:


# Merge all Obstacle Detected Files into a Single File
df51 = pd.concat([df8,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50],axis = 0)
df51 = df51.sort_values(by=['sortout'])
df51 = df51.drop(columns=['sortout'], axis = 1)
df51 = df51.fillna(' ')

'''
# Hence , Joint Current Station into the Obstacle Detected Excel File (.xlsx) 
df52 = pd.DataFrame(df51['预警描述'])
df52['Current_Station'] = df52['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df52 = df52.drop(columns= '预警描述',axis = 1)
df55 = pd.concat([df51,df52],axis=1)
df55 = df55.drop(columns = ['预警描述','预警状态'],axis = 1)
df55['Current_Station'] = df55['Current_Station'].astype("int")
df55['Platform ID'] = df55['Current_Station'].apply(lambda idxx : map_id(idxx))
df55["Current_Station"]= df55["Current_Station"].apply(lambda name : map_stname(name))
df55 = df55.fillna('               // ')

df55 = df55.reindex(columns=['车组','车厢','预警时间','Current_Station','Platform ID','DCU1 Obstacle Detected','DCU2 Obstacle Detected','DCU3 Obstacle Detected','DCU4 Obstacle Detected','DCU5 Obstacle Detected','DCU6 Obstacle Detected','DCU7 Obstacle Detected','DCU8 Obstacle Detected','DCU9 Obstacle Detected','DCU10 Obstacle Detected','DCU11 Obstacle Detected','DCU12 Obstacle Detected'])

writer = pd.ExcelWriter(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Alarm.xlsx') 
df55.to_excel(writer, sheet_name='Obstacle_Detected_Alarm',index = True, startrow = 1, na_rep='NaN', header=False)

workbook = writer.book
worksheet = writer.sheets['Obstacle_Detected_Alarm']
cols = ['车组','车厢','预警时间','Current_Station','Platform ID','DCU1 Obstacle Detected','DCU2 Obstacle Detected','DCU3 Obstacle Detected','DCU4 Obstacle Detected','DCU5 Obstacle Detected','DCU6 Obstacle Detected','DCU7 Obstacle Detected','DCU8 Obstacle Detected','DCU9 Obstacle Detected','DCU10 Obstacle Detected','DCU11 Obstacle Detected','DCU12 Obstacle Detected']
colors = ['#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD','#A5D8DD']


(max_row, max_col) = df55.shape

# Make the columns wider for clarity.
worksheet.set_column(0,  max_col - 1, 12)


# Set the autofilter.
worksheet.autofilter(0, 0, max_row, max_col )

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'fg_color': '#D7E4BC',
    'align' : 'center',
    'border': 1})


# Write the column headers with the defined format.
for col_num, value in enumerate(df55.columns.values):
    worksheet.write(0, col_num + 1, value, header_format)
    
# Fill in the colour for separate the related columns
d = dict(zip(range(25), list(string.ascii_uppercase)[1:]))

for i, col in enumerate(cols):
    f1 = workbook.add_format({'bg_color': colors[i],'border': 1})
    excel_header = str(d[df55.columns.get_loc(col)])
    len_df55 = str(len(df55.index) + 1)

    rng = excel_header + '2:' + excel_header + len_df55
    worksheet.conditional_format(rng, {'type': 'no_blanks',
                                       'format': f1})

#Set the row height
worksheet.set_default_row(27)

#Set the column width ( <!-- Cutomize -- > ) 
worksheet.set_column(1,33,15.9)


# hide index using xlsxwriter
worksheet.set_column(0,0, None, None, {'hidden': True})
writer.close()

'''
# In[20]:


# All Obstacle Detected Trainset with Count (T1-T36)
df401 = pd.DataFrame(df51.groupby(['车组']).size(),columns=['Obstacle Detected Group Count']).reset_index()
df401['sortout'] = df401['车组'].str.slice(1,3).astype('int')
df401 = df401.sort_values(by='sortout')
df401 = df401.drop(columns='sortout')


# In[21]:


# Count the amount of Obstacle Detected (Groupby 车组, 车厢, Detected DCU)
df64 = df6.copy()
df64['Detected DCU'] = df64['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Obstacle Detected)')
df64 = df64.drop(columns = ['预警描述','预警状态'])
df64 = pd.DataFrame(df64.groupby(['车组','车厢','Detected DCU']).size(),columns=['Obstacle Detected Count']).reset_index()
df64['sortout'] = df64['车组'].str.slice(1,3)
df64['sortout'] = df64['sortout'].astype("int")
df64['车厢'] = df64['车厢'].astype(str).str.zfill(2)
df64['Source'] = df64['车组']+ '_' + df64['车厢'] + '_' + df64['Detected DCU']
df64 = df64.sort_values(by=['sortout'],ignore_index = True)
df64 = df64.drop(columns=['sortout','车组','车厢','Detected DCU'],axis = 1)
df64 = df64.reindex(columns=['Source','Obstacle Detected Count'])



# Set up a Source (Filter) to get the occurred time
df102 = df6.copy()
df102['Detected DCU'] = df102['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Obstacle Detected)')
df102 = df102.dropna(how = 'any', axis = 0)
df102 = df102.drop(columns = ['预警描述','预警状态'])
df102['sortout'] = df102['车组'].str.slice(1,3)
df102['sortout'] = df102['sortout'].astype("int")
df102['车厢'] = df102['车厢'].astype(str).str.zfill(2)
df102['Source (Filter)'] = df102['车组']+ '_' + df102['车厢'] + '_' + df102['Detected DCU']
df102 = df102.sort_values(by=['sortout'],ignore_index = True)
df102 = df102.drop(columns=['sortout','车组','车厢','Detected DCU'],axis = 1)
df102 = df102.reindex(columns=['Source (Filter)','预警时间'])

'''
# Convert dataframe to .xlsx file (excel files ) with different formats (Obstacle Detected Count)
df64 = df64.fillna('               // ')
df102 = df102.fillna('               // ')

writer = pd.ExcelWriter(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Count.xlsx') 
df64.to_excel(writer, sheet_name='Obstacle_Detected_Count',index = True, startrow = 1, na_rep='NaN', header=False)
df102.to_excel(writer, sheet_name='Filter',index = True, startrow = 1, na_rep='NaN', header=False)


workbook = writer.book
worksheet = writer.sheets['Obstacle_Detected_Count']
worksheet1 = writer.sheets['Filter']

cols = ['Source','Obstacle Detected Count']
cols1 =['Source (Filter)','预警时间']
colors = ['#A5D8DD','#A5D8DD']
colors1 = ['#9BEE95','#9BEE95']

(max_row, max_col) = df64.shape
(max_row1, max_col1) = df102.shape

# Make the columns wider for clarity.
worksheet.set_column(0,  max_col - 1, 12)
worksheet1.set_column(0,  max_col1 - 1, 12)


# Set the autofilter.
worksheet.autofilter(0, 0, max_row, max_col )
worksheet1.autofilter(0, 0, max_row1, max_col1 )


# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'fg_color': '#D7E4BC',
    'align' : 'center',
    'border': 1})


# Write the column headers with the defined format.
for col_num, value in enumerate(df64.columns.values):
    worksheet.write(0, col_num + 1, value, header_format)
    
for col_num, value in enumerate(df102.columns.values):
    worksheet1.write(0, col_num + 1, value, header_format)
    
# Fill in the colour for separate the related columns
d = dict(zip(range(25), list(string.ascii_uppercase)[1:]))

for i, col in enumerate(cols):
    f1 = workbook.add_format({'bg_color': colors[i],'border': 1})
    excel_header = str(d[df64.columns.get_loc(col)])
    len_df64 = str(len(df64.index) + 1)

    rng = excel_header + '2:' + excel_header + len_df64
    worksheet.conditional_format(rng, {'type': 'no_blanks',
                                       'format': f1})
for i, col in enumerate(cols1):
    f1 = workbook.add_format({'bg_color': colors1[i],'border': 1})
    excel_header = str(d[df102.columns.get_loc(col)])
    len_df102 = str(len(df102.index) + 1)

    rng = excel_header + '2:' + excel_header + len_df102
    worksheet1.conditional_format(rng, {'type': 'no_blanks',
                                       'format': f1})


#Set the row height
worksheet.set_default_row(27)
worksheet1.set_default_row(27)

#Set the column width ( <!-- Cutomize -- > ) 
worksheet.set_column(1,33,20)
worksheet1.set_column(1,33,20)


# Hide index using xlsxwriter
worksheet.set_column(0,0, None, None, {'hidden': True})
worksheet1.set_column(0,0, None, None, {'hidden': True})
writer.close()

#Delete all .png file in a folder (All Obstacle Detected Images)
folder_path = (fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts')
target = os.listdir(folder_path)
for images in target:
    if images.endswith(".png"):
        os.remove(os.path.join(folder_path, images))
'''
# In[22]:


# Generate graph for T1 Obstacle Detected (Total) --> df65
try:
    df65 = df64.loc[(df64['Source'].str.contains('T1_'))].copy()
    df65['sort1'] = df65['Source'].str.slice(3,5)
    df65['sort2'] = df65['Source'].str.slice(9,11)
    df65['sort1'] = df65['sort1'].astype("int")
    df65['sort2'] = df65['sort2'].astype("int")
    df65 = df65.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
    ax = df65.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.title('T1 Obstacle Detected')
    plt.xlabel('Count')
    plt.ylabel('Obstacle Detected DCU')
    #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T1.png')
    plt.close()

except:
    print('No T1 Obstacle Detected Alarm')
    plt.close()


# In[23]:


# Generate graph for T2 Obstacle Detected (Total) --> df66
try:
 df66 = df64.loc[(df64['Source'].str.contains('T2_'))].copy()
 df66['sort1'] = df66['Source'].str.slice(3,5)
 df66['sort2'] = df66['Source'].str.slice(9,11)
 df66['sort1'] = df66['sort1'].astype("int")
 df66['sort2'] = df66['sort2'].astype("int")
 df66 = df66.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df66.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T2 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T2.png')
 plt.close()

except:
    print('No T2 Obstacle Detected Alarm')
    plt.close()


# In[24]:


# Generate graph for T3 Obstacle Detected (Total) --> df67
try:
 df67 = df64.loc[(df64['Source'].str.contains('T3_'))].copy()
 df67['sort1'] = df67['Source'].str.slice(3,5)
 df67['sort2'] = df67['Source'].str.slice(9,11)
 df67['sort1'] = df67['sort1'].astype("int")
 df67['sort2'] = df67['sort2'].astype("int")
 df67 = df67.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df67.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T3 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T3.png')
 plt.close()

except:
    print('No T3 Obstacle Detected Alarm')
    plt.close()


# In[25]:


# Generate graph for T4 Obstacle Detected (Total) --> df68
try:
 df68 = df64.loc[(df64['Source'].str.contains('T4_'))].copy()
 df68['sort1'] = df68['Source'].str.slice(3,5)
 df68['sort2'] = df68['Source'].str.slice(9,11)
 df68['sort1'] = df68['sort1'].astype("int")
 df68['sort2'] = df68['sort2'].astype("int")
 df68 = df68.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df68.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T4 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T4.png')
 plt.close()

except:
    print('No T4 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T5 Obstacle Detected (Total) --> df69
try:
 df69 = df64.loc[(df64['Source'].str.contains('T5_'))].copy()
 df69['sort1'] = df69['Source'].str.slice(3,5)
 df69['sort2'] = df69['Source'].str.slice(9,11)
 df69['sort1'] = df69['sort1'].astype("int")
 df69['sort2'] = df69['sort2'].astype("int")
 df69 = df69.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df69.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T5 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T5.png')
 plt.close()

except:
    print('No T5 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T6 Obstacle Detected (Total) --> df70
try:
 df70 = df64.loc[(df64['Source'].str.contains('T6_'))].copy()
 df70['sort1'] = df70['Source'].str.slice(3,5)
 df70['sort2'] = df70['Source'].str.slice(9,11)
 df70['sort1'] = df70['sort1'].astype("int")
 df70['sort2'] = df70['sort2'].astype("int")
 df70 = df70.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df70.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T6 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T6.png')
 plt.close()

except:
    print('No T6 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T7 Obstacle Detected (Total) --> df71
try:
 df71 = df64.loc[(df64['Source'].str.contains('T7_'))].copy()
 df71['sort1'] = df71['Source'].str.slice(3,5)
 df71['sort2'] = df71['Source'].str.slice(9,11)
 df71['sort1'] = df71['sort1'].astype("int")
 df71['sort2'] = df71['sort2'].astype("int")
 df71 = df71.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df71.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T7 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T7.png')
 plt.close()

except:
    print('No T7 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T8 Obstacle Detected (Total) --> df72
try:
 df72 = df64.loc[(df64['Source'].str.contains('T8_'))].copy()
 df72['sort1'] = df72['Source'].str.slice(3,5)
 df72['sort2'] = df72['Source'].str.slice(9,11)
 df72['sort1'] = df72['sort1'].astype("int")
 df72['sort2'] = df72['sort2'].astype("int")
 df72 = df72.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df72.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T8 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T8.png')
 plt.close()

except:
    print('No T8 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T9 Obstacle Detected (Total) --> df73
try:
 df73 = df64.loc[(df64['Source'].str.contains('T9_'))].copy()
 df73['sort1'] = df73['Source'].str.slice(3,5)
 df73['sort2'] = df73['Source'].str.slice(9,11)
 df73['sort1'] = df73['sort1'].astype("int")
 df73['sort2'] = df73['sort2'].astype("int")
 df73 = df73.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df73.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T9 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T9.png')
 plt.close()

except:
    print('No T9 Obstacle Detected Alarm')
    plt.close()

# Generate graph for T10 Obstacle Detected (Total) --> df74
try:
 df74 = df64.loc[(df64['Source'].str.contains('T10_'))].copy()
 df74['sort1'] = df74['Source'].str.slice(4,6)
 df74['sort2'] = df74['Source'].str.slice(10,12)
 df74['sort1'] = df74['sort1'].astype("int")
 df74['sort2'] = df74['sort2'].astype("int")
 df74 = df74.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df74.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T10 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T10.png')
 plt.close()

except:
    print('No T10 Obstacle Detected Alarm')
    plt.close()

# Generate graph for T11 Obstacle Detected (Total) --> df75
try:
 df75 = df64.loc[(df64['Source'].str.contains('T11_'))].copy()
 df75['sort1'] = df75['Source'].str.slice(4,6)
 df75['sort2'] = df75['Source'].str.slice(10,12)
 df75['sort1'] = df75['sort1'].astype("int")
 df75['sort2'] = df75['sort2'].astype("int")
 df75 = df75.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df75.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T11 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T11.png')
 plt.close()

except:
    print('No T11 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T12 Obstacle Detected (Total) --> df76
try:
 df76 = df64.loc[(df64['Source'].str.contains('T12_'))].copy()
 df76['sort1'] = df76['Source'].str.slice(4,6)
 df76['sort2'] = df76['Source'].str.slice(10,12)
 df76['sort1'] = df76['sort1'].astype("int")
 df76['sort2'] = df76['sort2'].astype("int")
 df76 = df76.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df76.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T12 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T12.png')
 plt.close()

except:
    print('No T12 Obstacle Detected Alarm')
    plt.close()

# Generate graph for T13 Obstacle Detected (Total) --> df77
try:
 df77 = df64.loc[(df64['Source'].str.contains('T13_'))].copy()
 df77['sort1'] = df77['Source'].str.slice(4,6)
 df77['sort2'] = df77['Source'].str.slice(10,12)
 df77['sort1'] = df77['sort1'].astype("int")
 df77['sort2'] = df77['sort2'].astype("int")
 df77 = df77.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df77.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T13 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T13.png')
 plt.close()

except:
    print('No T13 Obstacle Detected Alarm')
    plt.close()

# Generate graph for T14 Obstacle Detected (Total) --> df78
try:
 df78 = df64.loc[(df64['Source'].str.contains('T14_'))].copy()
 df78['sort1'] = df78['Source'].str.slice(4,6)
 df78['sort2'] = df78['Source'].str.slice(10,12)
 df78['sort1'] = df78['sort1'].astype("int")
 df78['sort2'] = df78['sort2'].astype("int")
 df78 = df78.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df78.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T14 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T14.png')
 plt.close()

except:
    print('No T14 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T15 Obstacle Detected (Total) --> df79
try:
 df79 = df64.loc[(df64['Source'].str.contains('T15_'))].copy()
 df79['sort1'] = df79['Source'].str.slice(4,6)
 df79['sort2'] = df79['Source'].str.slice(10,12)
 df79['sort1'] = df79['sort1'].astype("int")
 df79['sort2'] = df79['sort2'].astype("int")
 df79 = df79.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df79.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T15 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T15.png')
 plt.close()

except:
    print('No T15 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T16 Obstacle Detected (Total) --> df80
try:
 df80 = df64.loc[(df64['Source'].str.contains('T16_'))].copy()
 df80['sort1'] = df80['Source'].str.slice(4,6)
 df80['sort2'] = df80['Source'].str.slice(10,12)
 df80['sort1'] = df80['sort1'].astype("int")
 df80['sort2'] = df80['sort2'].astype("int")
 df80 = df80.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df80.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T16 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T16.png')
 plt.close()

except:
    print('No T16 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T17 Obstacle Detected (Total) --> df81
try:
 df81 = df64.loc[(df64['Source'].str.contains('T17_'))].copy()
 df81['sort1'] = df81['Source'].str.slice(4,6)
 df81['sort2'] = df81['Source'].str.slice(10,12)
 df81['sort1'] = df81['sort1'].astype("int")
 df81['sort2'] = df81['sort2'].astype("int")
 df81 = df81.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df81.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T17 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T17.png')
 plt.close()

except:
    print('No T17 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T18 Obstacle Detected (Total) --> df82
try:
 df82 = df64.loc[(df64['Source'].str.contains('T18_'))].copy()
 df82['sort1'] = df82['Source'].str.slice(4,6)
 df82['sort2'] = df82['Source'].str.slice(10,12)
 df82['sort1'] = df82['sort1'].astype("int")
 df82['sort2'] = df82['sort2'].astype("int")
 df82 = df82.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df82.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T18 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T18.png')
 plt.close()

except:
    print('No T18 Obstacle Detected Alarm')
    plt.close()



# Generate graph for T19 Obstacle Detected (Total) --> df83
try:
 df83 = df64.loc[(df64['Source'].str.contains('T19_'))].copy()
 df83['sort1'] = df83['Source'].str.slice(4,6)
 df83['sort2'] = df83['Source'].str.slice(10,12)
 df83['sort1'] = df83['sort1'].astype("int")
 df83['sort2'] = df83['sort2'].astype("int")
 df83 = df83.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df83.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T19 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T19.png')
 plt.close()

except:
    print('No T19 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T20 Obstacle Detected (Total) --> df84
try:
 df84 = df64.loc[(df64['Source'].str.contains('T20_'))].copy()
 df84['sort1'] = df84['Source'].str.slice(4,6)
 df84['sort2'] = df84['Source'].str.slice(10,12)
 df84['sort1'] = df84['sort1'].astype("int")
 df84['sort2'] = df84['sort2'].astype("int")
 df84 = df84.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df84.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T20 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T20.png')
 plt.close()

except:
    print('No T20 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T21 Obstacle Detected (Total) --> df85
try:
 df85 = df64.loc[(df64['Source'].str.contains('T21_'))].copy()
 df85['sort1'] = df85['Source'].str.slice(4,6)
 df85['sort2'] = df85['Source'].str.slice(10,12)
 df85['sort1'] = df85['sort1'].astype("int")
 df85['sort2'] = df85['sort2'].astype("int")
 df85 = df85.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df85.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T21 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T21.png')
 plt.close()

except:
    print('No T21 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T22 Obstacle Detected (Total) --> df86
try:
 df86 = df64.loc[(df64['Source'].str.contains('T22_'))].copy()
 df86['sort1'] = df86['Source'].str.slice(4,6)
 df86['sort2'] = df86['Source'].str.slice(10,12)
 df86['sort1'] = df86['sort1'].astype("int")
 df86['sort2'] = df86['sort2'].astype("int")
 df86 = df86.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df86.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T22 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T22.png')
 plt.close()

except:
    print('No T22 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T23 Obstacle Detected (Total) --> df87
try:
 df87 = df64.loc[(df64['Source'].str.contains('T23_'))].copy()
 df87['sort1'] = df87['Source'].str.slice(4,6)
 df87['sort2'] = df87['Source'].str.slice(10,12)
 df87['sort1'] = df87['sort1'].astype("int")
 df87['sort2'] = df87['sort2'].astype("int")
 df87 = df87.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df87.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T23 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T23.png')
 plt.close()

except:
    print('No T23 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T24 Obstacle Detected (Total) --> df88
try:
 df88 = df64.loc[(df64['Source'].str.contains('T24_'))].copy()
 df88['sort1'] = df88['Source'].str.slice(4,6)
 df88['sort2'] = df88['Source'].str.slice(10,12)
 df88['sort1'] = df88['sort1'].astype("int")
 df88['sort2'] = df88['sort2'].astype("int")
 df88 = df88.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df88.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T24 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T24.png')
 plt.close()

except:
    print('No T24 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T25 Obstacle Detected (Total) --> df89
try:
 df89 = df64.loc[(df64['Source'].str.contains('T25_'))].copy()
 df89['sort1'] = df89['Source'].str.slice(4,6)
 df89['sort2'] = df89['Source'].str.slice(10,12)
 df89['sort1'] = df89['sort1'].astype("int")
 df89['sort2'] = df89['sort2'].astype("int")
 df89 = df89.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df89.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T25 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T25.png')
 plt.close()

except:
    print('No T25 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T26 Obstacle Detected (Total) --> df90
try:
 df90 = df64.loc[(df64['Source'].str.contains('T26_'))].copy()
 df90['sort1'] = df90['Source'].str.slice(4,6)
 df90['sort2'] = df90['Source'].str.slice(10,12)
 df90['sort1'] = df90['sort1'].astype("int")
 df90['sort2'] = df90['sort2'].astype("int")
 df90 = df90.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df90.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T26 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T26.png')
 plt.close()

except:
    print('No T26 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T27 Obstacle Detected (Total) --> df91
try:
 df91 = df64.loc[(df64['Source'].str.contains('T27_'))].copy()
 df91['sort1'] = df91['Source'].str.slice(4,6)
 df91['sort2'] = df91['Source'].str.slice(10,12)
 df91['sort1'] = df91['sort1'].astype("int")
 df91['sort2'] = df91['sort2'].astype("int")
 df91 = df91.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df91.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T27 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T27.png')
 plt.close()

except:
    print('No T27 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T28 Obstacle Detected (Total) --> df92
try:
 df92 = df64.loc[(df64['Source'].str.contains('T28_'))].copy()
 df92['sort1'] = df92['Source'].str.slice(4,6)
 df92['sort2'] = df92['Source'].str.slice(10,12)
 df92['sort1'] = df92['sort1'].astype("int")
 df92['sort2'] = df92['sort2'].astype("int")
 df92 = df92.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df92.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T28 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T28.png')
 plt.close()

except:
    print('No T28 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T29 Obstacle Detected (Total) --> df93
try:
 df93 = df64.loc[(df64['Source'].str.contains('T29_'))].copy()
 df93['sort1'] = df93['Source'].str.slice(4,6)
 df93['sort2'] = df93['Source'].str.slice(10,12)
 df93['sort1'] = df93['sort1'].astype("int")
 df93['sort2'] = df93['sort2'].astype("int")
 df93 = df93.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df93.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T29 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T29.png')
 plt.close()

except:
    print('No T29 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T30 Obstacle Detected (Total) --> df94
try:
 df94 = df64.loc[(df64['Source'].str.contains('T30_'))].copy()
 df94['sort1'] = df94['Source'].str.slice(4,6)
 df94['sort2'] = df94['Source'].str.slice(10,12)
 df94['sort1'] = df94['sort1'].astype("int")
 df94['sort2'] = df94['sort2'].astype("int")
 df94 = df94.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df94.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T30 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T30.png')
 plt.close()
except:
    print('No T30 Obstacle Detected Alarm')
    plt.close() 


# Generate graph for T31 Obstacle Detected (Total) --> df95
try: 
 df95 = df64.loc[(df64['Source'].str.contains('T31_'))].copy()
 df95['sort1'] = df95['Source'].str.slice(4,6)
 df95['sort2'] = df95['Source'].str.slice(10,12)
 df95['sort1'] = df95['sort1'].astype("int")
 df95['sort2'] = df95['sort2'].astype("int")
 df95 = df95.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df95.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T31 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T31.png')
 plt.close()

except:
    print('No T31 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T32 Obstacle Detected (Total) --> df96
try:   
 df96 = df64.loc[(df64['Source'].str.contains('T32_'))].copy()
 df96['sort1'] = df96['Source'].str.slice(4,6)
 df96['sort2'] = df96['Source'].str.slice(10,12)
 df96['sort1'] = df96['sort1'].astype("int")
 df96['sort2'] = df96['sort2'].astype("int")
 df96 = df96.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df96.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T32 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T32.png')
 plt.close()

except:
    print('No T32 Obstacle Detected Alarm')
    plt.close()   


# Generate graph for T33 Obstacle Detected (Total) --> df97
try:   
 df97 = df64.loc[(df64['Source'].str.contains('T33_'))].copy()
 df97['sort1'] = df97['Source'].str.slice(4,6)
 df97['sort2'] = df97['Source'].str.slice(10,12)
 df97['sort1'] = df97['sort1'].astype("int")
 df97['sort2'] = df97['sort2'].astype("int")
 df97 = df97.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df97.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T33 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T33.png')
 plt.close()
except:
    print('No T33 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T34 Obstacle Detected (Total) --> df98
try:   
 df98 = df64.loc[(df64['Source'].str.contains('T34_'))].copy()
 df98['sort1'] = df98['Source'].str.slice(4,6)
 df98['sort2'] = df98['Source'].str.slice(10,12)
 df98['sort1'] = df98['sort1'].astype("int")
 df98['sort2'] = df98['sort2'].astype("int")
 df98 = df98.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df98.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T34 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T34.png')
 plt.close()
except:
    print('No T34 Obstacle Detected Alarm')
    plt.close()


# Generate graph for T35 Obstacle Detected (Total) --> df99
try:   
 df99 = df64.loc[(df64['Source'].str.contains('T35_'))].copy()
 df99['sort1'] = df99['Source'].str.slice(4,6)
 df99['sort2'] = df99['Source'].str.slice(10,12)
 df99['sort1'] = df99['sort1'].astype("int")
 df99['sort2'] = df99['sort2'].astype("int")
 df99 = df99.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df99.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T35 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T35.png')
 plt.close()
except:
    print('No T35 Obstacle Detected Alarm')
    plt.close()



# Generate graph for T36 Obstacle Detected (Total) --> df100
try:   
 df100 = df64.loc[(df64['Source'].str.contains('T36_'))].copy()
 df100['sort1'] = df100['Source'].str.slice(4,6)
 df100['sort2'] = df100['Source'].str.slice(10,12)
 df100['sort1'] = df100['sort1'].astype("int")
 df100['sort2'] = df100['sort2'].astype("int")
 df100 = df100.sort_values(by=['sort1','sort2'],ignore_index = True, ascending = False)
 ax = df100.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 ax.xaxis.get_major_locator().set_params(integer=True)
 plt.title('T36 Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Obstacle_Detected_Charts\T36.png')
 plt.close()
except:
    print('No T36 Obstacle Detected Alarm')
    plt.close()
# In[26]:


# Selector of Obstacle Detected (For DropDownList [Trainset])  -->  df213
df213 = pd.concat([df65,df66,df67,df68,df69,df70,df71,df72,df73,df74,df75,df76,df77,df78,df79,df80,df81,df82,df83,df84,df85,df86,df87,df88,df89,df90,df91,df92,df93,df94,df95,df96,df97,df98,df99,df100],axis = 0)
df213['Type'] = df213['Source'].str.extract('(?:.*T)([0-9]+)(?:_)')
df213['Type'] = 'T' + df213['Type']
df213 = df213.sort_values(by=['sort1','sort2'])


'''
#Delete all .png file in a folder (Top Ten Obstacle Detected Distribution)
folder_path = (fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Top_Ten')
target = os.listdir(folder_path)
for images in target:
    if images.endswith(".png"):
        os.remove(os.path.join(folder_path, images))
'''
# In[27]:


# Top Ten DCU Obstacle Detected Graph --> df101
df101 = df64.nlargest(n=10 , columns =['Obstacle Detected Count']).copy()
datas = list(df101['Obstacle Detected Count'])
try:   
 df101.plot.barh(x = 'Source', y= 'Obstacle Detected Count', rot = 0 ,width = 0.7,figsize = (12,12))
 for index,data in enumerate(datas):
    plt.text(data+0.2,index-0.1, str(data) , fontsize = 13)
 plt.title('Top Ten Obstacle Detected')
 plt.xlabel('Count')
 plt.ylabel('Obstacle Detected DCU')
 #plt.savefig(fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Obstacle_Detected_DCU.png')
 plt.close()
except:
    print('No Top Ten Result')
    plt.close()

'''
#Delete all .png file in a folder (Top Ten Obstacle Detected Trend)
folder_path = (fr'C:\Users\{user}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend')
target = os.listdir(folder_path)
for images in target:
    if images.endswith(".png"):
        os.remove(os.path.join(folder_path, images))
'''
# In[28]:


# Set up a Source (Filter) to get the occurred time
df102 = df6.copy()
df102['Detected DCU'] = df102['预警描述'].str.extract('(?:.*&& )(.+?)(?:_Obstacle Detected)')
df102['车厢'] = df102['车厢'].astype(str).str.zfill(2)
df102['Source (Filter)'] = df102['车组']+ '_' + df102['车厢'] + '_' + df102['Detected DCU']
df102['Current_Station'] = df102['预警描述'].str.extract('(?:.*Station)([0-9]+)(?:.0)')
df102 = df102.dropna(axis = 0, how = 'any')
df102['Current_Station'] = df102['Current_Station'].astype("int")
df102['Platform ID'] = df102['Current_Station'].apply(lambda idxx : map_id(idxx))
df102["Current_Station"]= df102["Current_Station"].apply(lambda name : map_stname(name))
df102['Type'] = df102['Source (Filter)'].str.extract('(?:.*T)([0-9]+)(?:_)')
df102['Type'] = 'T' + df102['Type']
#df102 = df102.drop(columns = ['预警描述','预警状态'])
df102 = df102.dropna(axis=0, how='any')
df102['sort1']= df102['Source (Filter)'].str.extract('(?:.*T)([0-9]+)(?:_)')
df102['sort2']= df102['Source (Filter)'].str.extract('(?:.*_)([0-9]+)(?:_DCU)')
df102['sort3']= df102['Source (Filter)'].str.extract('(?:.*DCU)([0-9]+)(?:)')
df102['sort1'] = df102['sort1'].astype("int")
df102['sort2'] = df102['sort2'].astype("int")
df102['sort3'] = df102['sort3'].astype("int")
df102 = df102.sort_values(by=['sort1','sort2','sort3'],ignore_index = True, ascending = True)
df102 = df102.drop(columns=['车组','车厢','Detected DCU'],axis = 1)
df102 = df102.reindex(columns=['Source (Filter)','预警时间','Current_Station','Platform ID','Type'])


# In[29]:


# Top 1 No. of Obstacle Detected Trend --> df104
top1 = df101.iloc[0]['Source']
df104 = df102.copy()
df104 = df104.loc[(df104['Source (Filter)'] == top1)]
df104['预警时间'] = df104['预警时间'].str.slice(0,10)
df104= pd.DataFrame(df104.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df104 = df104.sort_values(by=['预警时间'])
ax = df104.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df104.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top1 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top1.png'.format(user,top1))
plt.close()


# In[30]:


# Top 2 No. of Obstacle Detected Trend --> df105
top2 = df101.iloc[1]['Source']
df105 = df102.copy()
df105 = df105.loc[(df105['Source (Filter)'] == top2)]
df105['预警时间'] = df105['预警时间'].str.slice(0,10)
df105= pd.DataFrame(df105.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df105 = df105.sort_values(by=['预警时间'])
ax = df105.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df105.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top2 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top2.png'.format(user,top2))
plt.close()



#Top 3 No. of Obstacle Detected Trend --> df106
top3 = df101.iloc[2]['Source']
df106 = df102.copy()
df106 = df106.loc[(df106['Source (Filter)'] == top3)]
df106['预警时间'] = df106['预警时间'].str.slice(0,10)
df106= pd.DataFrame(df106.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df106 = df106.sort_values(by=['预警时间'])
ax = df106.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df106.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top3 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top3.png'.format(user,top3))
plt.close()


#Top 4 No. of Obstacle Detected Trend --> df107
top4 = df101.iloc[3]['Source']
df107 = df102.copy()
df107 = df107.loc[(df107['Source (Filter)'] == top4)]
df107['预警时间'] = df107['预警时间'].str.slice(0,10)
df107= pd.DataFrame(df107.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df107 = df107.sort_values(by=['预警时间'])
ax = df107.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df107.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top4 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top4.png'.format(user,top4))
plt.close()


#Top 5 No. of Obstacle Detected Trend --> df108
top5 = df101.iloc[4]['Source']
df108 = df102.copy()
df108 = df108.loc[(df108['Source (Filter)'] == top5)]
df108['预警时间'] = df108['预警时间'].str.slice(0,10)
df108= pd.DataFrame(df108.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df108 = df108.sort_values(by=['预警时间'])
ax = df108.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df108.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top5 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top5.png'.format(user,top5))
plt.close()


#Top 6 No. of Obstacle Detected Trend --> df109
top6 = df101.iloc[5]['Source']
df109 = df102.copy()
df109 = df109.loc[(df109['Source (Filter)'] == top6)]
df109['预警时间'] = df109['预警时间'].str.slice(0,10)
df109= pd.DataFrame(df109.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df109 = df109.sort_values(by=['预警时间'])
ax = df109.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df109.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top6 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top6.png'.format(user,top6))
plt.close()


#Top 7 No. of Obstacle Detected Trend --> df110
top7 = df101.iloc[6]['Source']
df110 = df102.copy()
df110 = df110.loc[(df110['Source (Filter)'] == top7)]
df110['预警时间'] = df110['预警时间'].str.slice(0,10)
df110= pd.DataFrame(df110.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df110 = df110.sort_values(by=['预警时间'])
ax = df110.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df110.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top7 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top7.png'.format(user,top7))
plt.close()


#Top 8 No. of Obstacle Detected Trend --> df111
top8 = df101.iloc[7]['Source']
df111 = df102.copy()
#df111 = df111.drop(columns =['Source','Obstacle Detected Count'],axis = 1 )
df111 = df111.loc[(df111['Source (Filter)'] == top8)]
df111['预警时间'] = df111['预警时间'].str.slice(0,10)
df111= pd.DataFrame(df111.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df111 = df111.sort_values(by=['预警时间'])
ax = df111.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df111.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top8 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top8.png'.format(user,top8))
plt.close()


#Top 9 No. of Obstacle Detected Trend --> df112
top9 = df101.iloc[8]['Source']
df112 = df102.copy()
df112 = df112.loc[(df112['Source (Filter)'] == top9)]
df112['预警时间'] = df112['预警时间'].str.slice(0,10)
df112= pd.DataFrame(df112.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df112 = df112.sort_values(by=['预警时间'])
ax = df112.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df112.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top9 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top9.png'.format(user,top9))
plt.close()


#Top 10 No. of Obstacle Detected Trend --> df113
top10 = df101.iloc[9]['Source']
df113 = df102.copy()
df113 = df113.loc[(df113['Source (Filter)'] == top10)]
df113['预警时间'] = df113['预警时间'].str.slice(0,10)
df113= pd.DataFrame(df113.groupby(['Source (Filter)','预警时间']).size(),columns=['Obstacle Detected Count']).reset_index()
df113 = df113.sort_values(by=['预警时间'])
ax = df113.plot.scatter(x= '预警时间', y= 'Obstacle Detected Count', style='b',figsize = (12,12))
ax.yaxis.get_major_locator().set_params(integer=True)
df113.plot.line(x= '预警时间', y='Obstacle Detected Count', ax=ax, style='b',rot=25)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(top10 +' '+ 'Obstacle Detected Trend')
#plt.savefig(r'C:\Users\{0}\Downloads\location\Obstacle_Detected\Top_Ten\Top_Ten_Trend\{1}_Top10.png'.format(user,top10))
plt.close()

# In[31]:


# Top Ten Obstacle Detected Trend Graphs (Group by Source (Filter ) & Occurring Time)  -->  df402
df402 = pd.concat([df104,df105,df106,df107,df108,df109,df110,df111,df112,df113],axis = 0)


# In[5]:


# Create a dashborad for Obstacle Detected Alarm 


# fig --> All Trainset Obstacle Detected Group Count Graph

fig = px.bar(df401,x='车组',
             y='Obstacle Detected Group Count',
             title = f'All Trainset Obstacle Detected Group Count',
             hover_name='车组')

# fig1 --> All Top Ten Obstacle Detected Trend Graph

fig1 = px.bar(df101,x='Source',
              y='Obstacle Detected Count',
              title = f'Top Ten Obstacle Detected Trend',
              hover_name='Source')


layout = html.Div([
    html.Div([html.Header("Obstacle Detected"),
    html.Div([dcc.Dropdown(id="mydropdown",
                 options = df102['Type'].unique(),
                 value = df102.iloc[0]['Type']),
    dcc.Graph(id = 'all_graphs')],className ='six columns'),
    html.Div([
        dcc.Graph(id = 'one_graph',figure = fig)],className= 'five columns'),],className = 'row'),
    html.Div([html.H2("Data", style={"textAlign":"center"}),
    html.Hr(),
    html.Div(id='table1',children = 'Excel'),],className='row'),
    html.H2("Trend", style={"textAlign":"center"}),
    html.Hr(),
    html.Div([dcc.Dropdown(id="mydropdown2",
              options = df101['Source'].unique(),
              value = df101.iloc[0]['Source']
            ),
    dcc.Graph(id = 'trend_graphs')],className ='six columns'),
    html.Div([
        dcc.Graph(id = 'top_ten_trend',figure = fig1)],className ='five columns'),
        
    ])
    
   

@app.callback(
    Output('all_graphs','figure'),
    Output('table1', 'children'),
    Input('mydropdown','value')
)


def sync_input(changes):

    filtered_data = df102.loc[df102['Type']==changes]
    filtered_data2 = df213.loc[df213['Type']==changes]
    a = filtered_data2.nlargest(n=1,columns=['Obstacle Detected Count'])
    a = a.iloc[0]['Source']
    fig_bar = px.bar(df213.loc[df213['Type']==changes],
                x='Source',
                y='Obstacle Detected Count',
                title =f'The Highest Obstacle Detected Train : {a}',
                hover_name = 'Source')
    
    filtered_data = filtered_data.drop(columns=['Type'],axis = 1)
    tb = html.Div([dash_table.DataTable(filtered_data.to_dict('records'), [{"name": i, "id": i} for i in filtered_data.columns],
                          editable = False,
                          filter_action = 'native',
                          sort_action = 'native',
                          sort_mode='multi',
                          page_action= 'native',
                          page_current = 0,
                          page_size = 10,                      
                          style_cell_conditional=[                              
                                       {'if': {'column_id': c},
                                        'textAlign': 'center'    
                                       } for c in ['Source (Filter)','预警时间']
                                
                          ],
                          style_data={
                                'color': 'white',
                                'backgroundColor': 'rgb(50, 50, 50)'
                          }, 
                          style_header={
                                'backgroundColor': 'rgb(30, 30, 30)',
                                'color': 'white',
                                'fontWeight': 'bold'
                                } )],className='twelve columns'),
    
    
    
    
    return fig_bar , tb


@app.callback(
    Output('trend_graphs','figure'),
    Input('mydropdown2','value')

)

def trend_input(changes):
    fil_data = df402.loc[df402['Source (Filter)']==changes]
    #filtered_data2 = df213.loc[df213['Type']==changes]

    fig = px.line(fil_data.loc[fil_data['Source (Filter)']==changes],
                x='预警时间',
                y='Obstacle Detected Count',
                title =f'Obtacle Detected Trend',
                hover_name = 'Source (Filter)',
                markers = True)
    
    return fig



# In[ ]:




