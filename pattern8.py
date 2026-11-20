# #Question 8: Inverted Star Pyramid
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#running the outer loop in reverse order 
for i in range(6,0,-1):
    #inner loop for printing spaces in each row
    for j in range(6-i):
        print(" ",end=" ")
    #this loop prints 2*i-1 stars in each row
    for k in range(2*i-1):
        print("*",end=" ")
    #move to the next line
    print()