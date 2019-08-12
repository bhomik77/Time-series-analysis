from statsmodels.tsa.stattools import adfuller
def adf_test(x, l, column_name):
    #Perform Dickey-Fuller test:
    print(column_name)
    timeseries = l
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    a = dfoutput
    if a[0] >= a[4]:
        print(column_name, "is not staionary for critical value 1%")
    else:
        print(column_name, "is stationary for critical value 1%")
    if a[0] >= a[5]:
        print(column_name, "is not staionary for critical value 5%")
    else:
        print(column_name, "is stationary for critical value 5%")
    if a[0] >= a[6]:
        print(column_name, "is not staionary for critical value 10%")
    else:
        print(column_name, "is stationary for critical value 10%")
        
    