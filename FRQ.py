def mostFrequent(L):
	maxValue=None
	maxCount=0
	counts=dict()
	for element in L:
		count=counts.get(element,0)+1
		counts[element]=count
		if (count>maxCount):
			maxCount=count
			maxValue=element
	return maxValue

print(mostFrequent([1,2,3,3,3,2,3,3,3]))


def mostCommonName(L):
	counts=dict()
	maxValue=-1 
	maxCount=-1
	for element in L:
		if(counts.get(element)==None):
			counts[element]=1
		else: 
			counts[element]+=1
	for i in counts:
		if counts[i]>maxValue:
			maxValue=counts[i]
			maxCount=i
	return maxCount

print(mostCommonName(["aaron", "cindy", "aaron", "jane"]))

def movieAwards(s):
	