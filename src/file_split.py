def splitfile():
	with open('TaiwanStoreFansIdNamePair.txt','r',encoding='UTF-8') as f:
		number = 0
		count = 0 ;
		for line in f:
			rowdata = line.split('\t')
			write_file(number,rowdata[0])
			count += 1;
			if count > 999:
				number += 1
				count = 0
def write_file(number,data):
	filename = 'piece' + str(number)+'.txt'
	with open(filename, 'a') as f:
		f.write((data)+'\n')

if __name__ == '__main__':
	splitfile()