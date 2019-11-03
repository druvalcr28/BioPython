from Bio import SeqIO

def makeDict(file_name):
    orgDict=dict()
    for seq_record in SeqIO.parse(file_name, "swiss"):
        protein = (seq_record.description.split(";")[0])[14:]
        org = seq_record.annotations["organism"]
        if(org in orgDict.keys()):
            (orgDict[org]).add(protein)
        else:
            orgDict[org] = set([protein])
    return orgDict

def findProteins(org,orgDict):
    for i in orgDict[org]:
        print(i)

def findDiff(orgDict):
    h = orgDict["Homo sapiens (Human)"]
    c = orgDict["Pan troglodytes (Chimpanzee)"]
    for i in (h-c):
        print(i)

def maxInter(orgDict):
    orgs = ["Homo sapiens (Human)","Pan troglodytes (Chimpanzee)","Mus musculus (Mouse)"]
    maxInter=0
    ans=[]
    for i in range(len(orgs)):
        for j in range(i+1,len(orgs)):
            inter = (orgDict[orgs[i]]).intersection(orgDict[orgs[j]])
            if(len(inter) > maxInter):
                maxInter=len(inter)
                ans=[i,j]
    if(maxInter==0):
        print("None")
    else:
        print(orgs[ans[0]],"&",orgs[ans[1]],":",maxInter)

def longestProt(file_name):
    maxL=0
    maxP=""
    for seq_record in SeqIO.parse(file_name, "swiss"):
        if (len(seq_record.seq) > maxL):
            maxL=len(seq_record.seq)
            maxP= seq_record
    print(maxP)

def protein_dict_fun(data):
    protein_dict = {}
    for seq_record in SeqIO.parse(file_name, "swiss"):
        protein_name = (seq_record.description.split(";")[0])[14:]
        org_name = seq_record.annotations["organism"]
        if not(protein_name in protein_dict.keys()) :
                protein_dict[protein_name] = set([org_name])
        else:
            protein_dict[protein_name].update(set([org_name]))
   
    return protein_dict

def main():
    # orgDict = makeDict("input.txt")
    # findProteins("Homo sapiens (Human)",orgDict)
    # findDiff(orgDict)
    # longestProt("input.txt")
    # maxInter(orgDict)


if __name__ == '__main__':
    main()