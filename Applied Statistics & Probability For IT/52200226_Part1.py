"""
Source code of Part 1
Demonstrate the usage of all functions in Python Statistics library
"""

# Importing the statistics module
import statistics 

# Importing the fractions module
from fractions import Fraction

# Function 1: statistics.mean(data)
"""
Calculate the average of the given dataset
"""

list1 = [1, 9, 3, 6, 8, 4, 2, 5]
tuple1 = (-1, 6, -11, 2, 9, 8, -5, 7)
fraction1 = (Fraction(1, 6), Fraction(3, 4), Fraction (2, 5), Fraction(6, 5), Fraction (4, 10))
dictionary1 = {4: 'num1', 9: 'num2', 3: 'num3', 7: 'num4', 11: 'num5'}

m1 = statistics.mean(list1) # Input parameter can be a list 
m2 = statistics.mean(tuple1) # or tuple 
m3 = statistics.mean(fraction1) # or fraction 
m4 = statistics.mean(dictionary1) # or dictionary

# Output value is in Float or Fraction data type
print('Mean from list =', m1) 
print('Mean from tuple =', m2)
print('Mean from fraction =', m3)
print('Mean from dictionary =', m4)


# Function 2: statistics.fmean(data, weights = None)
"""
Calculate the average like mean() function 
But faster because of converting all input data in float values 
and optional weighting is supported 
"""

list2 = [4.6, 1.2, 9, 11, -2, 7.8, 3, 6] # First input parameter is the same with Function 1
tuple2 = (-9, 11, 13.5, -20, 7, 16 )

fees = [100, 80, 76, 82, 120] 
weights = [0.35, 0.15, 0.2, 0.2, 0.1] # But weights for each corresponding data is supported

fm1 = statistics.fmean(list2) 
fm2 = statistics.fmean(fees, weights)
fm3 = statistics.fmean(tuple2)

print('Fmean from list =', fm1)
print('Fmean from fees with weigths', fm2)
print('Fmean from tuple =', fm3)


# Function 3: statistics.geometric_mean (data)
"""
Calculate same as average but different from formula by using 
product of all elements and then root by numbers of elements
"""

list3 = [7, 11, 22, 5, 17, 14] # Elements must be positive value
gmean1 = statistics.geometric_mean(list3)

print('Geometric mean from list1 = ', gmean1)

wrong_list = [-2, 6, 5, 0, 20, -11, 9] # Negative or zero value will throw exception
#gmean2 = statistics.geometric_mean(wrong_list)

#print('Geometric mean from list2 =', gmean2)


# Function 4: statistics.harmonic_mean (data, weights = None)
"""
Caculate the averrage in order to measure the central values 
of dataset especially in ratio like speed
"""

list4 = [11, 5, 9, 3, 2, 8, 6]
list5 = [30, 60, 50, 40, 65]
list5_weight = [0.25, 0.2, 0.15, 0.3, 0.1]

hmean = statistics.harmonic_mean(list4)
hmean_weight = statistics.harmonic_mean(list5, list5_weight)

print('Harmonic mean from list = ', hmean)
print('Harmonic mean from list with weight =', hmean_weight)

test_list = [14, 1, 2, 9, 22, 15, 6]
# Case number of weights is not equal to number of element in list
weights_test_list = [0.3, 0.15, 0.1, 0.25, 0.05, 0.1] 

#test_hmean = statistics.harmonic_mean(test_list, weights_test_list)

#print('Harmonic mean from test list with weight =', test_hmean)


# Function 5: statistics.median (data)
"""
Caculate the average of dataset as it is affected by outliners
"""

list6 = [2, 4, 9, 22, 31, 60] 
list7 = [4, 9, 2, 15, 22, 1, 40] 

median1 = statistics.median(list6)
median2 = statistics.median(list7) # Passing unsorted list is also acceptable

print('Median from sorted list = ', median1)
print('Median from unsorted list =', median2)


# Function 6: statistics.median_low (data)
"""
This function is the same as statistics.median(data)
but it will pick the smaller value of two middle ones
if the numbers of data is even
"""

list8 = [12, 1, 20, 30, 50, 99] # List has even length
list9 = [4.5, 6, 20, 11, 25.4] # List has odd length
tuple3 = (-6, -1, 7, 11, 20, -3, 5) # Tuple has mixed range of number

