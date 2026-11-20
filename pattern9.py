# #Question 9: Diamond
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

#outer loop for 5 times
for i in range(5):
    #inner loop for printing spaces in each row
    for j in range(5-i):
        print(" ",end=" ")
    #this loop prints 2*i-1 stars in each row
    for k in range(2*i-1):
        print("*",end=" ")
    #move to the next line
    print()
    
#running the outer loop in reverse order 
for i in range(5,0,-1):
    #inner loop for printing spaces in each row
    for j in range(5-i):
        print(" ",end=" ")
    #this loop prints 2*i-1 stars in each row
    for k in range(2*i-1):
        print("*",end=" ")
    #move to the next line
    print()