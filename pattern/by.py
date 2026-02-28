N = 5
for i in range(1,N+1):
    if i<=2 :
        print("* "*i +" "*(N*2)  +" "*N+"* "*i +" "*(N*2))
    else:
        print("* "+"  "*(i-2)+"*")
