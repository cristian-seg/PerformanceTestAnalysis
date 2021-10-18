#from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from dataAdequacy import dataAdequacy
import pickle
import sys
import os
from sklearn.metrics import accuracy_score
import pandas as pd

#Entrenamiento del Modelo
def train():
    try:
        #train test split
        path = './resources/data.xlsx'
        X_train, X_test, y_train, y_test = dataAdequacy(path)
        #modelo = KNeighborsClassifier(n_neighbors=3)
        #knn= modelo.fit(X_train,y_train) # fitting the data
        modelo = RandomForestClassifier(n_estimators= 20)
        rndmForest=modelo.fit(X_train, y_train)

        #y_pred = modelo.predict(X_test)
        
        print ("El modelo fue enrenado con exito")
        #Save Model As Pickle File
        with open('rndmForest.pkl','wb') as m:
            pickle.dump(rndmForest,m)
        print("El modelo fue almacenado con Exito")

        test(X_test,y_test)
    except:
        print("An error occurred while training the model ")

def test(X_test,Y_test):
    try:
        with open('rndmForest.pkl','rb') as mod:
            p=pickle.load(mod)
        pre=p.predict(X_test)
        print (accuracy_score(Y_test,pre)) #Prints the accuracy of the model
    except:
        print("An error occurred testing the model ")

def find_data_file(filename):
    try:
        if getattr(sys, "frozen", False):
            # The application is frozen.
            datadir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen.
            datadir = os.path.dirname(__file__)
        return os.path.join(datadir, filename)
    except:
        print("An error occurred searching for the trained model ")

def check_input(data) ->int :
    try:
        df=pd.DataFrame(data=data,index=[0])
        with open(find_data_file('rndmForest.pkl'),'rb') as model:
            p=pickle.load(model)
        op=p.predict(df)
        return op[0]
    except:
        print("An error occurred predicting the input data ")

if __name__=='__main__':
    train() 
