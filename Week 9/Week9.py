#Problem 1
'''
def convert_knuts(knuts=450):
	KNUTS_PER_SICKLE = 29
	SICKLES_PER_GALLEON = 17
	KNUTS_PER_GALLEON = KNUTS_PER_SICKLE * SICKLES_PER_GALLEON
				
	galleons = knuts // KNUTS_PER_GALLEON
	remaining_knuts = knuts % KNUTS_PER_GALLEON
				
	sickles = remaining_knuts // KNUTS_PER_SICKLE
	remaining_knuts = remaining_knuts % KNUTS_PER_SICKLE
	
	output = ""
	
	if galleons > 0:
		if galleons > 1:
			output = output + str(galleons) + " galleons"
		else:
			output = output + str(galleons) + " galleon"
	
	if sickles > 0:
		if output:
			output = output + " "
		if sickles > 1:
			output = output + str(sickles) + " sickles"
		else:
			output = output + str(sickles) + " sickle"
	
	if remaining_knuts > 0:
		if output:
			output = output + " "
		if remaining_knuts > 1:
			output = output + str(remaining_knuts) + " knuts"
		else:
			output = output + str(remaining_knuts) + " knut"
	
	return output

print(convert_knuts(544))
'''
#Problem 2
'''
def highway_directions(highway_num):
	if 1 < highway_num < 99:
		if highway_num % 2 == 0:
			return f"I-{highway_num} runs east/west"
		else:
			return f"I-{highway_num} runs north/south"

	elif 100 < highway_num < 999:
		service_highway = highway_num % 100

		if 1 <= service_highway <= 99:
			if service_highway % 2 == 0:
				return f"I-{highway_num} runs east/west"
			else:
				return f"I-{highway_num} runs north/south"
		else:
			return f"I-{highway_num} is an invalid highway number"
	else:
		return f"I-{highway_num} is an invalid highway number"
	
print(highway_directions(353))
'''
#Problem 3

def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length):
		result += pattern * width
		if i < length - 1:
			result += "\n"
	return result

print(design_rug(3,5,'$'))