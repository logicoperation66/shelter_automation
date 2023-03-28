## Define functions to fill pdf form
from PyPDF2 import PdfReader, PdfWriter

template_path = f"./empty.pdf"

reader = PdfReader(template_path)
fields = reader.get_fields()

values = {"numer": 123,
          "imie": "Jacek",
          "sex": "Jest",
          "chip": "jest",
          }

def fill_form(data:dict=None):





