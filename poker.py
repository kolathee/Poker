def numhand(hand):
	"""
	(hand) --> list of rank
	
	Return ranks of a hand
	"""
	rank = ['--23456789TJQKA'.index(r) for r,s in hand]
	rank.sort(reverse=True)
	return rank

def dokhand(hand):
    '''
    (hand) --> list of suits

    Return suits of a hand
    '''
    suit=['-CDHS'.index(s)/10.0 for r,s in hand]
    return suit

def is_flush(hand):
    '''
    (hand) -->  bool

    Return True if hand is flush, else False
    '''
    suit=dokhand(hand)
    return len(set(suit)) == 1

def is_straight(hand):
    '''
    (hand) -->  bool

    Return True if hand is straight, else False
    '''
	num=numhand(hand)
	num.sort()
	for i in xrange(3):
		if num[i]+1!=num[i+1]:
			return False
	return True
	
def is_royal(hand):
    '''
    (hand) -->  bool

    Return True if hand is royal flush, else False
    '''
	if sum(numhand(hand))== 60 and len(set(dokhand(hand)))==1:
		return True
	return False

def is_straightflush(hand):
    '''
    (hand) -->  bool

    Return True if hand is straight flush, else False
    '''
	return is_straight(hand) and is_flush(hand)

def is_three_of_kind(hand):
    '''
    (hand) -->  bool

    Return True if hand is three of a kind, else False
    '''
	num=numhand(hand)
	numset=list(set(num))
	for each in numset:
		if num.count(each)==3:
			return True
	return False

def is_four_of_kind(hand):
    '''
    (hand) -->  bool

    Return True if hand is four of a kind, else False
    '''
	num=numhand(hand)
	numset=list(set(num))
	for each in numset:
		if num.count(each)==4:
			return True
	return False

def is_two_pair(hand):
    '''
    (hand) -->  bool

    Return True if hand is two pair, else False
    '''
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
    '''
    (hand) -->  bool

    Return True if hand is one pair, else False
    '''
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
    '''
    (hand) -->  bool

    Return True if hand is full house, else False
    '''
	num=numhand(hand)
	numset=list(set(num))
	if len(numset)!=2:
		return False
	return (num.count(numset[0])==3 and num.count(numset[1])==2) or	(num.count(numset[0])==2 and num.count(numset[1])==3)

def handrank(hand):
	"""
	(hand) --> tuple

	Return rank of a hand
	"""
	if is_royal(hand):
		return 10,0
	elif is_straightflush(hand):
		return 9,max(numhand(hand))
	elif is_four_of_kind(hand):
		num=numhand(hand)
		numset=list(set(num))
		if num.count(numset[0])==4:
			return 8,numset[0]
		return 8,numset[1]
	elif is_fullhouse(hand):
		num=numhand(hand)
		numset=list(set(num))
		if num.count(numset[0])==3:
			return 7,numset[0],numset[1]
		return 7,numset[1],numset[0]
	elif is_flush(hand):
		return 6,max(numhand(hand))
	elif is_straight(hand):
		return 5,max(numhand(hand))
	elif is_three_of_kind(hand):
		num=numhand(hand)
		numset=list(set(num))
		for each in numset:
			if num.count(each)==3:
				cha=numset.pop(numset.index(each))
				return 4,cha,max(numset),min(numset)
	elif is_two_pair(hand):
		num=numhand(hand)
		numset=list(set(num))
		liTwo=[]
		for each in numset:
			if num.count(each)==2:
				liTwo.append(each)
		remain=[]
		for each in numset:
			if each not in liTwo:
				remain.append(each)
		return 3,max(liTwo),min(liTwo),remain[0]
	elif is_one_pair(hand):
		num=numhand(hand)
		numset=list(set(num))
		numset.sort(reverse=True)
		liTwo=[]
		for each in numset:
			if num.count(each)==2:
				liTwo.append(each)
				numset.remove(each)
		return 2,liTwo[0],numset[0],numset[1],numset[2]
	else:
		num=numhand(hand)
		num.sort(reverse=True)
		return 1,num[0],num[1]

def whowin(hands):
	"""
	([hand, hand, ..., hand]) --> hand

	Return the best hand from a list of hands
	"""
	winner=max(hands,key=handrank)
	maxrank=handrank(winner)
	out=[]
	for hand in hands:
		if handrank(hand)==maxrank:
			out.append(hand)
	return out