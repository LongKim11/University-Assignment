
# Task 1:

import numpy as np

def isPrime (n): # Function to check whether the number is prime number
  if n == 1:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2, n):
      if (n % i == 0):
        return False
    return True

def calSequence (value, n): # Function to return sequence value of question b
    res = value
    for i in range (1, n):
      res = np.dot(res, value)
    return res

def findMaxArr(a): # Function to return max value in array
  if len(a) == 0:
    return 0
  max = a[0]
  for ele in a:
    if ele > max:
      max = ele
  return max

print("Task 1:")

# Initialize matrix A, B and C regarding to essay's requirement
A = np.random.randint(1, 101, size = (10, 10)) 
B = np.random.randint(1, 21, size = (2, 10))
C = np.random.randint(1, 21, size = (10, 2))

# Question a:
a =  A + A.T + np.dot(C,B) + np.dot(B.T, C.T) 
print("a. ", a) 

print()

# Question b:
b = 0
for i in range (1, 11):
  temp = A / (i + 9)
  b += calSequence(temp, i)
print("b. ", b)

print()

# Question c:
c = A[0:10:2] # Know that odd rows start with index = 0 
print("c.", c)

print()

# Question d:
lst1 = []
for i in range (len(A)):
  for j in range (len(A[i])):
    if A[i][j] % 2 == 1:
      lst1.append(A[i][j])
d = np.array(lst1)
print("d. ", d)

print()

# Question e:
lst2 = []
for i in range(len(A)):
  for j in range(len(A[i])):
    if isPrime(A[i][j]):
      lst2.append(A[i][j])
e = np.array(lst2)
print("e. ", e)

print()

# Question f:
D = np.dot(C, B)
for i in range(0, len(D), 2): # Know that odd rows start with index = 0 
  for j in range(0, int(len(D[i]) / 2)):
    temp = D[i][j]
    D[i][j] = D[i][len(D[i]) - j - 1]
    D[i][len(D[i]) - j - 1] = temp
print("f. ", D)

print()

# Question g:
lst3 = []
for i in range(0, len(A)):
  count = 0
  for j in range(0, len(A[i])):
    if isPrime(A[i][j]): 
      count += 1
  lst3.append(count)
maxPrime = findMaxArr(lst3)
print("g. ", end = "")
for i in range (0, len(lst3)):
  if lst3[i] == maxPrime:
    print(A[i])

print()

# Question h:
lst4 = []
for i in range (0, len(A)):
  count = 0
  temp = []
  for j in range(0, len(A[i])):
    if A[i][j] % 2 == 1:
      count += 1
      if j == len(A[i]) - 1:
        temp.append(count)
    else:
      if(count > 0):
        temp.append(count)
      count = 0
  lst4.append(findMaxArr(temp))
maxContOdd = findMaxArr(lst4)
print("h. ", end = "")
for i in range(0, len(lst4)):
  if lst4[i] == maxContOdd:
    print(A[i])