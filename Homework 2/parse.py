def greatest(numbers):
	j = 0
	for i in numbers:
		if abs(i) > j:
			j = abs(i)
	return j

def makearray(numbers):
	array = []
	file = open(numbers, "r")
	for line in file:
		spline = line.split(' ')
		for num in spline:
			array.append(float(num))
	return array

def converttovec3(numbers):
	file = open("vectors.txt", "w")
	i = 0
	while i < len(numbers):
		vector = 'vec3(' + str(numbers[i]/5) + ','  + str(numbers[i+1]/5) + ',' + str(numbers[i+2]/5) + '),\n'
		i= i + 3
		file.write(vector)
	file.close()

def converttovec(numbers):
	file = open("vectors.txt", "w")
	i = 0
	while i < len(numbers):
		vector = str(numbers[i]) + ', '  + str(numbers[i+1]) + ', ' + str(numbers[i+2]) + ', ' + str(numbers[i+3]) + ', ' + str(numbers[i+4]) + ', ' + str(numbers[i+5]) + ', ' + str(numbers[i+6]) + ', ' + str(numbers[i+7]) + ', ' + str(numbers[i+8]) + ',\n'
		i= i + 9
		file.write(vector)
	file.close()

if __name__ == '__main__':
	converttovec(makearray('data.txt'))