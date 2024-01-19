import pandas as pd
import numpy as np
import time
from queue import PriorityQueue

class city(object):
    def __init__(self, id, using_ucs = True):
        self.id = id
        self.name = decode(id)
        
        self.ucs_cost = None
        self.a_star_cost = None
        self.path = []
        self.using_ucs = using_ucs
    
    def __eq__(self, other):
        if self.using_ucs == True: # using ucs
            return self.ucs_cost == other.ucs_cost 
        # using a*
        return self.a_star_cost == other.a_star_cost

    def __lt__(self, other):
        if self.using_ucs == True: # using ucs
            return self.ucs_cost < other.ucs_cost 
        # using a*
        return self.a_star_cost < other.a_star_cost
    def __le__(self, other):
        if self.using_ucs == True: # using ucs
            return self.ucs_cost <= other.ucs_cost 
        # using a*
        return self.a_star_cost <= other.a_star_cost
    
    def __gt__(self, other):
        if self.using_ucs == True: # using ucs
            return self.ucs_cost > other.ucs_cost 
        # using a*
        return self.a_star_cost > other.a_star_cost

    def __ge__(self, other):
        if self.using_ucs == True: # using ucs
            return self.ucs_cost >= other.ucs_cost 
        # using a*
        return self.a_star_cost >= other.a_star_cost
    
    def __str__(self):
        str = ''
        for i in self.path:
            str = str + i + '-'
        return str

    def adjacent_city(self, matrix):
        adjacent = []
        for i in range(len(matrix[self.id])):
                if matrix[self.id][i] != 0:
                    adjacent.append(i)
        return adjacent


def uniform_cost_search(goal, start):
    global expanded_routes_U, expanded_nodes_U

    q = PriorityQueue()
    
    p = city(start)
    p.ucs_cost = 0
    p.path = [p.name]
    q.put(p)
    visited = [] #mark by list

    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            return p.ucs_cost, p.path
        
        if (p.name not in visited):
            for c in p.adjacent_city(matrix):
                p1 = city(c)
                p1.ucs_cost = p.ucs_cost + matrix[p.id][c]
                p1.path = p.path + [p1.name]
                q.put(p1)
                
                expanded_routes_U.append(p1) #for drawing nodes and routes
                if p1.name in expanded_nodes_U:
                    expanded_nodes_U[p1.name] = expanded_nodes_U[p1.name] + 1
                else:
                    expanded_nodes_U[p1.name] = 0 
        
        visited.append(p.name)
    return None

def A_star_search(goal, start):
    global expanded_routes_A1, expanded_nodes_A1
    q = PriorityQueue()
    p = city(start, using_ucs = False)
    p.ucs_cost = 0
    p.a_star_cost = 0
    p.path = [p.name]
    q.put(p)
    visited = [] 
    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            return p.ucs_cost, p.path
                
        if (p.name not in visited):
            for c in p.adjacent_city(matrix):
                p1 = city(c, using_ucs = False)
                p1.ucs_cost = p.ucs_cost + matrix[p.id][c]
                p1.a_star_cost = p1.ucs_cost + heuristic[p1.id][goal]
                p1.path = p.path + [p1.name]
                q.put(p1)

                expanded_routes_A1.append(p1) #for drawing nodes and routes
                if p1.name in expanded_nodes_A1:
                    expanded_nodes_A1[p1.name] = expanded_nodes_A1[p1.name] + 1
                else:
                    expanded_nodes_A1[p1.name] = 0 

        visited.append(p.name)
    return None

def A_star_search2(goal, start):
    global expanded_routes_A2, expanded_nodes_A2
    q = PriorityQueue()
    p = city(start, using_ucs = False)
    p.ucs_cost = 0
    p.a_star_cost = 0
    p.path = [p.name]
    q.put(p)
    visited = [] 
    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            return p.ucs_cost, p.path
                
        if (p.name not in visited):
            for c in p.adjacent_city(matrix):
                p1 = city(c, using_ucs = False)
                p1.ucs_cost = p.ucs_cost + matrix[p.id][c]
                p1.a_star_cost = p1.ucs_cost + 2*heuristic[p1.id][goal]
                p1.path = p.path + [p1.name]
                q.put(p1)

                expanded_routes_A2.append(p1) #for drawing nodes and routes
                if p1.name in expanded_nodes_A2:
                    expanded_nodes_A2[p1.name] = expanded_nodes_A2[p1.name] + 1
                else:
                    expanded_nodes_A2[p1.name] = 0 

        visited.append(p.name)
    return None

