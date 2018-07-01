import pandas as pd
from operator import itemgetter

pd.set_option('display.max_columns',20)
pd.set_option('display.width',1000)

def main():

    df = pd.read_csv(r'C:\Users\Mitch\Projects\Golf\Data\golfers.csv', index_col='Unnamed: 0', encoding = 'latin1')
    df.columns = ['Golfer','Tournament','Course','Date 1','Score 1','Date 2','Score 2','Date 3','Score 3','Date 4','Score 4']
    df1 = df[['Golfer','Tournament','Course','Date 1','Score 1']]
    df2 = df[['Golfer','Tournament','Course','Date 2','Score 2']]
    df3 = df[['Golfer','Tournament','Course','Date 3','Score 3']]
    df4 = df[['Golfer','Tournament','Course','Date 4','Score 4']]
    df1.columns = df2.columns = df3.columns = df4.columns = ['Golfer','Tournament','Course','Date','Score']
    df = pd.concat([df1,df2,df3,df4])
    df = df.reset_index(drop=True)
    print(df)
    
if __name__=="__main__":
    main()

