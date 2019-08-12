import pandas as pd
import numpy as np
from plots import *
from stationary_check import *
from models import *
data = pd.read_csv("Book1.csv")

data['REER_percent'] = (data['REER'] - data['REER'].shift(-1))/data["REER"]    # it is for converting REER and M3 into percentage
data['M3_percent'] = (data['M3'] - data['M3'].shift(-1))/data["M3"]        # as all the data available is in percentage
del data["REER"]
del data["M3"]

avg = 0
count = 0
for i in range(len(data)):                      # we took average of market value for checking if we should invest or not
    avg = avg + data['Return(%)'][i]
    count += 1
avg = avg/count

y = []
count = 0
for i in range(len(data)):
    if data['Return(%)'][i] >= avg:              # making y '0' for not investing '1' for investing
        y.append(1)
        count += 1
    else:
        y.append(0)
        
for i in range(len(data)):
    data['Date'][i] = data['Date'][i] + '-' + str(20)
        
for i in range(len(data)):
    data['Crude Oil price'][i] = data['Crude Oil price'][i].replace(",", "")     # coverting crude oil data in float
    data['Crude Oil price'][i] = float(data['Crude Oil price'][i])                 
    
for name in data2.columns:
    if name != 'Date':
        l = data2[name]
        adf_test(x, l, name)
        plot_this(x, l, name)
        
# after checking we got some variable as stationary and some as non stationary.
# non stationary variables are: "M3_percent"
#                               "CPI"
#                               "GIP"
#                               "Crude Oil price"
#                               "Interest rate"

# Making the non stationary variable stationary using difference method.
data2['CPI_diff'] = data2['CPI'] - data2['CPI'].shift(1)
data2['GIP_diff'] = data2['GIP'] - data2['GIP'].shift(1)
data2['Crude Oil price_diff'] = data2['Crude Oil price'] - data2['Crude Oil price'].shift(1)
data2['Interest rate_diff'] = data2['Interest rate'] - data2['Interest rate'].shift(1)
data2['M3_diff'] = data2['M3_percent'] - data2['M3_percent'].shift(1)


data2 = data2.iloc[1:]

del data2["M3_percent"]
del data2["CPI"]
del data2["GIP"]
del data2["Crude Oil price"]
del data2["Interest rate"]


for name in data2.columns:
    if name != 'Date':
        l = data2[name]
        adf_test(x, l, name)
        plot_this(x, l, name)
        
# we again checked the updated variables it was coming stationary at 10% critical value

y = y[1:,:]
final = np.concatenate((data2,y), axis = 0)
final.to_csv('file.csv')
