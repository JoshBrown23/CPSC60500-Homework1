"""
TITLE: Fermat's Near Misses
FILE: Fermat's-Near_Misses.py
EXTERNAL FILES (included in program): requirements.txt
EXTERNAL FILES (created by program): None
DEVELOPERS: Mohammed Abdulaziz, Josh Brown 
DEVELOPER EMAILS: , joshuaabrown@lewisu.edu
COURSE NUMBER & SECTION: CPSC 60500-1
SUBMISSION DATE: 11/13/2026

PROGRAM DESCRIPTION: This program calculates the near misses for Fermat's Last Theorem 

RESOURCES USED:
https://www.geeksforgeeks.org/maths/fermat-s-last-theorem/
https://stackoverflow.com/a/44063193
https://www.geeksforgeeks.org/python/progress-bars-in-python/
"""

from tqdm import tqdm

"""
This function calculates the near misses for Fermat's Last Theorem
"""
def calculate_near_miss(n, k):
    relative_miss = 0
    miss = 0



    for i in tqdm(range(k+1), desc="Progress"): # Progress bar
        for x in range(10, k+1): # Iterates through all possible x values
            for y in range(10, k+1): # Iterates through all possible y values
                s = pow(x,n) + pow(y,n) # Sum of x^n and y^n
                z = int(pow(s, 1/n)) # Taking nth root of s - sum of x^n and y^n
                z_diff = s - pow(z, n) # Difference between s and z^n
                z1_diff = pow(z+1, n) - s # Difference between (z+1)^n and s
                current_near_miss = min(abs(z_diff), abs(z1_diff)) # Minimum of the two differences
                current_relative_miss = (current_near_miss / s) # Relative miss as a percentage
                if current_relative_miss < relative_miss or relative_miss == 0: # If the current relative miss is smaller than the previous one or if it's the first iteration then save it otherwise skip it
                    relative_miss = current_relative_miss
                    miss = current_near_miss
                    tqdm.write(f"x: {x}| y: {y}| z: {z}| acutal miss: {current_near_miss} | relative miss: {current_relative_miss}")
                else:
                    continue

    print(f"Final near miss: {miss}| relative miss: {relative_miss}")

"""
This is the main function that takes user input and calls the calculate_near_miss function
"""
def main():
    print("Welcome to Fermat's Near Misses!")
    n = int(input("Enter the value of n (2 < n < 12): ")) #Input for n
    while n <= 2 or n >= 12: # Input validation for n
        n = int(input("Please enter an n value greater than 2 and less than 12: "))

    k = int(input("Enter the value of k (k > 10): ")) #Input for k
    while k <= 10: # Input validation for k
        k = int(input("Please enter a k value greater than 10: "))

    calculate_near_miss(n, k)

    input("Press Enter to exit...")


if __name__ == "__main__": 
    main()
