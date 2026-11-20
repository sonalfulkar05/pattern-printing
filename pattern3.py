#Question 3: Inverted Right-Angled Triangle
#running outer loop for 6 times in reverse order
for i in range(5,0,-1):
    #inner loop for printing stars in each row
    for j in range(i):
        #printing i number of stars in each row
        print("*",end=" ")
    #move to the next line    
    print()