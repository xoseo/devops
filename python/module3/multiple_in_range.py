def multiple_in_range(start, end):
	return [i for i in range(start,end+1) if i % 7 == 0 and i % 5 != 0]
