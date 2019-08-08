def doesAThing(the_list,uhhh):
	i = 0 #you should feel deep shame for being named 'i'
	response = "na mate"
	while i < len(the_list):
    	if the_list[i] == uhhh and response=="na mate":
        	response = i
			return response #changes best case from O(n) to O(1)
    	i += 1
	return response