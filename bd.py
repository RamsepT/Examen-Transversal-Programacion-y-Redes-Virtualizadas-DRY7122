import sqlite3

phatBD = "C:\\Users\\Windows Microsoft\\Documents\\ITEM03\\.envi\\instance\\users.db"

def crearBD():
        conn = sqlite3.connect(phatBD)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE usuarios (nombre text, apellido text, rut integer)""")
        conn.commit()
        conn.close()

def AgregarUser():
        conn = sqlite3.connect(phatBD)
        cursor = conn.cursor()
        data = [
            ("Jeremy","Soto", 390494034 ),
            ("Rodrigo","Flores", 209143836 ),
            ("Ramsept","Vega", 204304980 ),
            ("Moises", "Gutierrez", 39044309)
        ]
        cursor.executemany("""INSERT INTO usuarios VALUES (?,?,?)""",data)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    crearBD()
    AgregarUser()
