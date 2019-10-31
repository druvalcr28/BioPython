import csv

class SeqInfo:
	def __init__(self,seq,gcRatio):
		self.seq = seq
		self.gcRatio = gcRatio
		
def createCSV(db):
	with open('info.csv','w') as file:
		writer = csv.writer(file)
		writer.writerow(['id','GCpercentage'])
		index=1
		for obj in db:
			writer.writerow([index,(obj.gcRatio)*100])
			index += 1
	file.close()

def main():
	db=list()
	file = open("input.txt","r")
	lines = file.readlines()
	for line in lines:
		gc = line.count("G")+line.count("C")
		if(line[-1]=='\n'):
			db.append(SeqInfo(line[:-1],gc/(len(line)-1)))
		else:
			db.append(SeqInfo(line,gc/len(line)))

	createCSV(db)


if __name__ == '__main__':
	main()