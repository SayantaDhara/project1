fiboArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(fiboArray): 
        return fiboArray[n-1] 
    else: 
        temp_fibo = fibonacci(n-1)+fibonacci(n-2) 
        fiboArray.append(temp_fibo) 
        return temp_fibo 

n=int(input("Enter number of terms"))  
print(fibonacci(n))
