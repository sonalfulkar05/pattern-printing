# #Question 7: Star Pyramid
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#outer loop for 6 times
for i in range(6):
    #inner loop for printing spaces in each row
    for j in range(6-i):
        print(" ",end=" ")
    #this loop prints 2*i-1 stars in each row
    for k in range(2*i-1):
        print("*",end=" ")
    #move to the next line
    print()