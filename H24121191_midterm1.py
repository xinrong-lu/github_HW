i = 9
while i > 2:
	a = i 
	b = i - 1
	c = i - 2
	j = 9
	while j > 0:
		print('%d x %d = %d' % (j, a, a*j), end='\t')
		print('%d x %d = %d' % (j, b, b*j), end='\t')
		print('%d x %d = %d' % (j, c, c*j))
		j -= 1
	print()
	i -= 3
