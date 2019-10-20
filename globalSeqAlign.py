def printDB(db,l1,l2):
	for i in range(l1):
		for j in range(l2):
			print(db[i][j],end=' ')
		print()

def gbSq(s1,s2):
	db = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
	direction = [['-' for i in range(len(s2)+1)] for j in range(len(s1)+1)]
	for i in range(len(s2)+1):
		db[0][i]=-2*i
	for i in range(len(s1)+1):	
		db[i][0]=-2*i
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			l = db[i][j-1]
			u = db[i-1][j]
			d = db[i-1][j-1]
			if(s1[i-1]==s2[j-1]):
				d += 1
			else:
				d -= 1
			if(l-2 > d or u-2 > d):
				if(l>u):
					direction[i][j] = 'l'
				else:
					direction[i][j] = 'u'
				db[i][j] = max([l,u])-2
			else:
				db[i][j] = d
				direction[i][j] = 'd'
	s1_=''
	s2_=''
	r=len(s1)
	c=len(s2)
	while(r>0 and c>0):
		if(direction[r][c]=='d'):
			s1_ = s1[r-1]+s1_
			s2_ = s2[c-1]+s2_
			r -= 1
			c -= 1
		elif(direction[r][c]=='l'):
			s1_ = '-'+s1_
			s2_ = s2[c-1]+s2_
			c -= 1
		elif(direction[r][c]=='u'):
			s1_ = s1[r-1]+s1_
			s2_ = '-'+s2_
			r -= 1
		else:
			print('?')
			return
	print(s1_)
	print(s2_)
	printDB(db,len(s1)+1,len(s2)+1)

def main():
	s2 = 'GCCCTAGCG'
	s1 = 'GCGCAATG'
	gbSq(s1,s2)

if __name__ == '__main__':
	main()