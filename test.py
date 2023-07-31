import psycopg2
host = 'localhost'
port = 5432
database = 'namma_yatri'
user = 'postgres'
password = 'Admin123'
connection = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Process the query result as needed
