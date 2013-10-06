def numhand(hand):
	rank = ['--23456789TJQKA'.index(r) for r,s in hand]
	rank.sort(reverse=True)
	return rank

def dokhand(hand):
    suit=['-CDHS'.index(s)/10.0 for r,s in hand]
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

def is_three_of_kind(hand):
	num=numhand(hand)
	numset=list(set(num))
	for each in numset:
		if num.count(each)==3:
			return True
	return False

def is_four_of_kind(hand):
	num=numhand(hand)
	numset=list(set(num))
	for each in numset:
		if num.count(each)==4:
			return True
	return False

def is_two_pair(hand):
	count=0
	num=numhand(hand)
	numset=list(set(num))
	for each in numset:
		if num.count(each)==2:
			count+=1
	if count == 2:
		return True
	return False 

def is_one_pair(hand):
	count=0
	num=numhand(hand)
	numset=list(set(num))
	for each in numset:
		if num.count(each)==2:
			count+=1
	if count == 1:
		return True
	return False

def is_fullhouse(hand):
	num=numhand(hand)
	numset=list(set(num))
	if len(numset)!=2:
		return False
	return (num.count(numset[0])==3 and num.count(numset[1])==2) or	(num.count(numset[0])==2 and num.count(numset[1])==3)