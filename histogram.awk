{ arr[int($1/10)]++; next } 
END {
	for (i in arr) 
	print i " - " arr[i]
}
