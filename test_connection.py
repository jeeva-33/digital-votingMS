from backend.db_connections import get_connection

try:
    conn = get_connection()
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
