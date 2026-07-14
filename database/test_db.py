try:
    import psycopg2
    psycopg2.connect('postgresql://admin:admin@localhost:5432/email_db')
    print('Connected!')

except Exception as e :
    print("Connection Failed !")
    print(f"\nError : {e}")