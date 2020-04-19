def swap_max_and_min(my_list):
	if len(my_list) != len(set(my_list)):
		raise ValueError()

	max_item = my_list.index(max(my_list))
	min_item = my_list.index(min(my_list))

	my_list[max_item], my_list[min_item] = my_list[min_item], my_list[max_item]
	return my_list
	