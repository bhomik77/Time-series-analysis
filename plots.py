import matplotlib.pyplot as plt



def plot_this(x, y, column_name):
    a = x
    a = pd.DataFrame(a)
    a[column_name] = y
    a.Date = pd.to_datetime(a.Date)
    a.set_index('Date', inplace=True)

    a.plot(figsize=(10,5), linewidth=5, fontsize=20)
    plt.xlabel('Year', fontsize=20);
    
    