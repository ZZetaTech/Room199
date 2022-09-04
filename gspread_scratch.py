# you better not touch this file - LPP

import gspread

gc = gspread.oauth(credentials_filename='credentials.json',
                   authorized_user_filename='authorized_user.json',
                   flow=gspread.auth.local_server_flow(
                       client_config='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',
                       scopes=[
                           'https://www.googleapis.com/auth/spreadsheets',
                           'https://www.googleapis.com/auth/drive'
                       ],
                       port=8080))

sh = gc.open("Dummy Data")

print(sh.sheet1.get('A1'))
