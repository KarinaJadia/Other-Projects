import numpy as np

ages = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
bodyfat = sorted([9.5,26.5,7.8,17.8,31.4,29.5,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7])
print(len(ages)/4, len(ages)/2, len(ages)*3/4)

print(ages[5],ages[14])
print(bodyfat[5],bodyfat[9],bodyfat[14])
print(min(bodyfat), max(bodyfat))