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

if __name__ == "__main__":
    count = 0
    for i in range(63):
        for j in range(63):

            t1 = time.time()
            answer = uniform_cost_search(i,j)
            t2 = time.time()
            answer_a = A_star_search(i, j)
            t3 = time.time()
            if (t3-t2>t2-t1):
                count+=1
    print(count,' in ',63*63,'case')
