N= 3
for i in range(N+1):
    if i >=3:
        print(" "*(N-i)+"*"+(i*" ")+" "*((N+i)-N-3) +"*")
    else:
        print((N-i)*" "+("* "*i))
for i in range(N-1 ,-1 , -1 ):
    if i >=3:
        print(" "*(N-i)+"*"+(i*" ")+" "*((N+i)-N-3) +"*")
    else:
        print((N-i)*" "+("* "*i))
