#Question 4: Increasing Number Triangle
#running outer loop for 6 times 
for i in range(6):
    #inner loop for printing numbers in increasing order
    for j in range(i+1):
        print(j+1,end=" ")
    #this print statement is used to move to the next line after each row is printed
    print()