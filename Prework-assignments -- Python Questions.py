#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):  #argument.....
    print(user_name + "USERNAME")   #takes orig arg thats inputted later and add the username part
hello_name("hello_")  # this takes the original arg and adding "hello" as the arg/var
 

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(a): #can i create an arg?
    return [i for i in range(0, a) if i % 2] #have to set condition? for "a" so that only odd numbers is printed. the % divides the "i", only taking odd values
print(first_odds(100)) #should print all odd numbers with in the range of up to any "a" value that's set


# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(a_list): #we have an arg, define it?
    a_list.sort()
    return a_list[-1] #sould grab the largest number after being sorted

a_list = [12, 15, 10, 38, 100, 96, 97, 77, 88, 55] #take list out of function
print(max_num_in_list(a_list))


# Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year): #def if/elif/else
    if a_year % 4 == 0: #checks to see if the year is divisible by 4 and then 400. if not will return false statements??..
        return True
    if a_year % 400 == 0:
        return True
    if a_year % 100 != 0:
        return False
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(2021))
print(is_leap_year(2022))
print(is_leap_year(2023))
print(is_leap_year(2024))


# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    if len(set(a_list)) == len(a_list) and max(a_list) - min(a_list): 
        return True
    else:
        return False
      
a_list = [3,-1,-2,0,1,8,6,7]

print(is_consecutive(a_list))






