import psycopg2
from psycopg2.extras import RealDictCursor

from sof2ai.shared import config

def get_connection():
    return psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        port=config.DB_PORT,
        options="-c search_path=sof2ai"
    )

def get_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)