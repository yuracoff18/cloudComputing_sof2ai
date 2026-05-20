from sof2ai.shared.database import get_connection, get_cursor
from sof2ai.shared.rabbitMq import send_message

def create_post(title: str, content: str, user_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)

    query = """
        INSERT INTO posts (title, content, user_id)
        VALUES (%s, %s, %s)
        RETURNING id, title, content, user_id, created_at;
    """

    cursor.execute(query, (title, content, user_id))
    post = cursor.fetchone()
    
    if post is None:
        raise Exception("No se pudo crear el post")
    
    conn.commit()
    send_message(post['content'], post["id"], 'Posts', title)
    cursor.close()
    conn.close()
    

    return post

def delete_post(post_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
        DELETE FROM posts
        WHERE id = %s
        RETURNING id, user_id, title, content
    """
    
    cursor.execute(query, (post_id,))
    deleted = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return deleted
    
def update_post(title: str, content: str, post_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
        UPDATE posts
        SET title = %s,
            content = %s
        WHERE id = %s
        RETURNING id, title, content, user_id, created_at;
    """
    
    cursor.execute(query, (title, content, post_id,))
    updated = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    send_message(content, post_id, "posts", title)
    
    return updated

def get_all_posts():
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
        SELECT * FROM posts
    """
    
    cursor.execute(query)
    posts = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return posts
    