from openpyxl import Workbook

def read_words_from_file(fileName):
	wb = Workbook(fileName)
	ws = wb.get_sheet_by_name("L1")

	allwords = []
	for row in range(1,3000):
		word = ws["B"+row]
		allwords.append(word)