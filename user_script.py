"""
Complete the script.
"""

#This script takes user input about employee salaries and
#  displays information relating to those salaries


#Collect employee salaries for 5 employees and turn into useable info
sal1 = float(input('Enter salary of Employee 1: '))
sal2 = float(input('Enter salary of Employee 2: '))
sal3 = float(input('Enter salary of Employee 3: '))
sal4 = float(input('Enter salary of Employee 4: '))
sal5 = float(input('Enter salary of Employee 5: '))

#Update user on process
print('Employee 1 Slalary has been sucessfully stored as an ', type(sal1))
print('Employee 2 Slalary has been sucessfully stored as an ', type(sal2))
print('Employee 3 Slalary has been sucessfully stored as an ', type(sal3))
print('Employee 4 Slalary has been sucessfully stored as an ', type(sal4))
print('Employee 5 Slalary has been sucessfully stored as an ', type(sal5))

#Convert to integer
sal1 = int(sal1)
sal2 = int(sal2)
sal3 = int(sal3)
sal4 = int(sal4)
sal5 = int(sal5)

#Update user on process (round 2)
print('Employee 1 Slalary has been sucessfully truncated as an ', type(sal1))
print('Employee 2 Slalary has been sucessfully truncated an an', type(sal2))
print('Employee 3 Slalary has been sucessfully truncated as an ', type(sal3))
print('Employee 4 Slalary has been sucessfully truncated as an ', type(sal4))
print('Employee 5 Slalary has been sucessfully truncated as an ', type(sal5))

#Find info about salaries
minsal = min(sal1, sal2, sal3, sal4, sal5)
maxsal = max(sal1, sal2, sal3, sal4, sal5)
avgsal = (sal1 + sal2 + sal3 + sal4 + sal5)/5

#Tell user about salaries
print('The lowest salary is: ', minsal)
print('The highest salary is: ',maxsal)
print('The difference between those is: ',maxsal-minsal)
print('The average salary is: ', avgsal)
