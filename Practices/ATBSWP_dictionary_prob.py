"""
Two function. One for displaying the items and total number of stuffs of the 
item, other one for adding new items from a list to a dictionary.
"""

def disp(dic):
	print ("Inventory:")
	tot = 0
	for i in dic.keys():
		print (i+ " "+ str(dic[i]))
		tot += dic[i]
	print ("Total number of items "+ str(tot))


def addInv (inv, loot):
	for i in loot:
		if i in inv.keys():
			inv.setdefault(i, inv[i])
			inv[i] += 1
		else:
			inv.setdefault(i, 0)
			inv[i] += 1
	return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addInv(inv, dragonLoot)
disp(inv)
