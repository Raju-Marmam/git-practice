'''
1. Formatted Twinkle Poem

Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are

'''
import sys
from time import process_time_ns

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


'''
2. Python Version Checker
Write a Python program to find out what version of Python you are using.

'''

# print(sys.version)

# import platform
# print(platform.python_version())

'''
3. Current DateTime Display
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

'''
# import datetime
# date_time=datetime.datetime.now()
# print(date_time)
#
# dt1=date_time.strftime("%Y-%m-%d %H:%M:%S")
# print(dt1)



'''
4. Circle Area Calculator
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504

'''

# import math
# x=math.pi
# r=float(input("enter radius"))
# area=x*r**2
# print("Area = ",area)


'''
5. Reverse Full Name
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

'''

# f_name=input("enter first name ")
# l_name=input("enter last name ")
# print(l_name+" "+f_name)
# print(l_name,"",f_name) #gives space
# print(f"{l_name} {f_name}")


'''
6. List and Tuple Generator
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

'''

# num=input("Enter a sequence of comma-separated numbers")
# lst1=num.split(",") #split returns list
# tp1=tuple(lst1)
# print(lst1)
# print(tp1)

'''
7. File Extension Extractor
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

# file_name=input("Enter file name ")
# f_extention=file_name.split('.')    #retuns list
# print(f_extention[-1])  #printing last value from the list

'''
8. First and Last Colors
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]

'''
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

'''
9. Exam Schedule Formatter
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''
# exam_st_date = (11, 12, 2014)
# print("The examination will start from :",f"{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}" )


'''
10. Number Expansion Calculator
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

'''
# n=int(input("Enter an integer "))
# val=n+int((str(n)*2))+int((str(n)*3))
# print(val)

'''
11. Function Documentation Printer
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.

'''

# help(abs)

'''
12. Monthly Calendar Display
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module

'''


'''
13. Multi-line Here Document
Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

'''
# multi_line=('''
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# ''')
# print(multi_line)

'''
14. Days Between Dates
Write a  Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

'''

'''
15. Sphere Volume Calculator
Write a Python program to get the volume of a sphere with radius six.

'''
# import math
# radius=int(input("Enter the radius of the sphere "))
# volume=(4/3)*math.pi*radius**3
# print(volume)


'''
16. Difference from 17
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

'''
# num=int(input("Enter a number "))
# difference=num-17
# if num>17:
#     print(2*difference)


'''
17. Number Range Tester
Write a Python program to test whether a number is within 100 of 1000 or 2000.

'''

# num=int(input("Enter a number "))
# if num<=1100 and num>=900:
#     print("Number within 1000")
# elif num>=2100 and num>=1900:
#     print("Number within 2000")
# else:
#     print("Number Not within 1000 or 2000")


'''
18. Triple Sum Calculator
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
'''

# n1=int(input("Enter n1 "))
# n2=int(input("Enter n2 "))
# n3=int(input("Enter n3 "))
# sum1=n1+n2+n3
# print("sum =",sum1)
#
# if n1==n2==n3:
#     print(3*sum1)


'''
19. Prefix "Is" String Modifier
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

'''
# st=input("Enter Sting ")
# if st.startswith('ls'):
#     print(st)
# else:
#     print("ls"+st)

'''
20. String Copy Generator
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

'''
# str1=input("Enter Sting ")
# cp=int(input("Enter number of copied required "))
# if cp<0:
#     print("Kindly enter non-negative integer")
# else:
#     print(str1*cp)


