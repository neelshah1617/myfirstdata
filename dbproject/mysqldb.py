#! /usr/bin/python 

import MySQLdb

db=MySQLdb.connect(host="localhost",user="root",passwd="Sh@h637187",db="world")
cur = db.cursor()


 
cur.execute("select name from country where code like \"IND\"")
for i in cur.fetchall():
 print i[0]

cur.close()
db.close()