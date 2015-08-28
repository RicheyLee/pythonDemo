__author__ = 'Richey'
import psycopg2
import json

conn = psycopg2.connect(database="shoudao2_ht", user="shoudao2", password="shoudao2@001", host="61.163.77.102",
                        port="30000")

print "Opened database successfully"
cur = conn.cursor()

cur.execute("UPDATE sd2_admin set roleid = '5' where username ='kanghong'")
conn.commit
print "Total number of rows updated :", cur.rowcount

print "Operation done successfully";
conn.close()
