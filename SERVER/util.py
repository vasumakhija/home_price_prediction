import json
import pickle
import numpy as np


__location=None
__data_colunms=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
        
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)
        

def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    global __model

    with open("C:/Users/vasum/Desktop/projects_BHK/SERVER/aartifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open("C:/Users/vasum/Desktop/projects_BHK/SERVER/aartifacts/bangalore_home_Price_model.pickle", 'rb') as g:
        __model = pickle.load(g)
    print("loading saved artifacts...done")
    
    
load_saved_artifacts()
    
if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())  
    print(get_estimated_price('1st block jayanagar',1000,3,3))
    print(get_estimated_price('1st block jayanagar',1000,2,2))
    print(get_estimated_price('anandapura',1000,3,3))
    print(get_estimated_price('ananth nagar',1000,3,3))