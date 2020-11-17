with open("simptome-complete.txt", 'r') as file:
	in_string = file.read()
	in_string = in_string.replace('\r\n', ' ')
	in_string = in_string.replace('\n', ' ')

	in_string = in_string.replace(',', ' ')
	tokens = in_string.split(' ');

	unique = list(set(tokens))

	output = "\n".join(unique)
	print(output)

	with open("simptome-unice-complete.txt", 'w') as out:
		out.write(output)
	
