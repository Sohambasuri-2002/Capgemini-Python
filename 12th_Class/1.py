# DATABASE CONNECTION : It is a process of connecting .py file with .db file
# We can perform CRUD operations on database

# SYNTAX TO CONNECT PY FILE TO DB FILE : 
# (1) import sqlite3 ---->  (provides file-based database like file.db)
# (2) conn = sqlite3.connect('database_name.db') ----->  (connect py file with db file)
# (3) cursor = conn.cursor() ---> (helps the interpreter to interact with database file)
# (4) cursor.execute('queries') 
# (5) conn.commit() ---> (use when there is a modification) and (To save modifications in table)
# (6) conn.close() ---> (To close db connection)
# (7) 

