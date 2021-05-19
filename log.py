import json

with open('caminho do documento json') as f:
    #first_line = f.readline()
    for line in f:
        leitura = json.loads(line)
        print ((leitura)['ClientIP'])
        print ((leitura)['ClientRequestURI'])



