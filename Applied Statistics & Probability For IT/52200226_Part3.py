""" 
Source code of Part 3
Implement Histogram matching algorithm in image processing
"""

# Import openCV library for loading image
import cv2 

# Import numpy library for working with array
import numpy as np

# Import matplotlib library for plotting histogram and show image
import matplotlib.pyplot as plt

"""
Varible declared below are global varible
"""

# Read original and referenced image 
# Flag 0 means reading in greyscale format
# Return numpy array storing pixel values
initial_image = cv2.imread('image2.jpg', 0)
referenced_image = cv2.imread('image3.jpg', 0)

"""
User-defined function below is supported for
calculating histogram equalization
"""

# Function to count the occurences of each greyscale value
def countFrequency(image):
    # Find dimensions of image in (x, y) format
    dimensions = image.shape

    # [0] means retrieving x as number of rows
    rows = dimensions[0]

    # [1] means retrieving y as number of columns
    columns = dimensions[1]

    # Create array contains 256 int value, default of each is 0
    frequency = np.zeros(256, dtype = int) 

    # Loop through each pixel values to count frequency 
    for i in range(rows):
        for j in range(columns):
            frequency[image[i, j]] += 1
    return frequency

# Function to calculate PMF 
def calculatePMF (frequency):
    # Compute sum of all pixel values
    sum = np.sum (frequency) 

    # Create float numpy array to store PMF
    pmf = np.zeros(256, dtype = float)

    # Compute PMF by dividing frequency by sum of all image values
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


# Function to find new pixel value before mapping 
def findNewPixelValue(round1, round2):
    # Array contains 256 int values, default of each is 0 
    new_pixel_value = np.zeros(256, dtype = int)

    # Find index of nearest value as new pixel one
    for i in range(len(round1)):
        index_arr = np.where(round2 == round1[i])[0]
        if (len(index_arr) == 0):
            difference_arr = np.absolute(round2 - round1[i])
            index = difference_arr.argmin()
            new_pixel_value[i] = index
        else:
            new_pixel_value[i] = index_arr[0]
    return new_pixel_value

# Function to map new pixel value to initial image
def mapping(new_pixel_value):
    # Copy all values of image before processing
    processed_image = initial_image.copy()

    # Find dimensions of image in (x, y) format
    dimensions = processed_image.shape

    # [0] means retrieving x as number of rows
    rows = dimensions[0]

    # [1] means retrieving y as number of columns
    columns = dimensions[1]

    # Loop through image pixel value to map new one
    for i in range(rows):
        for j in range(columns):
            processed_image[i, j] = new_pixel_value[processed_image[i, j]]
    return processed_image

"""
Main function start from here
"""

# Call function to calculate frequency of each image
fre1 = countFrequency(initial_image)
fre2 = countFrequency(referenced_image)


# Call function to find PMF, CDF of the two image
pmf1 = calculatePMF(fre1)
cdf1 = calculateCDF(pmf1)

pmf2 = calculatePMF(fre2)
cdf2 = calculateCDF(pmf2)

# Call function to round CDF value of the two image
round1 = calculate_grayscale_eq(cdf1)
round2 = calculate_grayscale_eq(cdf2)

# Call function to match Histogram
new_pixel_value = findNewPixelValue(round1, round2)
matched_image = mapping(new_pixel_value)
fre3 = countFrequency(matched_image)

"""
Statements below are used for plotting
image and histogram after processing for more imaginable
"""

plt.figure(figsize = (14, 8))
plt.subplot(2, 3, 1)
plt.title('Initial image')
plt.imshow(initial_image, cmap = 'gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Referenced image')
plt.imshow(referenced_image, cmap = 'gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Matched image')
plt.imshow(matched_image, cmap = 'gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Histogram of initial one')
plt.xlabel('Grayscale value')
plt.ylabel('Frequency')
plt.plot(range(256), fre1)

plt.subplot(2, 3, 5)
plt.title('Histogram of referenced one')
plt.xlabel('Grayscale value')
plt.ylabel('Frequency')
plt.plot(range(256), fre2)

plt.subplot(2, 3, 6)
plt.title('Histogram of matched one')
plt.xlabel('Grayscale value')
plt.ylabel('Frequency')
plt.plot(range(256), fre3)

plt.show()

    
        













