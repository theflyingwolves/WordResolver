from openpyxl import Workbook
from openpyxl import load_workbook

def read_words_from_file(fileName, sheetName, rows):
	wb = load_workbook(fileName)
	ws = wb.get_sheet_by_name(sheetName)

	allwords = []
	for word in ws.iter_rows(rows):
		allwords.append(str(word[0].value))
	return allwords