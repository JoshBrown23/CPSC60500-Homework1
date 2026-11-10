"""
TITLE: Fermat's Near Misses
FILE: Fermat's-Near_Misses.py
EXTERNAL FILES (included in program): None
EXTERNAL FILES (created by program): None
DEVELOPERS: Mohammed Abdulaziz, Josh Brown 
DEVELOPER EMAILS: , joshuaabrown@lewisu.edu
COURSE NUMBER & SECTION: CPSC 60500-1
SUBMISSION DATE: 

PROGRAM DESCRIPTION: 

RESOURCES USED:
"""

def calculate_near_miss(n, k):
    relative_miss = 0
    miss = 0

    for x in range(10, k):
        for y in range(10, k):
            s = pow(x,n) + pow(y,n)
            z = int(pow(s, 1/n)) # Taking nth root of s - sum of x^n and y^n
            z_diff = s - pow(z, n)
            z1_diff = pow(z+1, n) - s
            current_near_miss = min(abs(z_diff), abs(z1_diff))
            current_relative_miss = (current_near_miss / s) * 100
            if current_relative_miss < relative_miss or relative_miss == 0:
                relative_miss = current_relative_miss
                miss = current_near_miss
                print(f"x: {x}| y: {y}| z: {z}| acutal miss: {current_near_miss} | relative miss: {current_relative_miss}%")
            else:
                continue

    print(f"Final near miss: {miss}| relative miss: {relative_miss}%")




def main():
    n = int(input("Enter the value of n (2 < n < 12): "))
    while n <= 2 or n >= 12:
        n = int(input("Please enter an n value greater than 2 and less than 12: "))

    k = int(input("Enter the upper limit for x and y (k > 10): "))
    while k <= 10:
        k = int(input("Please enter a k value greater than 10: "))

    calculate_near_miss(n, k)

if __name__ == "__main__":
    main()
