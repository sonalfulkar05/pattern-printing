# #Question 11: Hollow Right-Angled Triangle
# *
# * *
# *   *
# *     *
# * * * * *

#running outer loop for 5 times
for i in range(5):
    #inner loop for printing stars in each row
    for j in range(i+1):
        #printing stars only in the first and last row and first and last column
        if i==4 or j==0 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    #move to the next line
    print()