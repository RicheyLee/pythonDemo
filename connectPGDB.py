__author__ = 'Richey'
import psycopg2
import json

conn = psycopg2.connect(database="shoudao2_ht", user="shoudao2", password="shoudao2@001", host="61.163.77.102",
                        port="30000")

print "Opened database successfully"
cur = conn.cursor()

cur.execute("SELECT username, userid, roleid, realname,departid  from sd2_admin where username = 'kanghong'")
rows = cur.fetchall()

x = []
for row in rows:
 info = {'username': row[0],"roleid": row[2], "userid": row[1], "realname": row[3],"departid":row[4]}
 x.append(info)
 m = {"all":len(x),"arr":x};
 list = json.dumps(m)
print list


print "Operation done successfully";
conn.close()
