import math
import pandas as pd
from operator import itemgetter
from html_parser import similar

pd.set_option('display.max_columns',20)
#pd.set_option('display.max_rows',100000)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',25)

def lat_sim(row):
    print(row['Course'])

def main():
    
    #Order
    #Read in CSVs
    #Match rows to geodata
    #Add geodata to rows w/null values via similar()
    #Separate into individual rounds
    #Ship
    df = pd.read_csv(r'C:\Users\Mitch\Projects\Golf\Data\golfers.csv',index_col='Unnamed: 0',encoding='latin1')
    df.columns = ['Golfer','Tournament','Course','Date 1','Score 1','Date 2','Score 2','Date 3','Score 3','Date 4','Score 4']
    df1 = df[['Golfer','Tournament','Course','Date 1','Score 1']]
    df2 = df[['Golfer','Tournament','Course','Date 2','Score 2']]
    df3 = df[['Golfer','Tournament','Course','Date 3','Score 3']]
    df4 = df[['Golfer','Tournament','Course','Date 4','Score 4']]
    df1.columns = df2.columns = df3.columns = df4.columns = ['Golfer','Tournament','Course','Date','Score']
    df = pd.concat([df1,df2,df3,df4])
    df = df.reset_index(drop=True)
    df.to_csv(r'C:\Users\Mitch\Projects\Golf\Data\individual_rounds.csv',index=False)

    cdf = pd.read_csv(r'C:\Users\Mitch\Projects\Golf\Data\Courses.csv', index_col = 'Unnamed: 0')
    cdf = cdf[['Course Name','Latitude','Longitude']]
    cdf.columns = ['Course','Latitude','Longitude']
    mdf = df.merge(cdf,how='outer',on=['Course'])
    mdf = mdf.reset_index(drop=True)

    tdf = pd.read_csv(r'C:\Users\Mitch\Projects\Golf\Data\timezones.csv',index_col='Unnamed: 0',encoding='latin1')
    tdf.columns = ['Latitude','Longitude','Region','Timezone','To UTC']
    
    ndf = mdf.merge(tdf,how='outer',on=['Latitude','Longitude'])
    ndf = ndf.drop(['Region'],axis=1)

    null_df = df[df['Latitude'].isnull()]
    null_df.apply(lambda row: lat_sim(row),axis=1)
    #df['Latitude'] = df.apply(lambda row: temp_fun(row))
    #df['Longitude'] = df.apply(lambda row: temp_fun(row))
    #df['Timezone'] = df.apply(lambda row: temp_fun(row))
    #df['To UTC'] = df.apply(lambda row: temp_fun(row))

if __name__=="__main__":
    main()
