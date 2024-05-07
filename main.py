import gspread
import pandas as pd

sa = gspread.service_account(filename='credentials.json')
sh = sa.open("sheet_answers")


wks = sh.sheet1

select = 'asdf'
print(wks.acell('B2').value)
print(select)