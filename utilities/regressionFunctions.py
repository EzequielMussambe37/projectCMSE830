from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
# def preprocessing():
import streamlit as st
def linear_regression(X,y,train_size=80,random_state = 23):
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=train_size,random_state=random_state)
    lin_reg = LinearRegression()
    # pipeline = Pipeline([
    # ('scaler', StandardScaler()), ('regression', LinearRegression())])
    #pipeline.fit(X_train,y_train)
    lin_reg.fit(X_train,y_train)
    return {"model": lin_reg,"X_test":X_test,"y_test":y_test,"X_train":X_train,"y_train":y_train}

def model_evaluation(result):
    y_predicted = result["model"].predict(result["X_test"])
    mse = mean_squared_error(y_predicted,result["y_test"])
    mae = mean_absolute_error(y_predicted,result["y_test"])
    r_squared = r2_score(result["y_test"],y_predicted)
    
    return {"mse":mse,"mae":mae,"r_squared":r_squared,"predicted":y_predicted} 
def construct_regression_table(model,columns):
    
    columns = ['intersect'] + columns
    parameter = ["w_"+ str(i) for i in range(0,len(columns))]
    w = [model.intercept_]+list(model.coef_)
    
    return {"Parameter":parameter,"Columns":columns,"Coeff_value":w}

def standardized_data(data):
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data

def normalized_data(data):
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    return data