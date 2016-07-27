import excel_parser
import excel_writer
import webster_api
import webster_xml_parser

# word = "hypocrite"
# xmlFileName = "words/"+word+".xml"
# xmlData = webster_api.get_word_definition(word)
# with open(xmlFileName, "w+") as xmlFile:
# 	xmlFile.write(xmlData)
# 	xmlFile.close()

# print webster_xml_parser.get_definitions_from_file(xmlFileName)

print excel_parser.read_words_from_file("sheet.xls")