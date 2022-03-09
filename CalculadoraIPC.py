from numpy import float16
import pandas as pd

calcula_df = pd.read_excel('CalculadoraDeflactorIPC.xlsx')
#print(calcula_df)

Fecha_inicio = input('Introduzca la fecha inicial a consultar')
Fecha_termino = input('Introduzca la fecha término a consultar')
Valor_calcular = input('Introduzca el valor a calcular')

filaIni_df = calcula_df[calcula_df['Anio_Mes']==Fecha_inicio]
indicadorIni = float(filaIni_df['IndiceIPC'])

filaFin_df = calcula_df[calcula_df['Anio_Mes']==Fecha_termino]
indicadorFin = float(filaFin_df['IndiceIPC'])

def calcula(indicadorIni, indicadorFin, Valor_calcular):
    print("Indicador de la fecha de inicio", indicadorIni)
    print("Indicador de la fecha final", indicadorFin)
    print("Valor a calcular", Valor_calcular)
    indicadorIPC = float(Valor_calcular)*(indicadorFin/indicadorIni)*100
    
    print("El valor equivalente a la fecha final es:", indicadorIPC)
    return(indicadorIPC)

calcula(indicadorIni, indicadorFin, Valor_calcular)



