import pandas as pd

#df = pd.read_excel('C://Users//ZAR//Drive//CalculadoraIPC//CalculadoraDeflactorIPC.xlsx', sheet_name='Indice', skiprows=1,)#.pivot(columns = 0,  values = 1)
#Lista = {col: df[col].dropna().tolist() for col in df.columns}
df = pd.read_excel('CalculadoraDeflactorIPC.xlsx')
print(df)
#print()
#df se file1
#file1 = file1.merge(file2[['columns', 'you', 'want', 'to','return']], how=’left’, on=’common-column-to-look-for’)
#df = df.merge(file2[['columns', 'you', 'want', 'to','return']], how=’left’, on=’common-column-to-look-for’)
Fecha_inicio = input('Introduzca la fecha a consultar')
Fecha_termino = input('Introduzca la fecha término a consultar')
Valor_indicador = int(input('Introduzca el valor a calcular'))

Valor_ajustado = df[['Valor calculado']==]



#https://www.youtube.com/watch?v=Oby3ksXd1oY&ab_channel=cctmexico



