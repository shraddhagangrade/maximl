def SubSt(string):
	l1=[]
	c=0
	for i in string:
		if i not in l1:  
			l1.append(i)
		else:
			c=max(c,len(l1)) 
			l1.clear()
			l1.append(i)
	c=max(c,len(l1))
	print(c)
string=input("ENTER A STRING")
SubSt(string)
