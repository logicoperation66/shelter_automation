import gspread
from ggsheet import ggfunctions
from dotenv import load_dotenv
import os

load_dotenv()

google_key = os.getenv("GOOGLE_KEY")
chosen_indeks = int(input("Podaj numer indeksu: "))

sa = gspread.service_account(filename=google_key)
sh = sa.open(title="dupa bez dupa3")
wks1 = sh.worksheet(title="Arkusz1")

list_of_dicts = wks1.get_all_records()

if __name__ == "__main__":
    #Funkcja do pobierania pól z PDF
    #Funkcja do wypełniania pdf z danych z list_of_dicts
    #Funkcja do wstawiania zdjęć