import pandas as pd
from functools import reduce
data={'numbers':[1,2,3,4,5,6],
      'letters':['a','b','c','d','e','f']}
df=pd.DataFrame(data)
sq=df['numbers'].map(lambda x:x**2)
ev=list(filter(lambda x:x%2==0,df['numbers']))
po=reduce(lambda x,y:x*y,df['numbers'])
print("dataframe\n",df)
print("map\n",sq)
print("reduce\n",po)
print("filtering\n",ev)