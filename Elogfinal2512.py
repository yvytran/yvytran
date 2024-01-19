import math
import numpy as np

# Constants
DELTA = 1  # Adjust the value of delta as needed

# Given values of x
x_values = [
   (135.9, 136.5, 136.5, 136.9, 133.9,135.5,134.9,136.5,135.5,135.5),
   (135.9, 136.5, 136.5, 136.9, 136.5,135.5,134.9,136.5,135.5,136.5),
   (135.9, 136.5, 136.5, 136.9, 134.5,135.5,134.9,136.5,135.5,135.9),
   (135.9, 136.5, 136.5, 136.9, 135.5,135.5,134.9,136.5,135.5,135.5),
   (135.9, 136.5, 136.5, 136.9, 134.9,135.5,134.9,136.5,135.5,136.5),
   (135.9, 136.5, 136.5, 136.9, 135.9,135.5,134.9,136.5,135.5,135.9)

]

# Given function f
def calculate_f1(pb1, pb2, pb3, pb4, pe, pb12, pb22, pb32, pb42, pe2):
   return -21.77 * pb1 - 35.88 * pb2 - 29.9 * pb3 -26.36 * pb4 - 40 * pe - 24.59*pb12 - 42.23*pb22 - 37.07*pb32 - 28.6*pb42 - 40*pe2 + 97732

def calculate_f2(pb1, pb2, pb3, pb4, pe, pb12, pb22, pb32, pb42, pe2):
   terms = [
       # term1
       (37.5 * ((0.2 / (1 + np.exp(124 + 0.9 * pb1))) + (np.exp(126 + 0.94 * pe)) + (0.55 / (1 + np.exp(124 + 0.9 * pb1))) + (0.25 / (1 + np.exp(126 + 0.94 * pe)))) + 37.5 * (
                      0.20 * np.exp(126 + 0.94 * pe)) / (1 + np.exp(124 + 0.94 * pb1) + np.exp(126 + 0.94 * pe)) + (
                      (0.25 * np.exp(126 + 0.9 * pe)) / (1 + np.exp(126 + 0.9 * pe))) - 10),
       # term2
       (60 * ((0.20 / (1 + np.exp(124 + 0.9 * pb2))) + (np.exp(126 + 0.94 * pe)) + (
             0.55 / (1 + np.exp(124 + 0.9 * pb2))) + (0.25 / (1 + np.exp(126 + 0.94 * pe)))) + 60 * (
                      0.20 * np.exp(126 + 0.94 * pe)) / (1 + np.exp(124 + 0.94 * pb2) + np.exp(126 + 0.94 * pe)) + (
                      (0.25 * np.exp(126 + 0.9 * pe)) / (1 + np.exp(126 + 0.9 * pe))) - 10),
       # term3
       (50 * ((0.20 / (1 + np.exp(124 + 0.9 * pb3))) + (np.exp(126 + 0.94 * pe)) + (
             0.55 / (1 + np.exp(124 + 0.9 * pb3))) + (0.25 / (1 + np.exp(126 + 0.94 * pe)))) + 50 * (
                      0.20 * np.exp(126 + 0.94 * pe)) / (1 + np.exp(124 + 0.94 * pb3) + np.exp(126 + 0.94 * pe)) + (
                      (0.25 * np.exp(126 + 0.9 * pe)) / (1 + np.exp(126 + 0.9 * pe))) - 10),
       # term4
       (43 * ((0.20 / (1 + np.exp(124 + 0.9 * pb4))) + (np.exp(126 + 0.94 * pe)) + (
             0.55 / (1 + np.exp(124 + 0.9 * pb4))) + (0.25 / (1 + np.exp(126 + 0.94 * pe)))) + 43 * (
                      0.20 * np.exp(126 + 0.94 * pe)) / (1 + np.exp(124 + 0.94 * pb4) + np.exp(126 + 0.94 * pe)) + (
                      (0.25 * np.exp(126 + 0.9 * pe)) / (1 + np.exp(126 + 0.9 * pe))) - 10),
       # term5
       (43 * ((0.20 / (1 + np.exp(124 + 0.9 * pb12))) + (np.exp(126 + 0.94 * pe2)) + (
                   0.55 / (1 + np.exp(124 + 0.9 * pb12))) + (0.25 / (1 + np.exp(126 + 0.94 * pe2)))) + 43 * (
                0.20 * np.exp(126 + 0.94 * pe2)) / (1 + np.exp(124 + 0.94 * pb12) + np.exp(126 + 0.94 * pe2)) + (
                (0.25 * np.exp(126 + 0.9 * pe2)) / (1 + np.exp(126 + 0.9 * pe2))) - 10),
       # term6
       (75 * ((0.20 / (1 + np.exp(124 + 0.9 * pb22))) + (np.exp(126 + 0.94 * pe2)) + (
                   0.55 / (1 + np.exp(124 + 0.9 * pb22))) + (0.25 / (1 + np.exp(126 + 0.94 * pe2)))) + 75 * (
                0.20 * np.exp(126 + 0.94 * pe2)) / (1 + np.exp(124 + 0.94 * pb22) + np.exp(126 + 0.94 * pe2)) + (
                (0.25 * np.exp(126 + 0.9 * pe2)) / (1 + np.exp(126 + 0.9 * pe2))) - 10),
       # term7
       (62 * ((0.20 / (1 + np.exp(124 + 0.9 * pb32))) + (np.exp(126 + 0.94 * pe2)) + (
               0.55 / (1 + np.exp(124 + 0.9 * pb32))) + (0.25 / (1 + np.exp(126 + 0.94 * pe2)))) + 62 * (
                0.20 * np.exp(126 + 0.94 * pe2)) / (1 + np.exp(124 + 0.94 * pb32) + np.exp(126 + 0.94 * pe2)) + (
                (0.25 * np.exp(126 + 0.9 * pe2)) / (1 + np.exp(126 + 0.9 * pe2))) - 10),
       # term8
       (50 * ((0.20 / (1 + np.exp(124 + 0.9 * pb42))) + (np.exp(126 + 0.94 * pe2)) + (
               0.55 / (1 + np.exp(124 + 0.9 * pb42))) + (0.25 / (1 + np.exp(126 + 0.94 * pe2)))) + 50 * (
                0.20 * np.exp(126 + 0.94 * pe2)) / (1 + np.exp(124 + 0.94 * pb42) + np.exp(126 + 0.94 * pe2)) + (
                (0.25 * np.exp(126 + 0.9 * pe2)) / (1 + np.exp(126 + 0.9 * pe2))) - 10)


   ]
   return sum(terms)

