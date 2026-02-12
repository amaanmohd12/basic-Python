def fact():
     num=int(input("Enter a number:"))
     fact=1
     i=1
     while i <=num:
      fact=fact*i
      i+=1
     print("The Factorial of number",num,"is",fact)    
fact()
    
