from numpy import float16
import pandas as pd

#df = pd.read_excel('C://Users//ZAR//Drive//CalculadoraIPC//CalculadoraDeflactorIPC.xlsx', sheet_name='Indice', skiprows=1,)#.pivot(columns = 0,  values = 1)
#Lista = {col: df[col].dropna().tolist() for col in df.columns}


calcula_df = pd.read_excel('CalculadoraDeflactorIPC.xlsx')
print(calcula_df)

#print()
#df se file1
#file1 = file1.merge(file2[['columns', 'you', 'want', 'to','return']], how=’left’, on=’common-column-to-look-for’)
#df = df.merge(file2[['columns', 'you', 'want', 'to','return']], how=’left’, on=’common-column-to-look-for’)

#def calcula_df ('Anio_Mes', 'IndiceIPC')
   # Valor_resultado=
Fecha_inicio = input('Introduzca la fecha a consultar')
Fecha_termino = input('Introduzca la fecha término a consultar')
Valor_indicador = input('Introduzca el valor a calcular')

filaIni_df = calcula_df[calcula_df['Anio_Mes']==Fecha_inicio]
indicadorIni = float(filaIni_df['IndiceIPC'])

filaFin_df = calcula_df[calcula_df['Anio_Mes']==Fecha_termino]
indicadorFin = float(filaFin_df['IndiceIPC'])

def calcula(indicadorIni, indicadorFin, Valor_indicador):
    print("inicio", indicadorIni)
    print("fin", indicadorFin)
    print("Indica", Valor_indicador)
    indicadorIPC = float(Valor_indicador)*(indicadorFin/indicadorIni)*100
    
    print(indicadorIPC)
    return(indicadorIPC)

calcula(indicadorIni, indicadorFin, Valor_indicador)


#Valor_ajustado = df[['Valor calculado']==]

#https://www.youtube.com/watch?v=Oby3ksXd1oY&ab_channel=cctmexico



