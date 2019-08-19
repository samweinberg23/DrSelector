from xlrd import open_workbook
import doctor

def updateDb(db):
	wb = ope_workbook('drFile.xls')
	for sheet in wb.sheets():
		for row in range(sheet.nrows):
			here = row[1].lower()
			if here == 'false':
				continue
			name = row[0]
			for val in row[2:]:
				db[val] = db.get(val, []) + [doctor(name)]	
