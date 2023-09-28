import pandas as pd

dataCsv = pd.read_csv("empresas.csv", delimiter=';')

df = pd.DataFrame(dataCsv)
df.to_xml('csvToXml2.xml', index=False, encoding='us-ascii', root_name='Recordset')