def uniform_cost_search_time(goal, start):
    q = PriorityQueue()
    
    p = city(start)
    p.ucs_cost = 0

    q.put(p)
    visited = [] #mark by list

    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            path = p.path + [p.name]
            return p.ucs_cost, path
        
        if (p.name not in visited):
            for c in p.adjacent_city(time_matrix):
                p1 = city(c)
                p1.ucs_cost = p.ucs_cost + time_matrix[p.id][c]
                p1.path = p.path + [p.name]
                q.put(p1)
        
        visited.append(p.name)
    return None
def A_star_plus_search(goal, start):
    global expanded_routes_A3, expanded_nodes_A3
    q = PriorityQueue()
    p = city(start, using_ucs = False)
    p.ucs_cost = 0
    p.a_star_cost = 0
    p.path = [p.name]
    q.put(p)
    visited = [] 
    while not q.empty():
        #p is the best node found
        p = q.get()

        if (p.id == goal):
            return p.ucs_cost, p.path
                
        if (p.name not in visited):
            for c in p.adjacent_city(matrix):
                p1 = city(c, using_ucs = False)
                p1.ucs_cost = p.ucs_cost + matrix[p.id][c]
                if heuristic[p1.id][goal]>=0.8*heuristic[start][goal]:
                    p1.a_star_cost = p1.ucs_cost + heuristic[p1.id][goal]
                elif heuristic[p1.id][goal]>=0.6*heuristic[start][goal]:
                    p1.a_star_cost = p1.ucs_cost + heuristic[p1.id][goal]*0.7
                else:
                    p1.a_star_cost = p1.ucs_cost + heuristic[p1.id][goal]*0.4
                p1.path = p.path + [p1.name]
                q.put(p1)

                expanded_routes_A3.append(p1) #for drawing nodes and routes
                if p1.name in expanded_nodes_A3:
                    expanded_nodes_A3[p1.name] = expanded_nodes_A3[p1.name] + 1
                else:
                    expanded_nodes_A3[p1.name] = 0 

        visited.append(p.name)
    return None
def decode(n): 
    global name
    return str(name[n])

def encode(str):
    for i in range(len(name)):
        if name[i] == str:
            return i
    return None



df = pd.read_excel(r"Data\Car_Driving.xlsx")
df2 = pd.read_excel(r"Data\Air_Distance1.xlsx")
df3 = pd.read_excel(r"Data\TimeTravel.xlsx")
heuristic = np.array(df2)[::,1:]
name = np.array(df)[::,0]
matrix = np.array(df)[::,1:]/1000
time_matrix = np.array(df3)[::,1:]

expanded_nodes_U = dict()
expanded_routes_U = []
expanded_nodes_A1 = dict()
expanded_routes_A1 = []
expanded_nodes_A2 = dict()
expanded_routes_A2 = []
expanded_nodes_A3=dict()
expanded_routes_A3 = []
if __name__ == "__main__":
    while True:
        start = input('START?')
        goal = input('GOAL?')
        if (start in name) and (goal in name):
            break
    t1 = time.time()
    answer = uniform_cost_search(encode(goal),encode(start))
    t2 = time.time()
    answer_a = A_star_search(encode(goal), encode(start))
    t3 = time.time()
    answer_time = uniform_cost_search_time(encode(goal), encode(start))
    t4 = time.time()
    answer_a_plus = A_star_plus_search(encode(goal), encode(start))
    t5 = time.time()

    if answer == None: #if dont have any solutions
        print('no solution')
    else:	
        solution = answer[0]
        path = answer[1]
        print('ucs minimum cost from {} to {} is {}'.format(start,goal,solution))
        print('path :')
        for i in path:
            print(i, end='->')
        print('RUNNING TIME UCS SEARCH')
        print("--- %s seconds ---" % (t2 - t1))
        print('UCS* nodes opened: ',expanded_nodes_U)
        print('total = ',sum(expanded_nodes_U.values()),' nodes')
        print('UCS* number of routes : ',len(expanded_routes_U))
    print()
    if answer_a == None: #if dont have any solutions
        print('no solution')

    else:	
        solution = answer_a[0]
        path = answer_a[1]
        print('a* minimum cost from {} to {} is {}'.format(start,goal,solution))
        print('path :')
        for i in path:
            print(i, end='->')        
        print('RUNNING TIME A* SEARCH')
        print("--- %s seconds ---" % (t3 - t2))
        print('A* nodes opened: ',expanded_nodes_A1)
        print('total = ',sum(expanded_nodes_A1.values()),' nodes')
        print('A* number of routes : ',len(expanded_routes_A1))
    print()

    if answer_time == None: #if dont have any solutions
        print('no solution')

    else:	
        solution = answer_time[0]
        path = answer_time[1]
        print('ucs minimum time taken from {} to {} is {}'.format(start,goal,solution))
        print('path :')
        for i in path:
            print(i, end='->')        
        print('RUNNING TIME UCS SEARCH (on time matrix)')
        print("--- %s seconds ---" % (t4 - t3))