median_low1 = statistics.median_low(list8)
median_low2 = statistics.median_low(list9)
median_low3 = statistics.median_low(tuple3)

print('Median low from odd list =', median_low1)
print('Median low from even list =', median_low2)   
print('Median low from tuple has mixed range of num = ', median_low3)


# Function 7: statistics.median_high (data)
"""
This function is the same as statistics.median(data)
but it will pick the bigger value of two middle ones
if the numbers of data is even
"""

list10 = [22, 100, 10, 89, 30] # List has odd length
list11 = [11, 30, 49, 62, 82, 99] # List has even length
tuple4 = (7, 2, -11, 20, 13, 40, -23) # Tuple has mixed range of number

median_high1 = statistics.median_high(list10)
median_high2 = statistics.median_high(list11)
median_high3 = statistics.median_high(tuple4)

print('Median high from odd list =', median_high1)
print('Median high from even list =', median_high2)   
print('Median high from tuple has mixed range of num =', median_high3)


# Function 8: statistics.median_grouped (data, interval = 1)
"""
Calculate the median of grouped continous data by using interpolation
"""

list12 = [20, 40, 50, 90, 100] 
list13 = [1, -3, 11, 9, 8, -2]

median_grouped1 = statistics.median_grouped(list12, interval = 2)
median_grouped2 = statistics.median_grouped(list13, interval = 3)

print('Group median of list1 =', median_grouped1)
print('Group median of list2 =', median_grouped2)


# Function 9: statistics.mode (data)
""" 
Calculate the frequency of data and then pick which 
ones appear most commonly
"""

list14 = [3, 7, 9, 3, 2, 3, 7, 7, 6, 7, 9]
cars = ['BMW', 'Audi', 'Mercedes', 'Audi', 'Mercedes', 'Audi'] 
# If elements have frequency equally, it will return which one appears first
tuple5 = (11, 30, 22, 11, 19, 30, 35, 11, 26, 30) 

mode_list = statistics.mode(list14)
mode_cars = statistics.mode(cars) # Also works with nominal data type
mode_tuple = statistics.mode(tuple5) 

print('Mode from list =', mode_list)
print('Mode from car =', mode_cars)
print('Mode from tuple =', mode_tuple)


# Function 10: statistics.multimode (data)
"""
This function has the same feature like statistic.mode (data)
but returning a list of values appearing most frequently 
instead of just only one 
"""

list15 = [2, 6, 3, 2, 2, 3, 5, 7, 3, 6, 7, 6]
words = "Helloo worlddd!"
tuple6 = (5, 2, 3, 7, 2, 2, 7, 9, 3, 7, 3)

multimode1 = statistics.multimode(list15)
multimode2 = statistics.multimode(words)
multimode3 = statistics.multimode(tuple6)

# If elements have frequency equally, it will returns list of them
print('Multi mode from list =', multimode1)
print('Multi mode from words =', multimode2)
print('Multi mode from tuple =', multimode3)

# Function 11: statistics.quantiles (data, *, n, method = 'exclusive')
"""
This function returns a list of n - 1 numeric value of upper quantiles
Method can be exclusive by default or inclusive
"""

list16 = [3, 2, 7, 11, 9, 15, 8, 24, 30, 19, 27, 30]
quartiles_exclusive = statistics.quantiles(list16, n = 4) 
quartiles_inclusive = statistics.quantiles(list16, n = 4, method = 'inclusive')
deciles_exclusive = statistics.quantiles(list16, n = 10)
deciles_inclusive = statistics.quantiles(list16, n = 10, method = 'inclusive')

print('Exclusive quartiles =', quartiles_exclusive)
print('Inclusive quartiles =', quartiles_inclusive)
print('Exclusive deciles =', deciles_exclusive)
print('Inclusive deciles =', deciles_inclusive)


# Function 12: statistics.pstdev (data, mu = None)
"""
Calculate the popluation standard deviation of given data
The larger pstdev gains, the higher variablity of given data is   
"""

list16 = [3.9, 5, 11, 15.6, 17.8, 20, 24.5]
tuple7 = (1, 9, 20, 7, 60, 92, 15, 11, 3, 45)
tuple7_mu = statistics.mean(tuple7)

# If mu is not passed through parameter, function will calculate itself
list_pstdev = statistics.pstdev(list16) 
tuple_pstdev = statistics.pstdev(tuple7, tuple7_mu)

