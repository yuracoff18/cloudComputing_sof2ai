from sof2ai.shared.database import get_connection, get_cursor


def create_user(email: str, name: str, password: str):
    conn = get_connection()
    cursor = get_cursor(conn)

    query = """
        INSERT INTO users (email, name, PASSWORD_)
        VALUES (%s, %s, %s)
        RETURNING id, email, name;
    """

    cursor.execute(query, (email, name, password))
    user = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return user


def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)

    query = """
        SELECT id, email, name
        FROM users
        WHERE id = %s;
    """

    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def get_user_by_email(email: str):
    conn = get_connection()
    cursor = get_cursor(conn)

    query = """
        SELECT id, email, name
        FROM users
        WHERE email = %s;
    """

    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def delete_user(user_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
    DELETE FROM users
    WHERE id = %s
    """
    
    cursor.execute(query, (user_id,))
    deleted = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return deleted
    