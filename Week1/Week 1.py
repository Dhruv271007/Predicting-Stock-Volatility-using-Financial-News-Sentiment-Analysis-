import pandas as pd
import numpy as np
df=pd.read_csv('stockdatamock.csv')
df['Daily Return']=(df['Close']-df['Open'])/df['Open']
print(df)