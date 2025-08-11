import os
print(os.listdir('.'))

import datetime
data_atual = datetime.date.today()
print(data_atual)

import json
dados = '{"nome": "Alice", "idade": 30}'
dados_dict = json.loads(dados)
print(dados_dict['nome'])
