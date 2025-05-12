import boto3
import psycopg2
import pandas as pd

# --- Configuración base de datos PostgreSQL ---
conn = psycopg2.connect(
    dbname="postgres_datos",
    user="postgres",
    password="utec",
    host="172.31.92.238",
    port="8005"
)

# --- Consulta de datos ---
query = "SELECT * FROM usuarios"
df = pd.read_sql(query, conn)
conn.close()

# --- Guardar como CSV ---
archivo_local = "data.csv"
df.to_csv(archivo_local, index=False)

# --- Subir a S3 ---
nombreBucket = "ctowa-output-02"
s3 = boto3.client('s3')
s3.upload_file(archivo_local, nombreBucket, archivo_local)

print("✅ Ingesta a S3 completada.")