def lists_2_dict(list1, list2):
	new_dict = {}
	for key in list1:
		for value in list2:
			new_dict[key] = value
			list2.remove(value)
			break
	return new_dict
	