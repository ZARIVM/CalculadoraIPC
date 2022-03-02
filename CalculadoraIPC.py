import pandas as pd

df = pd.read_excel('C://Users//ZAR//Drive//CalculadoraIPC//CalculadoraDeflactorIPC.xlsx', sheet_name='Indice', skiprows=1,)#.pivot(columns = 0,  values = 1)
#Lista = {col: df[col].dropna().tolist() for col in df.columns}

print(df)
#print()

