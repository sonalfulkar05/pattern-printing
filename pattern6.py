# #Question 6: Right-Aligned Triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#outer loop for 6 times
for i in range(6):
    #inner loop for printing spaces in each row
    for j in range(6-i):
        print(" ",end=" ") 
    #inner loop for printing stars in each row     
    for k in range(i):
        print("*",end=" ")
    print()    
    