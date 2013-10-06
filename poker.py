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

def handrank(hand):
	if is_royal(hand):
		return 10
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
				liTwo.remove(each)
		return 3,max(liTwo),min(liTwo),numset[0]
	elif is_one_pair(hand):
		num=numhand(hand)
		numset=list(set(num))
		numset.sort(reverse=True)
		liTwo=[]
		for each in numset:
			if num.count(each)==2:
				liTwo.append(each)
				liTwo.remove(each)
		return 2,liTwo[0],numset[0],numset[1],numset[2]
	else:
		num=numhand(hand)
		num.sort(reverse=True)
		return 1,num[0],num[1]