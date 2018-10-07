import sqlite3



conn = sqlite3.connect('db/bl_log.db')
cur = conn.cursor()

print "....::Musteriler::...."
cur.execute("SELECT * FROM Log")
customer_rows = cur.fetchall()
for customer in customer_rows:
    print(customer)

print "....::Anonim Musteriler::...."
cur.execute("SELECT * FROM Log_Anonymus")
anonymus_rows = cur.fetchall()
for an_customer in anonymus_rows:
    print(an_customer)