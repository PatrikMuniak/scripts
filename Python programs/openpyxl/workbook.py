import openpyxl, pickle
pickle_in=open('dict.pickle', 'rb')
dic=pickle.load(pickle_in)
wb=openpyxl.load_workbook('Builtin.xlsx')
ws=wb.active
i=1
for function in dic.keys():
    ws.cell(row=i, column=1, value=str(function))
    i=i+1
a=1
for description in dic.values():
    ws.cell(row=a, column=2, value=str(description))
    a+=1
#openpyxl.worksheet.dimensions.ColumnDimension('ws',index='B', width=True)
wb.save('Builtin.xlsx')

