import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def analisar_dados_rede(caminho_arquivo_log):
    try:
       
        df = pd.read_csv(caminho_arquivo_log)
    except FileNotFoundError:
        return "Arquivo de log não encontrado."

    
    df = df.dropna()

    
    dados_numericos = df.select_dtypes(include=np.number)

   
    modelo = IsolationForest(contamination=0.05, random_state=42)
    anomalias = modelo.fit_predict(dados_numericos)

   
    df['anomalia'] = anomalias

    
    anomalias_df = df[df['anomalia'] == -1]
    return anomalias_df


anomalias_detectadas = analisar_dados_rede("log_rede_exemplo.csv")


if isinstance(anomalias_detectadas, pd.DataFrame) and not anomalias_detectadas.empty:
    print("🚨 Anomalias detectadas:\n")
    print(anomalias_detectadas)
else:
    print("✅ Nenhuma anomalia detectada ou erro ao carregar o arquivo.")
