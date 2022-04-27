import request
from json import loads
from terminaltables import AsciiTable

url = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"

response = request.get(url)
data = response.json()

print(data['rates'])

rows = [
['CURRENCY' , 'CODE', 'BID', 'ASK']
]
for row in data['rates']:
    rows.append([
    row['currency'],
    row['code'],
    row['bid'],
    row['ask']
])
table = AsciiTable(rows)
print(table.table)