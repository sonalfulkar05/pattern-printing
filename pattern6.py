# #Question 6: Right-Aligned Triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(6):
    for j in range(6-i):
        print(" ",end=" ")  
    for i in range(i):
        print("*",end=" ")
    print()    
    