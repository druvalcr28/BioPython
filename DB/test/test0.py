from Bio import SeqIO,Align

def main():
	aligner= Align.PairwiseAligner()
	record0 = list(SeqIO.parse("o1.fasta", "fasta"))
	record1 = list(SeqIO.parse("o2.fasta", "fasta"))
	for i0 in record0:
		for i1 in record1:
			score= aligner.score(i0.seq,i1.seq)
			print(score/min(len(i0.seq),len(i1.seq)))
			break
		break
	#print(record0[0].seq)

if __name__ == '__main__':
	main()