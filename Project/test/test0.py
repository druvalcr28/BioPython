import os,sys
from Bio import SeqIO,Align

class ProteinInfo:
	def __init__(self,name,seq):
		self.name = name
		self.seq = seq

'''
pw2.align2.globalxx makes an optimal global alignment between your two sequences, where every match counts 1 point , while mismatches and insertions/deletions cost nothing.
'''
def findSim(seq1,seq2):
	aligner= Align.PairwiseAligner()
	score= aligner.score(seq1,seq2)
	return (score/min(len(seq1),len(seq2)))*100 
	
def main():
	#1
	currentD = os.getcwd()
	orgDict=list()
	mIndexToOrg={}
	index=0
	for filename in os.listdir(currentD):
		if(filename.endswith('.fasta')):
			orgRecord = list(SeqIO.parse(filename,"fasta"))
			orgName = ((orgRecord[0].name).split('|')[-1]).split('_')[-1]
			proteinInfo=list()
			for i in orgRecord:
				upIndex = (i.description).find('OS=')
				i.description = i.description[:upIndex-1]
				proteinName = '-'.join(((i.description).split())[1:])
				proteinSeq = i.seq
				proteinInfo.append(ProteinInfo(proteinName,proteinSeq))
			orgDict.append(proteinInfo)
			mIndexToOrg[index] = orgName
			index += 1
	# for i in range(len(orgDict)):
	# 	print(mIndexToOrg[i],len(orgDict[i]))

	#2
	protDict=dict()
	for orgl in range(len(orgDict)):
		for protCl in range(len(orgDict[orgl])):
			checkName = (orgDict[orgl][protCl]).name
			if(checkName not in protDict.keys()):
				seqList = list([(orgDict[orgl][protCl]).seq])
				for suborgl in range(orgl+1,len(orgDict)):
					for subprotcl in range(len(orgDict[suborgl])):
						if((orgDict[suborgl][subprotcl]).name==checkName):
							seqList.append((orgDict[suborgl][subprotcl]).seq)
							break
				protDict[checkName] = seqList
	# maxV=0
	# maxK=''
	# for i in protDict.keys():
	# 	print(i,len(protDict[i]))
	# 	if(len(protDict[i])>maxV):
	# 		maxV = len(protDict[i])
	# 		maxK = i
	# print(maxV,maxK)

	#3
	for protein in protDict.keys():
		removeList=list()
		for i in range(len(protDict[protein])):
			atleast=False
			for j in range(len(protDict[protein])):
				if(i!=j and findSim(protDict[protein][i],protDict[protein][j])>1):
					atleast=True
			if(not atleast):
				removeList.append(protDict[protein][i])
		protDict[protein] = list(set(protDict[protein])-set(removeList))
	
	#4
	minFound=list()
	minV=sys.maxsize
	for protein in protDict.keys():
		if(len(protDict[protein]) < minV):
			minFound.clear()
			minFound.append(protein)
			minV=len(protDict[protein])
		elif(len(protDict[protein]) == minV):
			minFound.append(protein)
	print(minFound)

if __name__ == '__main__':
	main()