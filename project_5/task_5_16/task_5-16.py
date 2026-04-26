import psycopg2
conn = psycopg2.connect(
    host="localhost",      
    port="5432",           
    database="testdb",     
    user="postgres",       
    password="example"        
)

cursor = conn.cursor()

cursor.execute("SELECT id, name, category FROM products LIMIT 5;")

rows = cursor.fetchall()

print("Результат запроса:")
print("-" * 50)
for row in rows:
    print(f"ID: {row[0]}, Название: {row[1]}, Категория: {row[2]}")

cursor.close()
conn.close()