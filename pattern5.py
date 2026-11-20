# Question 5: Repeated Row Number Triangle
#running outer loop for 6 times 
for i in range(1,6):
    #inner loop printing the same number in each row
    for j in range(i):
        print(i,end=" ")
    #this print statement is used to move to the next line after each row is printed
    print()