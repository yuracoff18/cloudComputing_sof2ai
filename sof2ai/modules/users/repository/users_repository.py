import os
import psycopg2

def get_user(id):

    dbconfig = {
        "host": os.environ.get("DB_HOST", "db"),
        "dbname": os.environ.get("DB_NAME", "sof2ai"),
        "user": os.environ.get("DB_USER", "userdb"),
        "password": os.environ.get("DB_PASSWORD", "tes1234"),
        "port": os.environ.get("DB_PORT", "5432")
    }

    conn = psycopg2.connect(**dbconfig)
    query = """
        SELECT
            id,
            "name",
            email,
            active,
            verified
        FROM
            sof2ai.users
        WHERE
            id = %s
    """

    values = [id]
    cursor = conn.cursor()
    cursor.execute(query, values)
    results = [row for row in cursor]
    return results


    