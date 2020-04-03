def number_increasing(n):
	total = 1
	while total <=n :
		if total == n:
			return True
		total = total *3 
		print(total)
	return False


print(number_increasing(9))