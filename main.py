import pypyodbc

conn_str = (
    r'Driver={Microsoft Access Driver (*mbd, *.accdb)};'
    r'DBQ=./db/attBackup.mbd;'
)
conn = pypyodbc.connect(conn_str)

cursor = conn.cursor()
cursor.execute('SELECT name FROM MSysObjects WHERE type=1 AND flags=0')

for row in cursor.fetchall():
    print(row)

conn.close()