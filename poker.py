def numhand(hand):
	ranks = ['-A23456789TJQK'.index(r) for r,s in hand]
	return rank
def dokhand(hand):
    suit=[s for r,s in hand]
    return suit
def flush(hand):
    suit=dokhand(hand)
    return len(set(suits)) == 1