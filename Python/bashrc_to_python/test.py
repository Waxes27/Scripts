def hello(x):
    print('hello you are bombs',x)
    
def bye(y):
    print('bye u suck',y)
    
fun = {'hello':hello,'bye':bye}

ls = []

for _ in input().lower().split():
    ls.append(_)
    
command = ls[0]


print(fun['hello'](2))