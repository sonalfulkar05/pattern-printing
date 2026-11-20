# Question 10: Hollow Square
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
#running outer loop for 5 times
for i in range(5):
    #inner loop for printing stars in each row
    for j in range(5):
        #printing stars only in the first and last row and first and last column
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    #move to the next line
    print()