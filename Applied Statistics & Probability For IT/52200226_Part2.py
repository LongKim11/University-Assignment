"""
Source code of Part 1
Illustrate program for Histogram equalization algorithm in image processing
"""

# Import numpy module for working with array
import numpy as np 

# Import matplotlib module for plotting histogram and show image
import matplotlib.pyplot as plt 

# Import openCV library for loading image
import cv2 

"""
Variables declared below are global variable
"""

# Flag 0 means reading image in greyscale format
original_image = cv2.imread('image1.jpg', 0) # Return a numpy array

# Attribute shape for numpy array to achieve the dimensions in (x, y) format
dimensions = original_image.shape

# Retrieve x value of dimensions (x, y) as number of rows 
rows = dimensions[0]

# Retrieve y value of dimensions (x, y) as number of columns
columns = dimensions[1]

"""
User-defined functions below is supported for 
processing Histogram equalization algorithm
"""

# Function to count the occurences of each pixel value
def countOccurences (image):
    # Array contains 256 int values, default of each is 0
    frequency = np.zeros(256, dtype = int) 

    # Loop through each pixel values to count frequency 
    for i in range (rows):
        for j in range (columns):
            frequency[image[i, j]] += 1
    return frequency

# Function to calculate PMF 
def calculatePMF (frequency):
    # Find the total pixel value of image
    sum = np.sum (frequency) 

    # Create float numpy array to store PMF
    pmf = np.zeros(256, dtype = float)
    
    # Compute PMF by dividing each frequency by sum 
    pmf = [ele / sum for ele in frequency]
    return pmf 

# Function to calculate CDF 
def calculateCDF (pmf):
    # Array contains 256 float values, default of each is 0
    cdf = np.zeros(256, dtype = float)

    # Compute CDF by sum of its pmf value and left adjacent cdf value
    cdf[0] = pmf[0]
    for i in range (1, len(pmf)):
        cdf[i] = pmf[i] + cdf[i - 1]
    return cdf

# Function to find new greyscale value before mapping
def calculate_grayscale_eq(cdf_array):
    greyscale_eq = [np.round(ele * 255) for ele in cdf_array]
    return greyscale_eq

# Function to map new greyscale values into image
def mapping(new_greyscale):
    # Copy all values of original image before processing
    processed_image = original_image.copy()

    # Loop through image array to map new greyscale value into it
    for i in range (rows):
        for j in range(columns):
            processed_image[i, j] = new_greyscale[processed_image[i, j]] 
    return processed_image

"""
Main function starts from here
"""

# Call function to find PMF, CDF of input image
frequency = countOccurences(original_image)
pmf = calculatePMF(frequency)
cdf = calculateCDF(pmf)

# Call function to equalization histogram 
new_greyscale = calculate_grayscale_eq(cdf)
processed_image = mapping(new_greyscale)

# New PMF after processing
new_frequency = countOccurences(processed_image)

"""
Statements below are used for plotting
image and histogram after processing for more imaginable
"""
plt.figure(figsize = (12, 6))

plt.subplot(2, 2, 1)
plt.title('Original image')
plt.imshow(original_image, cmap = 'gray')
plt.axis('off')


plt.subplot(2, 2, 2)
plt.title('Processed image')
plt.imshow(processed_image, cmap = 'gray')
plt.axis('off')


plt.subplot(2, 2, 3)
plt.title('Histogram of original one')
plt.xlabel('Grayscale value')
plt.ylabel('Frequency')
plt.plot(range(256), frequency)


plt.subplot(2, 2, 4)
plt.title('Histogram of processed one')
plt.xlabel('Grayscale value')
plt.ylabel('Frequency')
plt.plot(range(256), new_frequency)

plt.show()






















