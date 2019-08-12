def SIBC(data, y, x_val, y_val):
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    neigh = KNeighborsClassifier(n_neighbors=2)
    neigh.fit(data, y)
    y_predict = neigh.predict(x_val)
    return accuracy_score(y_val, y_predict), neigh

def LogisticRegression(data, y, x_val, y_val):
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    neigh = LogisticRegression(random_state=0, solver='lbfgs').fit(data, y)
    y_predict = neigh.predict(x_val)
    return accuracy_score(y_val, y_predict)

def ridge(data, y, x_val, y_val):
    from sklearn import linear_model
    from sklearn.metrics import r2_score
    reg = linear_model.Ridge(alpha=.5)
    reg.fit(data, y)
    y_predict = reg.predict(x_val)
    return reg.score(x_val, y_val)

def lasso(data, y, x_val, y_val):
    from sklearn import linear_model
    reg = linear_model.Lasso(alpha=.1)
    reg.fit(data, y)
    print(reg.get_params())
    y_predict = reg.predict(x_val)
    return reg.score(x_val, y_val)

def elastic_net(data, y, x_val, y_val, i):
    from sklearn import linear_model
    reg = linear_model.ElasticNet(random_state = i)
    reg.fit(data, y)
    y_predict = reg.predict(x_val)
    return reg.score(x_val, y_val)

def linear_Regression(data, y, x_val, y_val):
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit(data, y)
    y_predict = reg.predict(x_val)
    print(reg.get_params(deep = False))
    return reg.score(x_val, y_val)