import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-LM222JM\SQLEXPRESS;'
                          'Database=AdventureWorks2017;'
                          'Trusted_Connection=yes;')

command = 'SELECT * FROM HumanResources.Department'

query = pd.read_sql_query("{}".format(command), conn)
df = pd.DataFrame(query)
df.to_xml('SQLServerToXml.xml', index=False, encoding='utf-8', root_name='Recordset')
