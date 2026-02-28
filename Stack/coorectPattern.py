 
def correct_order(x):

        store = []
        for char in x:
            
            if store !=[] and store[-1] == "(":
                if char == ")":
                    store.pop()
                else:
                    store.append(char)
            elif store !=[] and store[-1] == "{":
                if char == "}":
                    store.pop()
                else:
                    store.append(char)
            elif store !=[] and store[-1] == "[":
                if char == "]":
                    store.pop()
                else:
                    store.append(char)
            else:
                store.append(char)

        if  store == []:
            return True
        return False   
        

print(correct_order("(([])){}"))   
print(correct_order("(([)){}]"))   
print(correct_order("(([]){}"))   
print(correct_order("()()[])){}"))   
 