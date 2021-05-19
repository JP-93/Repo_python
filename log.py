import json

with open('/Users/pedrobsouza/Documents/20210513T000013Z_20210513T000043Z_c9c50ef1.json') as f:
    #first_line = f.readline()
    for line in f:
        leitura = json.loads(line)
        print ((leitura)['ClientIP'])
        print ((leitura)['ClientRequestURI'])



