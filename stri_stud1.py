st = input('text: ')

lst =  [x.split(';') for i, x in enumerate(st.split('_')) if i >= 0]

print(lst[0])

for x in lst:
	if x[0].find('Петров') != -1:
		print(x[0]+'\n',x[1]+'\n',x[2])

