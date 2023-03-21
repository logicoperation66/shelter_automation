### Define func which gona return data from row of specific index

def gg_row(
        worksheet:str=None,
        index:str=None):
    wks = worksheet
    row = wks.get(f"A{index+1}:F{index+1}")

    return row