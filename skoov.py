'''for skoov code challenge '''
def subSequenceChecker(subSequence, word,n,m):	
	'''
	Args:
	subSequence : Subsequence word (derived word)
	word 		: Original word from which subsequence are derived
	n 			: Lenth of Subsequence word
	m 			: lenth of Original word
	'''
	if(n == 0):
		# fucntion returns  the word if subsequence is derived from it.
		return word
	if(m == 0):
		return 0
	#condition of check if perticuller character exist in subsequence and word.
	if(subSequence[n-1] == word[m-1]):
		#if so recursive function call with each(word, subsequence) lenght-1.
		return subSequenceChecker(subSequence, word, n-1, m-1)
	# if they don't recursive function call with word lenght-1.
	return subSequenceChecker(subSequence, word, n, m-1)

try:
	fword = open("words.txt")
	fsubSequence = open("subwords.txt")
except IOError:
	print "IOError occured"
# wr and ws are variables which stores orignal word and subsequence word as list respectively.
wr = fword.read().split("\n")
ws = fsubSequence.read().split("\n")
for i in range(len(ws)):
	wlist = []
	for j in range(len(wr)):
		temp = subSequenceChecker(ws[i], wr[j], len(ws[i]), len(wr[j]))
		if temp:
			wlist.append(temp)
	s = ", "
	print '"%s" --> "%s".'%(ws[i], s.join(wlist))