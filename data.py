import sqlite3
import mysql.connector
import webbrowser
conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE lifegraph_data
         (ID INT PRIMARY KEY     NOT NULL,
         DEVICE           TEXT    NOT NULL,
         VOLUME           INT     NOT NULL,
         PRESSURE         INT     NOT NULL,
         TEMPERATURE      INT  NOT NULL);''')

conn.execute("INSERT INTO lifegraph_data (ID,DEVICE,VOLUME,PRESSURE,TEMPERATURE) \
      VALUES (1, 'DEVICE A', 200, '50', 298 )");

conn.execute("INSERT INTO lifegraph_data (ID,DEVICE,VOLUME,PRESSURE,TEMPERATURE) \
      VALUES (2, 'DEVICE B', 500, '60', 300 )");

conn.execute("INSERT INTO lifegraph_data (ID,DEVICE,VOLUME,PRESSURE,TEMPERATURE) \
      VALUES (3, 'DEVICE C', 1000, '40', 310 )");


conn = mysql.connector.connect(user='root', password='',
                              host='localhost',database='test')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select_device = """SELECT * FROM lifegraph_data"""
cursor = conn.cursor()
cursor.execute(select_device)
result = cursor.fetchall()

p = []

tbl = "<div><bar>DEVICE</bar><bar>VOLUME</bar><bar>PRESSURE</bar><bar>TEMPERATURE</bar></div>"
p.append(tbl)

for row in result:
    a = "%s"%row[1]
    p.append(a)
    b = "%s"%row[2]
    p.append(b)
    c = "%s"%row[3]
    p.append(c)

filename = 'BarChart.js'
def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)
webbrowser.open(filename)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")
