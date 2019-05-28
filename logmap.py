import xlrd
import json

logmaps = []
keys = ['code', 'info', 'detail', 'suggestion']

with xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\日志映射.xlsx') as log:
    with open('C:\\Users\\Administrator\\Desktop\\logmap.json', encoding='utf-8', mode='w+') as mapfile:
        sheetsName = log.sheet_names()   
        for sheetName in sheetsName:
            sheet = log.sheet_by_name(sheetName)
            for row in range(sheet.nrows):
                logmap = {}
                for col in range(sheet.ncols):
                    logmap[keys[col]] = sheet.cell_value(row, col)
                logmaps.append(logmap)
        json.dump(logmaps, mapfile, indent='\t', ensure_ascii=False)
