# import pandas lib as pd
import pandas as pd
import xlwings as xw

ws = xw.Book("Book1.xlsx").sheets['Sheet1']
# Selecting data from a single cell
v1 = ws.range("A1:A7").value
print(v1)


