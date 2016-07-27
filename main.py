import excel_parser
import excel_writer
import webster_api
import webster_xml_parser
import os

def check_word(word):
	xmlFileName = "words/"+word+".xml"
	xmlData = webster_api.get_word_definition(word)
	with open(xmlFileName, "w+") as xmlFile:
		xmlFile.write(xmlData)
		xmlFile.close()
	definitions = webster_xml_parser.get_definitions_from_file(xmlFileName)
	os.remove(xmlFileName)
	return definitions

def main():
	allwords = excel_parser.read_words_from_file("sheet.xlsm", "L1", "B2:B10")
	for word in allwords:
		print word + ": "
		print check_word(word)
		print "\n"

if __name__ == '__main__':
    main()