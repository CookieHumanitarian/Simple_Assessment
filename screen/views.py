from django.shortcuts import render

#Made a dict as it's easier to edit values
table_one = {
    "A1": 41, "A2": 18, "A3": 21, "A4": 63, "A5": 2, "A6": 53,
    "A7": 5, "A8": 57, "A9": 60, "A10": 93, "A11": 28, "A12": 3,
    "A13": 90, "A14": 39, "A15": 80, "A16": 88, "A17": 49,
    "A18": 60, "A19": 26, "A20": 28
}

#values for table 2
alpha_calc = table_one["A5"] + table_one["A20"]
beta_calc = table_one["A15"] / table_one["A7"]
charlie_calc = table_one["A13"] * table_one["A12"]

#Made another dict for table 2 so it's easier to edit
table_two = {
    "Alpha": alpha_calc, "Beta": beta_calc, "Charlie": charlie_calc
}

def index(request):
    return render(request, "index.html", {
        "table_one": table_one,
        "table_two": table_two
    })