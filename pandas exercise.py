import pandas as pd
import numpy as np

#Create First DataFrame
data = {'producto' : ['A','B','C','D','E'],
        'ventas' :[100,150,80,120,200],
        'precio' : [10,12,8,15,11]}
df = pd.DataFrame(data)
print(df)

#Filter for B
productoB = df[df.producto=='B']
productoB

#Add Cost Column
coste = [3,4,6,2,7]
df['coste'] = coste
df

#Calculate Benefit
df['beneficio'] = df['ventas'] * df['precio'] - df['coste']
df
