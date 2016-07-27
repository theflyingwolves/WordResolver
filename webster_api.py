import urllib2

def get_word_definition(word):
	request_url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" + word + "?key=90d9256a-50de-40f7-9204-ff3928181f62"
	return urllib2.urlopen(request_url).read()