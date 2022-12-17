# Exercise 7 - namayesh maghsoomol-aley
# @author: Ramin Aryaei
#-----------------------------------------------
number = int(input('Enter a Number: '))
for i in range(1,number+1):
    if number % i == 0:
        print(i, end = '\t')