# Exercise 1: Print First 10 natural numbers using while loop

# number = 1
# while number < 11:
#     print(number)
#     number+=1


# Exercise 2: Print the following pattern

# for x in range(1,6):
#     for y in range(1,x+1):
#         print(y,end=' ')
#     print('')


# Exercise 3: Calculate the sum of all numbers from 1 to a given number

# number = int(input("Number: "))
# sum = 0
# for x in range(number+1):
#     #print(x)
#     sum +=x
# print(sum)


# Exercise 4: Write a program to print multiplication table of a given number

# num = int(input("Number: "))
# for x in range(1,11):
#     print(x*num)

# Exercise 5: Display numbers from a list using loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for num in numbers:
#     if num > 500:
#         break
#     elif num > 150:
#         continue
#     elif num%5==0:
#         print(num)

# Exercise 6: Count the total number of digits in a number

# num = 756893
# count = 0
# while num > 0 :
#     num //= 10
#     count+=1
#
# print(count)

#Exercise 7: Print the following pattern

# for x in range(5,0,-1):
#     for y in range(x,0,-1):
#         print(y,end=" ")
#     print("")

# Exercise 8: Print list in reverse order using a loop

# list1 = [10, 20, 30, 40, 50]
# # print(list1[4])
# for x in range(len(list1),0,-1):
#     print(list1[x-1])

# Exercise 9: Display numbers from -10 to -1 using for loop

# number = -10
# for x in range(number,0,1):
#     print(x)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# for i in range(5):
#     print(i)
# else:
#     print("Done")

# Exercise 11: Write a program to display all prime numbers within a range

# start = 25
# end = 50
#
# for num in range(start,end+1):
#     # print(num)
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)



# Exercise 12: Display Fibonacci series up to 10 terms
# num1 = 0
# num2 = 1
# for x in range(10):
#     print(num1)
#     result = num1+num2
#     num1=num2
#     num2=result


# Exercise 13: Find the factorial of a given number

# res = 1
# for x in range(1,6):
#     res = x * res
#     print(res)

# Exercise 14: Reverse a given integer number

# number = 76432
# list1 = list(str(number))
# for x in list1[::-1]:
#     print(x)


# Exercise 15: Use a loop to display elements from a given list present at odd index positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# length_of_list = len(my_list)
#
# for x in range(length_of_list):
#     if x % 2 != 0 :
#         print(my_list[x])


# Exercise 16: Calculate the cube of all numbers from 1 to a given number

# num = int(input("Enter number: "))
# for i in range(1,num+1):
#     print(f"Current Number is : {i}  and the cube is {i**3}")

# Exercise 17: Find the sum of the series upto n terms

# n = 5
# sum = 0
# for i in range(1,n+1):
#     val  = int(i*"2")
#     sum += val
#     print(sum)

# n = 5
# sum = 0
# current_num = 0
# for i in range(1,n+1):
#     current_num = (current_num * 10) + 2
#     sum += current_num
#     print(sum)

# Exercise 18: Print the following pattern

for i in range(6):
    print(i*' *')
for j in range(4,0,-1):
    print(j*' *')