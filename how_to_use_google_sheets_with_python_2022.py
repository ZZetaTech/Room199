# https://www.youtube.com/watch?v=bu5wXjz2KvU
# i promise this is not a rick roll

import gspread
import datetime

sa = gspread.service_account(filename='service_account.json')
sh = sa.open('Dummy Data')

wks = sh.worksheet('Machine Data')
print('Rows:', wks.row_count)
print('Cols:', wks.col_count)

print(wks.acell('A1').value)

print(wks.get_all_records())
print(wks.get_all_values())

# Find a cell with exact string value
cell = wks.find("Ape")

print("Found something at R%sC%s" % (cell.row, cell.col))

# Get all values from the first row
values_list = wks.row_values(cell.row)

print(values_list)

# Find a cell with exact string value
cell_machine = wks.find("Bandsaw")

print("Found something at R%sC%s" % (cell_machine.row, cell_machine.col))

#.TIME FOR THE MOMENT OF TRUTH
# Is Ape verified to use Bandsaw?
print(values_list[cell_machine.col - 1])
print(wks.row_values(wks.find('Ape').row)[wks.find('Bandsaw').col-1])

def is_verified(student: str, machine: str) -> bool:
  return wks.row_values(wks.find(student).row)[wks.find(machine).col-1] == 'TRUE'

# wks_histories = sa.open('Machine Histories').worksheet('Histories')

sh_histories = sa.open('Machine Histories')
wks_histories = sh_histories.worksheet('Histories')

print(wks_histories.acell('A1').value)

print(type(datetime.date.today()))