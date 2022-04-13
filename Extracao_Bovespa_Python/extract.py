from yahooquery import Ticker

acao = Ticker("BPAC11.SA")
#print( petrobras.history(period="max"))

''' Extraindo periodo de 60 dias com intervalo de 30 minutos'''
#df = petrobras.history(start="2022-02-22", end="2022-02-23", interval = "1m" )


''' Extraindo periodo de 30 minutos'''
#df = acao.history(period="1d",  interval = "1m")



''' Extraindo de um periodo pré-estabelecido'''
df = acao.history(start="2022-04-11", end="2022-04-12", interval = "1m")

print(df)

'''Importação dos dados para CSV'''
compression_opts = dict(method='zip',archive_name='out.csv')

df.to_csv('out.zip', index=True, compression=compression_opts)
