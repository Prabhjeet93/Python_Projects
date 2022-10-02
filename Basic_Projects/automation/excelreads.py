import pandas as pd
import csv




# df_sheet_index = pd.read_excel('./automation/data.xlsx')
# #print(df_sheet_index)
# print(type(df_sheet_index))

# print(df_sheet_index.count())

# for i in df_sheet_index.count:
#     print("The link is = ",i)

with open('./automation/data.csv', 'r') as file:
    rd = csv.reader(file)
    print(type(rd))
    # for row in rd:
    #     print(row)
file.close()
