def printDB(db,l1,l2):
	for i in range(l1):
		for j in range(l2):
			print(db[i][j],end=' ')
		print()

def gbSq(s1,s2):
	db = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
	direction = [['-' for i in range(len(s2)+1)] for j in range(len(s1)+1)]

	maxR=maxC=0
	
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			l = db[i][j-1]
			u = db[i-1][j]
			d = db[i-1][j-1]
			if(s1[i-1]==s2[j-1]):
				d += 1
			else:
				d -= 1
			if(max([l-2,u-2,d])>0):
				if(l-2 > d or u-2 > d):
					db[i][j] = max([l,u])-2
					if(db[maxR][maxC]<db[i][j]):
						maxR=i
						maxC=j
				else:
					db[i][j] = d
					if(db[maxR][maxC]<db[i][j]):
						maxR=i
						maxC=j
					direction[i][j] = 'd'
			else:
				db[i][j]=0
				direction[i][j] = '-'
	maxsolu=''
	while(direction[maxR][maxC] != '-'):
		maxsolu = s1[maxR-1]+maxsolu
		maxR -= 1
		maxC -= 1
	print(maxsolu)
	printDB(db,len(s1)+1,len(s2)+1)

def main():
	s2 = 'GCCCTAGCG'
	s1 = 'GCGCAATG'
	gbSq(s1,s2)

if __name__ == '__main__':
	main()