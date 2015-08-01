import math

global dataset
dataset = 0
detail_category_dict = dict()
category_dict = dict()

addstr = lambda e1, e2: str(int(e1)+int(e2))
dividestr = lambda e1, e2: str(format(float(e1)/ float(e2),'.3f'))
multiplystr = lambda e1, e2: format(float(e1) * float(e2),'.4f')
integrate = lambda e1, e2, e3: float(multiplystr(e1, dividestr(e2, e3)))

def aggregate_samedata(category, like, talking, here_count):
	categorylist = category.split('/')
	valuelist = [like, talking, here_count,1]
	for ele in categorylist:
		if ele in category_dict:
			category_dict[ele][0] = addstr(category_dict[ele][0], like)
			category_dict[ele][1] = addstr(category_dict[ele][1], talking)
			category_dict[ele][2] = addstr(category_dict[ele][2], here_count)
			category_dict[ele][3] += 1
		else:
			category_dict.update({ele:valuelist})

def re_classify(type_dict, total):
	like = 0
	talk = 0
	here = 0
	for name in type_dict:
		like += integrate(type_dict[name][0],type_dict[name][3],total)
		talk += integrate(type_dict[name][1],type_dict[name][3],total)
		here += integrate(type_dict[name][2],type_dict[name][3],total)
	return [format(like,'.4f'), format(talk,'.4f'), format(here,'.4f')]


def average_data():
	new_dict = dict()
	for item in category_dict:
		new_list = []
		new_list.append(dividestr(category_dict[item][0],category_dict[item][3]))
		if(category_dict[item][1] != '0'):
			new_list.append(dividestr(category_dict[item][1],category_dict[item][3]))
		else:
			new_list.append(0)
		if(category_dict[item][2] != '0'):
			new_list.append(dividestr(category_dict[item][2],category_dict[item][3]))
		else:
			new_list.append(0);
		new_list.append(category_dict[item][3])	
		new_dict.update({item: new_list})
	return new_dict


def print_dict(pr_dict):
	for item in pr_dict:
		print(item,pr_dict[item])
		
def read_piecedata(filename):
	global dataset
	with open(filename, 'r') as f:
		for line in f:
			each = line.split('\t')
			dataset += 1
			#aggregate_samedata(each[2], each[3], each[4], each[5].splitlines()[0])

def read_piece(dir, number):
	try:
		for i in range(0, number+1):
			filename = dir + str(i) + '.txt'
			read_piecedata(filename)
	except IOError:
		print("No such file {0}".format(filename))

def read_classify_data():
	for i in range(0, 5):
		type_dict = dict()
		total = 0
		filename = str(i) + '.txt'
		with open(filename, 'r') as f :
			for line in f:
				rawdata = line.split(':')
				valuelist = rawdata[1].strip('[]\n').split(',')
				total += int(valuelist[3])
				type_dict.update({rawdata[0]:valuelist})
		value = re_classify(type_dict, total)
		detail_category_dict.update({str(i):value})
	write_dict(detail_category_dict,'detail.txt')

def write_dict(result_dict, filename):
	with open(filename, 'w') as f:
		for item in result_dict:
			f.write(item +'\t' + str(result_dict[item])+ "\n")

#if __name__ == '__main__':
read_piece('./output/opiece',43)
print(dataset)
	#read_classify_data()


