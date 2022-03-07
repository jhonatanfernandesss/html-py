#!C:\Users\lucas\AppData\Local\Programs\Python\Python37\python.exe
import requests
import json
import cgi

#coleta dados do formulário

form = cgi.FieldStorage()

nome = form.getvalue('nome')

print(nome)


apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0OTQ3NDQ1OSwidWlkIjoyODYxMzUzMCwiaWFkIjoiMjAyMi0wMy0wN1QxNzoxMzo1MS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTAwMTUxNDEsInJnbiI6InVzZTEifQ.PuRTJAEcYVQc_e2y-IcQbwQ86qNF9-I7E3CueraHFX4"

apiUrl = "https://api.monday.com/v2"

headers = {"Authorization" : apiKey}



#Após cria item com valores de colunas

query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:2384161263, item_name:$myItemName, column_values:$columnVals) { id } }' 
vars = { 
'myItemName' : str(nome), 
'columnVals' : json.dumps({ 
   'status' : {'label' : 'Concluído'}, 
   'data' : {'date' : '2022-03-07'} 
}) 
} 

data = {'query': query5, 'variables' : vars}

r = requests.post(url=apiUrl, json=data, headers=headers)
print(data)
print(r.json())

print('<script>window.location="index.html"</script>')