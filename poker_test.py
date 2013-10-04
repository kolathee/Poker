import unittest
import poker

def numhand(hand):
	return [2,3,4,5,6]
def dokhand(hand):
    ls=[]
    for i in hand:
        if i[1] not in ls:
            ls.append(i[1])
    return ls

