import gspread

sa = gspread.service_account(filename="key/civil-hull-360218-c0bd493828d4.json")
sh = sa.open(title="dupa bez dupa3")

wks1 = sh.worksheet(title="Arkusz1")
print(wks1)

