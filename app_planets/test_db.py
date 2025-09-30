import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="Asdf12345",
        host="localhost",
        port="5432"
    )
    print("✅ Подключение успешно!")
    conn.close()
except Exception as e:
    print(f"❌ Ошибка: {e}")