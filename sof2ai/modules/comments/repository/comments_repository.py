from sof2ai.shared.database import get_connection, get_cursor
from sof2ai.shared.rabbitMq import send_message

def create_comment(post_id: int, user_id: int, content: str, parent_comment_id: int | None):
    conn = get_connection()
    cursor = get_cursor(conn)

    query = """
        INSERT INTO comments (post_id, user_id, content, parent_comment_id, status)
        VALUES (%s, %s, %s, %s, 'PENDING')
        RETURNING id, post_id, user_id, content, parent_comment_id, status, created_at;
    """

    cursor.execute(query, (post_id, user_id, content, parent_comment_id))
    comment = cursor.fetchone()

    if comment is None:
        raise Exception("No se pudo crear el comentario")
    
    send_message(content, comment['id'], "comments")
    
    conn.commit()
    cursor.close()
    conn.close()

    return comment

def delete_comment(comment_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
        DELETE FROM comments
        WHERE id = %s
        RETURNING id, post_id, content
    """
    
    cursor.execute(query, (comment_id,))
    delete = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return delete
    
def update_comment(content: str, comment_id: int):
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
        UPDATE comments
        SET content = %s
        WHERE id = %s
        RETURNING id, post_id, content
    """
    
    cursor.execute(query, (content, comment_id))
    updated = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    send_message(content, comment_id, "Comments")
    
    return updated
    
    
def get_all_by_post_id(post_id:int):
    conn = get_connection()
    cursor = get_cursor(conn)
    
    query = """
        SELECT * FROM comments
        WHERE post_id = %s
    """
    
    cursor.execute(query, (post_id,))
    allByPostId = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return allByPostId
    