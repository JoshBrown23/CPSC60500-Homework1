# x^n + y^n = z^n - Fermat's Near Misses

# 2 < n < 12 - equations power
# 10 <= x <= k - variable x
# 10 <= y <= k - variable y
# k > 10 - limit of variables x and y. Can impose an upper limit if overflow occurs

# To check for misses use:
# z^n < (x^n + y^n) < (z+1)^n

# If a near miss is found, choose which is closer to (x^n + y^n) and print the result, including the relative difference.

# IS IT ALRIGHT TO MAKE THE APPLICATION CONSOLE BASED?


"""
TITLE: Fermat's Near Misses
FILE: Fermat's-Near_Misses.py
EXTERNAL FILES (included in program): None
EXTERNAL FILES (created by program): None
DEVELOPERS: Mohammed Abulaziz, Josh Brown 
DEVELOPER EMAILS: , joshuaabrown@lewisu.edu
COURSE NUMBER & SECTION: CPSC 60500-1
SUBMISSION DATE: 

PROGRAM DESCRIPTION: 

RESOURCES USED:
"""

# n = int(input("Enter the value of n (2 < n < 12): "))
# while n <= 2 or n >= 12:
#     n = int(input("Please enter an n value greater than 2 and less than 12: "))

# k = int(input("Enter the upper limit for x and y (k > 10): "))
# while k <= 10:
#    k = int(input("Please enter a k value greater than 10: "))


from math import floor
from tqdm import tqdm

# n = 9
# x = 126
# y = 125


# print(f"z^n: {z**n}")
# print(f"(z+1)^n: {(z+1)**n}")
# print(f"(x^n + y^n): {s}")



# print(f"z_diff: {z_diff * 100}%")
# print(f"z1_diff: {z1_diff * 100}%")


near_miss = 0
k = int(input("Enter the upper limit for x and y (k > 10): "))
n = int(input("Enter the value of n (2 < n < 12): "))
for i in tqdm(range(k)):
    for x in range(10, k):
        for y in range(10, k):
            s = x**n + y**n
            z = floor(pow(s, (1/n))) # Taking nth root of s - sum of x^n and y^n
            z_diff = (s - z**n)
            z1_diff = ((z+1)**n - s)
            current_near_miss = min(z_diff, z1_diff)
            if current_near_miss < near_miss or near_miss == 0:
                near_miss = current_near_miss
                print(f"x: {x}| y: {y}| z: {z}| actual miss: {current_near_miss} | relative miss: {(current_near_miss / s) * 100} %")
            else:
                continue

print(f"Final near miss: {near_miss }| relative miss: {(near_miss / s) * 100}%")
