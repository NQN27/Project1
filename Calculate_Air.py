import pandas as pd
import numpy as np
dl = pd.read_excel(r"Data\Location.xlsx")


from math import radians, sin, cos, sqrt, atan2
def haversine(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Calculate the distance
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # 6371 is the radius of the Earth in kilometers
    
    return distance


heuristic=[[0 for i in range(63)] for j in range(63)]
location=np.array(dl)[::,1:]
def Call():
    for l in location:
        str(l).split(',')

    for i in range(63):
        for j in range(63):
            if i!=j:
                p=str(location[i][0]).split(',')
                q=str(location[j][0]).split(',')
                heuristic[i][j]=haversine(float(p[0]),float(p[1]),float(q[0]),float(q[1]))
    df=pd.DataFrame(heuristic)
    df.to_excel(r"Data\Air_Distance1.xlsx", index= False, header=False)
            
