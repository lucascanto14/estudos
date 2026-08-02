#importando sql
import sqlite3 as lite

#criando conexao 
con = lite.connect('dados.db')

#criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE infocam(id INTEGER PRIMARY KEY AUTOINCREMENT, fs TEXT, fe TEXT, fN TEXT, sN TEXT, sec TEXT, av TEXT, pix TEXT, bmax TEXT, bN TEXT, Lmax TEXT, mag TEXT, cdeg TEXT, cdegmax TEXT, io TEXT, raP TEXT, dcP TEXT, av1 TEXT, x1 TEXT, y1 TEXT, x2 TEXT, y2 TEXT, az1 TEXT, ev1 TEXT, az2 TEXT, ev2 TEXT, azm TEXT, evm TEXT, ra1 TEXT, dc1 TEXT, ra2 TEXT, dc2 TEXT, ram TEXT, dcm TEXT, class TEXT, m INTEGER, dr REAL, dv REAL, Vo REAL, lng1 REAL, lat1 REAL, h1 REAL, dist1 REAL, gd1 REAL, azL1 REAL, evL1 REAL, lng2 REAL, lat2 REAL,h2 REAL , dist2 REAL , gd2 REAL , len REAL , GV REAL , rao REAL , dco REAL , Voo REAL , rat REAL , dct REAL , memo TEXT)")
	