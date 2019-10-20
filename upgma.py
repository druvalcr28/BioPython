import sys

def  findMin(db,l):
	minR=minC=-1
	minV=sys.maxsize
	for i in range(l):
		for j in range(i):
			if(db[i][j]<minV):
				minR=i
				minC=j
				minV=db[i][j]
	return minR,minC

def printDict(d,dl,colName):
	print("Row and Column order :")
	for i in range(dl):
		name=''
		s=''
		for j in range(len(d[i])):
			name += colName[d[i][j]]
		name=s.join(sorted(list(name)))
		print(name,end='  ')
	print()

def makeNewDict(d,l,minR,minC,colName):
	nd=dict()
	nd[0]=d[minR]+d[minC]
	dIndex=0
	ndIndex=1
	while(dIndex<l):
		if(dIndex!=minR and dIndex!=minC):
			nd[ndIndex] = d[dIndex]
			ndIndex += 1
		dIndex += 1
	printDict(nd,ndIndex,colName)
	return nd

def printDB(db):
	print("Matrix :")
	for i in range(len(db)):
		print(db[i])

def makeNewDB(mainDB,nd,l):
	ndb = [[0 for i in range(l-1)] for j in range(l-1)]
	for i in range(l-1):
		for j in range(i):
			ans=0
			for l1 in range(len(nd[i])):
				for l2 in range(len(nd[j])):
					if(nd[i][l1]>nd[j][l2]):
						ans += mainDB[nd[i][l1]][nd[j][l2]]
					else:
						ans += mainDB[nd[j][l2]][nd[i][l1]]
			ans /= (len(nd[i])*len(nd[j]))
			ndb[i][j]=ans
	printDB(ndb)
	print()
	return ndb

def merge(mainDB,db,d,l,colName):
	if(l<=2):
		return
	minR,minC = findMin(db,l)
	nd = makeNewDict(d,l,minR,minC,colName)
	ndb = makeNewDB(mainDB,nd,l)
	merge(mainDB,ndb,nd,l-1,colName)

def main():
	db = [[],[19],[27,31],[8,18,26],[33,36,41,31],[18,1,32,17,35],[13,13,29,14,28,12]]
	colName = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G'}
	d=dict()
	for i in range(len(db)):
		d[i]=[i]
	merge(db,db,d,len(db),colName)

if __name__ == '__main__':
	main()