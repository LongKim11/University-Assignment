from tabulate import tabulate
from itertools import combinations 

"""
Variables declared below are global one
"""

file = open('input2.txt')

RDB = {} # Store relational database scheme
FD = {} # Store function dependency
key_dic = {} # Store key of relation diagram

# Read line by line in file
for line in file:
    components = line.split()

    if len(components) == 2:
        table = components[0]
        field = components[1][1: len(components[1]) - 1]
        
        RDB[table] = field

    elif len(components) == 3:
        X = components[0]
        Y = components[2]

        FD[X] = Y

# Algorithm for finding closure of X attribute set
def findClosureHelper (X, track): 
    closure = X
    for keys in FD.keys():

        if ',' in keys:
            left_side = keys.split(',')
            check = True
            for attribute in left_side:
                if attribute not in closure:
                    check = False
                    break
            if check and keys not in track:
                track[keys] = True
                attribute_set = FD.get(keys).split(',')
                for attribute in attribute_set:
                    if attribute not in closure:
                        closure += ',' + attribute 
        else:
            if keys in closure and keys not in track:
                track[keys] = True
                attribute_set = FD.get(keys).split(',')
                for attribute in attribute_set:
                    if attribute not in closure:
                        closure += ',' + attribute 

    if (closure != X):
        closure = findClosureHelper(closure, track)
    return closure

def findClosure(X):
    track = {}
    return findClosureHelper(X, track)

# Algorithm for find key of relational diagram
# Base on its function dependency
def findKey():
    relation = RDB.keys()
    
    for R in relation:
        U = RDB.get(R).split(',')
        U_left = ''
        U_right = ''

        for k in FD.keys():
            if ',' in k:
                k_single = k.split(',')
                check = True

                for ele in k_single:
                    if ele not in U:
                        check = False
                        break 

                if check:
                    U_left = k_single
                    U_right = FD.get(k).split(',')

            elif k in U:
                U_left = k.split(',')
                U_right = FD.get(k).split(',')
        
        N = ''       
        for i in range(len(U)):
            if U[i] not in U_right:
                N += U[i] + ','
        N = N[0:len(N) - 1]
        N_closure = findClosure(N).split(',')

        check = True
        for attribute in U:
            if attribute not in N_closure:
                check = False 
        
        if check:
            key_dic[R] = N 
        else:
            D = []
            for attribute in U_right:
                if attribute not in U_left:
                    D.append(attribute)

            L = []
            for attribute in U:
                if attribute not in D and attribute not in N:
                    L.append(attribute)
            
            i = 1
            while(len(L) >= i):
                attribute_set = combinations(L, i)
                for attribute in attribute_set:
                    X_i = N + ',' + attribute
                    X_i_closure = findClosure(X_i)
                    attribute_remove = []

                    if (set(X_i_closure) == set(U)):
                        key_dic[R] = X_i 
                        attribute_remove.append(attribute)
                    
                    if (len(attribute_remove) > 0):
                        for attribute in attribute_remove:
                            L.remove(attribute)

file.close()

"""
Main function start from here
Below statements are used for writing data to output file
"""

X = input('Enter X: ')
X_closure = [[X, findClosure(X)]]

findKey()

output = open('output2.txt', 'w', encoding = 'utf8')

output.write(tabulate(X_closure, headers = ['TẬP THUỘC TÍNH X', 'BAO ĐÓNG CỦA X'], tablefmt = 'simple_grid'))
output.write('\n\n')

fmt_key_dic = []
for k in key_dic:
    fmt_key_dic.append([k, key_dic.get(k)])

output.write(tabulate(fmt_key_dic, headers = ['LƯỢC ĐỒ QUAN HỆ', 'KHÓA'], tablefmt = 'simple_grid'))
output.write('\n\n')

output.close()



