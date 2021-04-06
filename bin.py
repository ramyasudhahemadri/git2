def b(n):
    if n==1 :
        return "0b1"
    else:
        
        return bin(n//2)+str(n%2)

n=int(input("enter the number::")) 
print(b(n))