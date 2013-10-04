def numhand(hand):
	rank = ['-A23456789TJQK'.index(r) for r,s in hand]
	return rank
def dokhand(hand):
    suit=[s for r,s in hand]
    return suit
def is_flush(hand):
    suit=dokhand(hand)
    return len(set(suits)) == 1
def is_stright(hand):
	num=numhand(hand)
	num.sort()
	for i in xrange(3):
		if num[i]+1!=num[i+1]:
			return False
	return True
def is_royal(hand):
	if sum(numhand(hand))== 60 and len(set(dokhand(hand))==1
		return True
	return False