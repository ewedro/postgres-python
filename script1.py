import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
query = """
INSERT INTO notes 
VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');
"""
cur.execute(query)
conn.commit()
cur.execute("SELECT * from notes;")
rows = cur.fetchall()
print(rows)
conn.close()
