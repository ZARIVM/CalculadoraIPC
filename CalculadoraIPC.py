import pandas as pd

df = pd.read_excel('C://Users//ZAR//Drive//CalculadoraIPC//CalculadoraDeflactorIPC.xlsx', sheet_name='Indice', skiprows=1,)#.pivot(columns = 0,  values = 1)
#Lista = {col: df[col].dropna().tolist() for col in df.columns}
file2 = 20/20/20

print(df)
#print()
#df se file1
#file1 = file1.merge(file2[['columns', 'you', 'want', 'to','return']], how=’left’, on=’common-column-to-look-for’)
df = df.merge(file2[['columns', 'you', 'want', 'to','return']], how=’left’, on=’common-column-to-look-for’)