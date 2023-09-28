import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LM222JM\SQLEXPRESS;'
                      'Database=AdventureWorks2017;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT * FROM HumanResources.Department', conn)

print(df)

xml_data = ['<root>']
for column in df.columns:
    xml_data.append('<{}>'.format(column))  # Opening element tag
    for field in df.index:
        # writing sub-elements
        xml_data.append('<{0}>{1}</{0}>'.format(field, df[column][field]))
    xml_data.append('</{}>'.format(column))
xml_data.append('</root>')

with open('teste.xml', 'w') as f:
    for line in xml_data:
        f.write(line)
