from app.core.database import engine
try:
    conn = engine.connect(); 
    print('DB Engine Connected!')
    conn.close()
except Exception as e:
    print(f"An Error Occur while Connecting with Database : {e}")