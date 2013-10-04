def numhand(hand):
	rank = ['--23456789TJQKA'.index(r) for r,s in hand]
	return rank

def dokhand(hand):
    suit=[s for r,s in hand]
    return suit

def is_flush(hand):
    suit=dokhand(hand)
    return len(set(suit)) == 1

def is_straight(hand):
	num=numhand(hand)
	num.sort()
	for i in xrange(3):
		if num[i]+1!=num[i+1]:
			return False
	return True
	
def is_royal(hand):
	if sum(numhand(hand))== 60 and len(set(dokhand(hand)))==1:
		return True
	return False

def is_straightflush(hand):
	return is_straight(hand) and is_flush(hand)