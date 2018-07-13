import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

pd.set_option('display.max_columns',20)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',10)

def main():

    df = pd.read_csv(r'C:\Users\Mitch\Projects\Golf\Data\full_data.csv',encoding='latin1')

    corr_mat = df.corr()
    corr_mat.columns = [f[0:4] for f in corr_mat.columns]
    print(corr_mat)
    
    #Everything broke because you cahnged the format of the input data. For shame.
    #x = ndf[features[1:]]
    #x = np.asarray(x).reshape(x.shape[0],x.shape[1])
    #y = ndf[features[0]]
    #y = np.asarray(y).reshape(y.shape[0],1)

    #linreg = linear_model.LinearRegression()
    #linreg.fit(x,y)

    #pred = linreg.predict(x)
    #residuals = pred - y
   
    #print(np.mean(residuals))
    #print(np.std(residuals))
    #print(np.histogram(residuals))
    
    #mse = mean_squared_error(test_y, pred)
    #print(linreg.intercept_,linreg.coef_,mse)

if __name__=="__main__":
    main()
