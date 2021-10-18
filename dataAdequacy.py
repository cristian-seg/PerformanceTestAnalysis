import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def dataAdequacy(path):
    try:
        file = pd.read_excel(path)
        df = pd.DataFrame(file)

        #se eliminan columnas
        df=df.drop(['timeStamp','label','responseMessage', 'dataType', 'URL', 'IdleTime', 'failureMessage','grpThreads', 'threadName'], axis=1)
        
        #Se cambia True a 1 y False a 0
        success_dict = {True:1,False:0}
        df = df.applymap(lambda s: success_dict.get(s) if s in success_dict else s)
        df[["success"]] = df[["success"]].apply(pd.to_numeric)

        #Renombramos las columnas
        df = df.rename(columns={'elapsed':'VO','responseCode':'V1','success':'V2','bytes':'V3','sentBytes':'V4','allThreads':'V5', 'Latency':'V6','Connect':'V7','Result':'V8'})

        #Normalización de datos
        columnas = ['V0','V1','V2','V3','V4','V5','V6','V7','V8']
        scaler = MinMaxScaler()
        df_norm = scaler.fit_transform(df.iloc[:, :9])
        df_norm = pd.DataFrame(df_norm, columns=columnas)

        #División de datos
        X = df_norm.iloc[:,0:8]
        Y = df_norm.iloc[:,8:]

        #Divisón de datos para entreno y testeo
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.75,
                                                random_state = 1324,
                                                shuffle      = True
        )

        print ( "Los datos fueron adecuados con exito")
        return X_train, X_test, y_train, y_test
    except:
        print("An error occurred while preparing the input data. ")
 
