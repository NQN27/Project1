from Calculate_Air import haversine,location
import test_class
import requests
import json
from test_class import encode
from Calculate_RealDistance import locations,transform
matrix = test_class.matrix
name = test_class.name
import Code_interface 


def transform_place_to_location(place):

    key='sd78W6yR6ms16xXUF76C6RD2OpQgaPrKgBCen66O'
    url = "https://rsapi.goong.io/geocode?address={}&api_key={}".format(place,key)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data=json.loads(response.text)
    
    lat=data['results'][0]['geometry']['location']['lat']
    lng=data['results'][0]['geometry']['location']['lng']
    return str('{},{}').format(lat,lng)


def get_place(place):
    Chosen_place=[]
    r_place=place.split(',')
    for i in range(len(name)):
            p=str(location[i][0]).split(',')
            dis=haversine(float(r_place[0]),float(r_place[1]),float(p[0]),float(p[1]))
            if dis<=50:
                Chosen_place.append(name[i])
    return Chosen_place

def get_distance(start,finish):

    key='sd78W6yR6ms16xXUF76C6RD2OpQgaPrKgBCen66O'
    url = "https://rsapi.goong.io/DistanceMatrix?origins={}&destinations={}&vehicle=car&api_key={}".format(start,finish,key)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data=json.loads(response.text)
    
    dist=data['rows'][0]['elements'][0]['distance']['value']/1000
    truetime=data['rows'][0]['elements'][0]['duration']['value']
    return [dist,truetime]
if __name__ == '__main__':
    start_point,end_point,type_input=Code_interface.Call_interface()

    if type_input == 1:
        start_place=transform_place_to_location(start_point)
        end_place=transform_place_to_location(end_point)
    else:
        start_place=start_point
        end_place=end_point
        
    Chosen_start=get_place(start_place)

    Chosen_end=get_place(end_place)   

    min=1e9
    for start in Chosen_start:
        for end in Chosen_end:
            p,s=test_class.A_star_search(encode(end), encode(start))
            p=p + get_distance(start_place, transform(start))[0] + get_distance(end_place, transform(end))[0]
            if min>p:
                min=p            
                way=s
                
    print(min) 
    print(start_point, end='->')
    for i in s:
        print(i, end='->')  
    print(end_point)          
