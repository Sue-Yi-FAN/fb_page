import math
from aggregate_data import *
#normalize = lambda vl : [ x / sum(vl) for x in vl if x != 0] 
def normalize(vl):
	result = []
	for x in vl:
		if x != 0:
			result.append(x / sum(vl))
		else:
			result.append(0)
	return result

def diff_list(cl, tl):
	print(cl)
	print(tl)
	sum = 0
	for i in range(0,len(cl)):
		sum += pow(cl[i] - tl[i],2)
	return sum

def read_classify_data():
	category_dict = dict()
	with open('five_kind_range.txt', encoding='UTF-8') as f:
		for line in f:
			templist = line.split('\t')
			valuelist = [float(x) for x in 
			templist[1].strip('[]\n').split(',')]
			category_dict.update({templist[0]:valuelist})
	return category_dict

def read_input_data(name):
	filedir = './output/'
	filename = filedir + name
	test_dict = dict()
	with open(filename, encoding='UTF-8') as f:
		for line in f:
			rawdata = line.split('\t')
			valuelist = [int(rawdata[3]),int(rawdata[4]), 
			int(rawdata[5])] 
			dataname = rawdata[1] + '\t' + rawdata[2]
			test_dict.update({dataname:valuelist})
	return test_dict

def normalize_category(category_dict):
	n_category_dict = dict()
	for item in category_dict:
		normallist = normalize(category_dict[item])
		n_category_dict.update({item:normallist})
	return n_category_dict

def compare_two_dict(category_dict, test_dict):
	classify_dict = dict()
	for tname in test_dict:
		compare_dict = dict()
		valuelist = []

		for cname in category_dict:
			value = diff_list(category_dict[cname],
				test_dict[tname])
			valuelist.append(value)
			compare_dict.update({value:cname})
		
		answer = compare_dict[min(valuelist)]
		result = '(' + answer + ')' '\t' + tname
		classify_dict.update({result:test_dict[tname]})

	return classify_dict

def print_dict(category_dict):
	for item in category_dict:
		print(item, category_dict[item])


category_dict = read_classify_data()

normal_dict = normalize_category(category_dict)
print_dict(normal_dict)
#test_dict = read_input_data('opiece43.txt')
#normal_test = normalize_category(test_dict)
#print(normal_test)
#ctest_dict = compare_two_dict(normal_dict, normal_test)
#print_dict(ctest_dict)
#write_dict(ctest_dict,'classified_input.txt')