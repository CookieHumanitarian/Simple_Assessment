from django.shortcuts import render

table = {
    "A1": 41, "A2": 18, "A3": 21, "A4": 63, "A5": 2, "A6": 53,
    "A7": 5, "A8": 57, "A9": 60, "A10": 93, "A11": 28, "A12": 3,
    "A13": 90, "A14": 39, "A15": 80, "A16": 88, "A17": 49,
    "A18": 60, "A19": 26, "A20": 28
}

#View of index displaying table 1 and 2
def index(request):
    return render(request, "screen/index.html", {
        "tables": table
    })