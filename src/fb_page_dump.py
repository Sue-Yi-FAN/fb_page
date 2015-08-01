import urllib.request
import json
import traceback

urlbase = "https://graph.facebook.com/"
parameter = "me/likes?access_token="
accessToken = "CAACEdEose0cBAMIGzansoLSEIF9sVP0V2BJZCrqcIi1VkKo6Hp2XhXgJVB8GfEUzKUeXe3k1yCEOT9JGldk5TlBgcBsEtSDbZCKGUmz5D1oRqfDTWLkW2ozv4gS8ZC0NrplDQp2TWwdsgQVZCs4kgP5OjU1m3WPW50RrZA7fmBssvTvBw2ZAJo4ZC2uhJwx98qWuZCNwzJyKnAEKXmKabomQ"

def is_access_id(url):
	try:
		with urllib.request.urlopen(url) as f:
			result = urllib.request.urlopen(url)
			return True
	except:
		return False

def force_get_id():
	urlbase = "http://graph.facebook.com/"
	idList = []
	for i in range(177265072325596,177265072330000):
		url = urlbase + str(i)
		if is_access_id(url):
			idList.append(i)
	return idList

def get_like_page(url):
	result  = ''
	while True:
		try:
			page_json = get_url_result(url)
			if(page_json):
				result += get_like_id(page_json['data'])
				url = (page_json['paging']['next'])
		except KeyError:
			print("KeyError : Id data")
			break;
	return result

def get_like_id(page_json):
	result = ''
	for data in page_json:
		try:
			result += str(data['id']) + \
			' ' + str(data['name']) + ' '
			result += get_page_detail(data['id']) + '\n'
		except KeyError:
			print("KeyError : page json have no 'id' or 'name'")
	return result

def get_base_url():
	url_base = 'http://graph.facebook.com/'
	return url_base

def get_url_result(url_id):
	url_base = get_base_url()
	url = url_base + str(url_id)
	try:
		with urllib.request.urlopen(url) as f:
			fbyte = f.read()
			fstr = fbyte.decode('utf-8')
			fbjson = json.loads(fstr)
			return fbjson
	except urllib.error.HTTPError as e:
		print("Get  {0}  fail".format(url_id))
		failure_log(url_id)
		return ''
	except:
		print('other fail and log id: {0}'.format(url_id))
		failure_log(url_id)
		traceback.print_exc()

def failure_log(url):
	try:
		with open('nondo.txt', 'a') as f:
			f.write(str(url)+'\n');
	except:
		pass

def get_page_detail(page_id):
	result = ''
	page_json = get_url_result(page_id)
	if(page_json):
		print("Success get id : {0}".format(page_id))
		try:
			 result = str(page_json['id']) + \
				'\t' + str(page_json['name']) + '\t'\
			 + str(page_json['category']) + '\t'\
			 + str(page_json['likes']) + '\t' \
			 + str(page_json['talking_about_count']) + '\t'\
			 + str(page_json['were_here_count']) + '\n'
			 return result
		except KeyError:
			print('KeyError : page json were not have some field')
		
def _inner_process():
	with open('TaiwanStoreFansIdNamePair.txt', 'r', encoding ='UTF-8') as f:
		for line in f:
			try:
				data = ''
				row = line.split('\t')
				data += row[0] + '\t' + row[1].splitlines()[0] + '\t'
				temp = get_page_detail(str(row[0]))
				if temp == str(row[0]):
					print("Wait for server")
					break
				else:
					data += temp + '\n'
					write_file(data)
			except TypeError:
				pass


def write_file(data,outname):
	with open(outname, 'a+', encoding = "UTF-8") as f:
			try:
				f.write(data)
			except TypeError:
				pass

def get_piece(filename,outname):
	with open(filename, 'r',encoding='UTF-8') as f:
		for line in f:
			data = line.splitlines()
			write_file(get_page_detail(data[0]),outname)
	end = input("Search is Over, click 'enter' to exit")

if __name__ == '__main__':
	fname = input('Please input the file name:\n');
	outname = input('input the output name:')
	get_piece(fname,outname)
