import pandas as pd

df = pd.read_csv("empresas.csv", delimiter=';')

xml_data = ["""<?xml version="1.0" encoding="us-ascii"?>
    <Recordset>"""]

for row in df.iterrows():
    c = 0
    xml_data.append('<Row>')
    for value in df.index:
        xml_data.append('<{0}>{1}</{0}>'.format(df.columns[c], df.values[c][c]))
        c = c+1
    xml_data.append('</Row>')
xml_data.append('</Recordset>')

with open('csvToXml.xml', 'w', encoding='us-ascii') as f:
    for line in xml_data:
        f.write(line)
