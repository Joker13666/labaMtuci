mystr = input('text: ')

lst =  [x.split(';') for i, x in enumerate(mystr.split('_')) if i >= 0]

print(lst[0])

for x in lst:
    print(x[0] + '    ', x[1] + '    ', x[2]) 
 