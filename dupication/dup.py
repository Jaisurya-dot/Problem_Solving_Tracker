x = 'abcd'

def find_dup(s):
    dist = {}
    flag = False
    for i  in range(len(s)):
        try:
            if  dist[s[i]] is None:
                dist[s[i]] = 1
            else: 
                flag = True
                return flag
        except  KeyError:
             dist[s[i]] = 1
      
    return flag

if find_dup(x):
    print("Duplicate found")
else:
    print("No duplicate found")