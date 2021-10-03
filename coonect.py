
conn = mysql.connector.connect(user='root', password='',
                              host='localhost',database='test')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")
