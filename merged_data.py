import mysql.connector
import os
import streamlit as st

def insert_merged_data_in_bulk(df, table_name='ClientesPQRS'):
    connection = None
    cursor = None

    try:
        # Establecer la conexión a la base de datos
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            st.success("Connected to the database successfully.")
            cursor = connection.cursor()

            # Crear la consulta de inserción
            insert_query = f"""
            INSERT INTO {table_name} (IdCliente, NombreCompleto, Sexo, Edad, Ciudad, Idpqrs, Tipo, FechaCaso, Asunto, Estado, FechaCierre, Urgencia)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Convertir los datos del DataFrame en una lista de tuplas
            merged_data = df[['IdCliente', 'NombreCompleto', 'Sexo', 'Edad', 'Ciudad', 'Idpqrs', 'Tipo', 'FechaCaso', 'Asunto', 'Estado', 'FechaCierre', 'Urgencia']].to_records(index=False).tolist()

            # Ejecutar la inserción en la base de datos
            cursor.executemany(insert_query, merged_data)
            connection.commit()

            st.success(f"{cursor.rowcount} rows inserted successfully.")

    except mysql.connector.Error as e:
        st.error(f"Error: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
