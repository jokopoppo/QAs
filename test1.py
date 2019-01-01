dict = {'a' : 1 }
a=[]

for i in a :
    try :
        dict['a']
    except KeyError:
        dict['a'] = 2

print(dict)