def search_in_dict(my_list_or_set, my_dict):

	new_set = set()
	for item in my_list_or_set:
		for value in my_dict.values():
			if item == str(value):
				new_set.add(item)
	return new_set
