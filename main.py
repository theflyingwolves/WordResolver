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

def definition_to_str(deftns):
	result = "";
	for deftn in deftns:
		result += deftn
		result += "\n"
	return result

def main():
	allwords = excel_parser.read_words_from_file("sheet.xlsm", "L1", 2,10)
	allDeftns = []
	for word in allwords:
		print word + ": "
		deftn = check_word(word)
		defStr = definition_to_str(defth)
		allDeftns.append(defstr)
		print defStr
	excel_writer.write_to_excel_column("sheet.xlsm", "L1", 2, 10)


if __name__ == '__main__':
    main()