# Sort x_values based on the values of the function f
sorted_x_list = sorted(x_values, key=lambda x: calculate_f1(*x))

# Print the sorted x_values
print("Sorted x values in increasing order of f1:")
for x in sorted_x_list:
   print("x =", x, ", f1 =", calculate_f1(*x))

# Print the sorted x_values
print("Sorted x values as a list: \n", sorted_x_list )

def discrete_neighborhood(yk, delta):
   n = len(yk)
   for i in range(n):
       for d in np.arange(-delta, delta + 1, delta):
           y_neighbor = np.copy(yk)
           y_neighbor[i] += d
           yield tuple(y_neighbor)
# Iterate through each set and print its neighborhood results
for i, set_values in enumerate(x_values):
   print(f"Set {i + 1} neighborhood:")


   for neighbor in discrete_neighborhood(set_values, DELTA):
       print(neighbor)


   print("-" * 20)  # Add a separator between sets

def zag(xi, calculate_f1, calculate_f2, sorted_x_list, delta):
   k, bCont = 0, 1

   yk = xi

   while bCont:
       bCont, yList, y_values_tuples = 0, [], []
       for ykj in discrete_neighborhood(yk, delta):
           if np.all(ykj >= yk) and calculate_f1(*ykj) < calculate_f1(*yk):
               yk, k, bCont = ykj, k + 1, 1
               continue


           elif calculate_f2(*ykj) < calculate_f2(*yk):
               yList.append(ykj)
               y_values_tuples.append(tuple(ykj))
               bCont = 1

       if bCont:
           y_star = min(y_values_tuples, key=lambda ykj: calculate_f1(*ykj))
           if np.all(np.greater(y_star, sorted_x_list)):
               yk, k = y_star, k + 1
           else:
               bCont = 0
           print(y_star)

   return yList

def process_sorted_x_list(sorted_x_list, calculate_f1, calculate_f2, delta):
   xList = []

   if sorted_x_list is not None:
       for xi in sorted_x_list:
           yList = zag(xi, calculate_f1, calculate_f2, sorted_x_list, delta)
           xList.append(yList)

   return xList

# Call the function with your parameters
result = process_sorted_x_list(sorted_x_list, calculate_f1, calculate_f2, DELTA)

# Print the result
print("Result: \n", result)

print("\nSubstituted Results:")
for i, yList in enumerate(result):
   for j, yk in enumerate(yList):
       print(f"Set {i + 1}, Neighbor {j + 1} - f1: {calculate_f1(*yk)}, f2: {calculate_f2(*yk)}")





