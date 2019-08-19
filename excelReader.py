from doctor import Doctor

def updateDb(db, module):
	wb = module.open_workbook('drFile.xlsx')
	for sheet in wb.sheets():
		for i in range(sheet.nrows):
			row = sheet.row(i)
			if not row[1].value:
				continue
			name = row[0].value
			for cell in row[2:]:
				val = cell.value
				db[val] = db.get(val, []) + [Doctor(name)]	
