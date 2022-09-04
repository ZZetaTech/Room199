import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Dummy Data').sheet1

print(sheet)