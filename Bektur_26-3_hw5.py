designations = []
codes = []

data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

operators = {}
i = 0
while i < len(designations):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators["Fonex"]
del operators["Katel"]

operators["O!"].add("0700")
operators["O!"].add("0500")
operators["Megacom"].add("0999")
operators["Megacom"].add("0555")
operators["Beeline"].add("0222")
operators["Beeline"].add("0777")
for key, value in operators.items():
    print(f"{key} - {value}")
