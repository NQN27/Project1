import pandas as pd
import numpy as np
import requests
import json

df = pd.read_excel(r'Data\Car_Driving.xlsx')
dh = pd.read_excel(r'Data\Air_Distance1.xlsx') 
dl = pd.read_excel(r'Data\Location.xlsx')
name = matrix = np.array(df)[::,0] #Get file name of City
matrix = np.array(df)[::,1:]
location=np.array(dl)[::,1:] #Remove the index
heuristic = np.array(dh)[::,1:]
locations=np.array(dl)[::,::]
def transform(name):
    for city in locations:
        if name in city:
            return city[1]
def transform_matrix(name):
    for city in locations:
        if name in city:
            return city[1].split(',')

distance=[[0 for i in range(63)] for j in range(63)]
timeTravel=[[0 for i in range(63)] for j in range(63)]
if __name__ == '__main__':
    for i in range(63):
        for j in range(63):
            if matrix[i][j]!=0:
                key='sd78W6yR6ms16xXUF76C6RD2OpQgaPrKgBCen66O'
                if i<j:
                    start=location[j][0]
                    finish=location[i][0]
                else:
                    start=location[i][0]
                    finish=location[j][0]
                url = "https://rsapi.goong.io/DistanceMatrix?origins={}&destinations={}&vehicle=car&api_key={}".format(start,finish,key)

                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)
                data=json.loads(response.text)

                dist=data['rows'][0]['elements'][0]['distance']['value']
                truetime=data['rows'][0]['elements'][0]['duration']['value']
                distance[i][j]=dist
                timeTravel[i][j]=truetime
    df=pd.DataFrame(distance)
    dt=pd.DataFrame(timeTravel)
    df.to_excel(r'Data\Car_Driving.xlsx', index= False, header=False)
    dt.to_excel(r'Data\TimeTravel.xlsx', index= False, header=False)
