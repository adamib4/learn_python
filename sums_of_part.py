

def parts_sums(ls):
	test = []
	for x in range(len(ls)):
		test.append(sum(ls))
		ls.pop(0)
	test.append(0)
	return(test)

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
print (parts_sums(ls))