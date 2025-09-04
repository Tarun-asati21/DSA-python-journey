def pattern1(n):

    for i in range(n) :
        for j in range(1) :
            print("*"*n)

def pattern2(n):

    for i in range (1,n+1):
            print ("*"*i)

def pattern3(n):
    
    num = ""

    for i in range (1,n+1):
            num = num + str(i)
            print(num)

def pattern4(n):

    for i in range (1,n+1):
            print(str(i)*i)

def pattern5(n):

    for i in range (n,0,-1):
            print("*"*i)

def pattern6(n):

    for i in range (n,0, -1):
        for j in range (1,i+1):
            print(j, end="")    
        print()

def pattern7(n):

     for i in range(1,n+1):
            for k in range (0, n-i ):
                 print(" ", end="")
            for j in range (0, 2*i-1 ):
                print("*", end="")
            for m in range (0, n-i ):
                print(" ", end="")
            print()

def pattern8(n):
     
     for i in range(n,0,-1):
        for k in range (0, n-i):
            print(" ", end ="")
        for j in range (0, 2*i-1):
            print("*", end ="")
        for k in range (0, n-i):
            print(" ", end ="")
        print()        

def pattern9(n):

     for i in range(1,n+1):
            for k in range (0, n-i ):
                 print(" ", end="")
            for j in range (0, 2*i-1 ):
                print("*", end="")
            for m in range (0, n-i ):
                print(" ", end="")
            print()    

     for i in range(n,0,-1):
        for k in range (0, n-i):
            print(" ", end ="")
        for j in range (0, 2*i-1):
            print("*", end ="")
        for k in range (0, n-i):
            print(" ", end ="")
        print()             

def pattern10(n):
     
     for i in range (1,n+1):
          print("*"*i, end="")
          print()
     for j in range (n-1, 0, -1):
          print("*"*j, end ="")
          print() 
     

def pattern11(n):
     
     for i in range (1,n+1):
          if i%2 !=0 :
               print("1 "+"0 1 "*(i//2), end ="")
               print()
          if i%2 == 0 :
               print("0 1 "*(i//2), end ="")
               print()

def pattern12(n):
     
     for i in range (1,n+1):
          
          for j in range (1,i+1):
            print (j , end ="")
          for k in range (0,2*(n-i)):
            print(" ", end="")
          for m in range (i,0,-1):
            print(m, end ="")
          print()

def pattern13(n):

        num = 0
        for i in range (1,n+1):
             for j in range (1, i+1):
                  
                  num = num+1
                  print(num , end =" ")

             print()

def pattern14(n):

    # way1
    # list = ["A","B","C","D","E"]
    # for i in range (0, n):
    #      for j in range(0, i+1):
    #         print(list[j], end ="") 
    #      print()

    # scalable way 
    for i in range (0,n):
         for j in range (0, i+1):
              print(chr(65+j), end="")
         print()

def pattern15(n):
     
     for i in range (n,0, -1):
          for j in range (0, i):
               print(chr(65+j), end="")
          print()

def pattern16(n):
     
     for i in range (1,n+1):
          print((chr(64+i))*i, end ="")
          print()

def pattern17(n):
     
     for i in range (1, n+1):
          
          for j in range (0,n-i):
               print(" ", end="")
          for k in range (1, i+1):
               print(chr(64+k), end="")
          for l in range(i-1, 0, -1):
               print(chr(64+l), end="")
          for j in range (0,n-i):
               print(" ", end="") 
          print()       

def pattern18(n):
    
    for i in range (1,n+1):
         for k in range (i, 0,-1):
              print(chr(65+n-k), end="")
         print()

def pattern19(n):

    for i in range (n,0,-1):
         for j in range (0, i):
              print("*", end="")
         for j in range (0, 2*(n-i)):
              print(" ", end="")
         for j in range (0,i):
              print("*", end ="")
         print()

    for i in range (1,n+1):
         for j in range (0,i):
              print("*",end ="")
         for j in range(0, 2*(n-i)):
              print(" ", end="")
         for j in range (0, i):
              print("*",end="")
         print()                 
                    
def pattern20(n):

     for i in range (1,n+1):
          for j in range (0,i):
               print("*", end ="")
          for j in range (0, 2*(n-i)):
               print(" ", end ="")
          for j in range (0,i):
               print('*', end = "")
          print()

     for i in range (n-1,0,-1):
         for j in range (0, i):
              print("*", end="")
         for j in range (0, 2*(n-i)):
              print(" ", end="")
         for j in range (0,i):
              print("*", end ="")
         print()         
          
def pattern21(n):

     for i in range (0,n):
          print("*",end ="")
     print()

     for i in range (0, n-2):
          for j in range (1):
               print("*", end="")
          for j in range (0, n-2):
               print(" ", end="")
          for j in range (1):
               print("*", end ="")
          print()

     for i in range (0,n):
          print("*",end ="")

def pattern22(n):

     size = 2*n -1
     for i in range (size):
          for j in range (size):
               num = min(i,j,size-i-1,size-j-1)
               print(n - num, end=" ")
          print()
