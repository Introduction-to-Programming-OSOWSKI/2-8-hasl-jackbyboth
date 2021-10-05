#WRITE YOUR CODE IN THIS FILE
def hasL(x):


    for i in range(0, len(x)):
        
        if x[i] == "l":
            return True
        
        
    return False
print(hasL("abama"))