print ('Population standard deviation of list =', list_pstdev)
print ('Population standard deviation of tuple =', tuple_pstdev)

# Function 13: statistics.pvariance (data, mu = None)
"""
Calculate the population variance of given data
"""

list17 = [7, 24, 38, 40, 69, 100, 120]
list18 = [2, 6, 12, 24, 48, 50]
tuple8 = (12, 69, 95, 5, 20, 1, 16, 100)
mu_list18 = statistics.mean(list18)
mu_tuple8 = statistics.mean(tuple8)

# Not passing mu value, function automatically calculate it
pvar1 = statistics.pvariance(list17)
# Passing mu value
pvar2 = statistics.pvariance(list18, mu_list18)
pvar3 = statistics.pvariance(tuple8, mu_tuple8)

print('Population varince from list1 =', pvar1)
print('Population variance from list2 =', pvar2)
print('Population variance from tuple =', pvar3)


# Function 14: statistics.stdev (data, xbar = None)
"""
This function has the same feature with statistics.pstdev(data, mu = None)
but the standard deviation is belong to sample
"""

list17 = [1, 9, 22, 33, 50, 79, 100]
tuple9 = (17, 100, 60, 23, 41, 7, 9, 35)
mu_tuple9 = statistics.mean(tuple9)

# Not passing mu value, function will calculate by itself
list_stdev = statistics.stdev(list17)
# Passing mu value
tuple_stdev = statistics.stdev(tuple9, mu_tuple9)

print("Sample standard deviation from list =", list_stdev)
print("Sample standard deviation from tuple =", list_stdev)


# Function 15: statistics.variance (data, xbar = None)
"""
This function has the same feature with statistics.pvariance(data, mu = None)
but the variance is belong to sample
"""

list18 = [2.8, 7.3, 12.5, 20, 36.4]
list19 = [3, 6, 22, 40.5, 60, 100]
mu_list19 = statistics.mean(list19)

var1 = statistics.variance(list18)
var2 = statistics.variance(list19, mu_list19)

print('Sample variance from list1 =', var1)
print('Sample variance from list2 =', var2)


# Function 16: statistics.covariance (x, y, /)
"""
Calculate the covariance to measure the directional
relationship between two input dataset
"""

# Input length of two dataset must be the same
x1 = [9, 12, 16, 15, 13]
y1 = [11, 15, 19, 8, 5]

x2 = [-7, -2, -25, -13, -40]
y2 = [12, 20, 45, 16, 37]

covar1 = statistics.covariance(x1, y1)
covar2 = statistics.covariance(x2, y2)

print('First covariance =', covar1)
print('Second covariance =', covar2)


# Function 17: statistics.correlation(x, y, /, *, method = 'linear')
"""
This function returns the Pearson's correlation coefficient for 
measuring the strength and direction of linear relationship
"""

# Input length must be the same, otherwise it will thorw error
x3 = [22, 8, 19, 41, 12, 35]
y3 = [32, 58, 73, 61, 24, 40]

x4 = (2, 9, 8, 11, 21, 15)
y4 = (12, 24, 9, 11, 15, 7)

# There are two options for linear of ranked method respectively Pearson or Spearman
pearsonCoefficient = statistics.correlation(x3, y3, method = 'linear')
spearmanCoefficient = statistics.correlation(x4, y4, method = 'ranked')

print('The Pearson coeffiecient =', pearsonCoefficient)
print('The Pearson coeffiecient =', pearsonCoefficient)


# Function 18: statistics.linear_regression (x, y, /, *, proportional = False)
"""
This functions return the slope and intercept of independent variable x and
dependent variable y 
"""

hours = [2, 4, 7, 8, 10]
shirts_total = [5, 10, 15, 17, 20]

years = (2000, 2001, 2002, 2003, 2004)
cars_total = (15, 32, 40, 43, 45)

# Proportion set False mean they are undirectly proportional 
slope1, intercept1 = statistics.linear_regression(hours, shirts_total, proportional = False)
# Whereas, they are directly proportional
slope2, intercept2 = statistics.linear_regression(years, cars_total, proportional = True)

print('Slope1 =', slope1)
print('Intercept1 =', intercept1)
print('Slope2 =', slope2)
print('Intercept2 =', intercept2)

#print(statistics.pstdev([]))







