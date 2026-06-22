"""FALSE BOOLEANS
Empty strings
empty sets,list etc
value none
value false
zero
obj from class with _len_func that return 0/false
"""
"""
class myclass():
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj))
#@hahaha it returns true
"""
def myfunc():
    return True
if myfunc():
    print("YES!")
else:
    print("No!")