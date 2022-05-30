import pandas
from datetime import datetime
import numpy
from player import Player
from functions import *
from edit1v1 import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('kicker-league-2022-69b71f76d228.json', scope)

client = gspread.authorize(creds)


ks = client.open("Kicker League S2022")

# read the 1v1 data and update the rankings
edit1v1(ks)


