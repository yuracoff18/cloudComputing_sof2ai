import pika
import os
import json


def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.environ.get("SERVICE", "localhost"),
            port=int(os.environ.get("PORT", 5672)),
            credentials=pika.PlainCredentials(
                os.environ.get("USER", "user"),
                os.environ.get("PASSWORD", "admin")
            )
        )
    )


def send_message(body: str, id: int, src: str, title=''):

    connection = get_connection()

    channel = connection.channel()

    channel.queue_declare(
        queue="messages",
        durable=True,
    )
    
    payload = {
        'id': id,
        'content': body,
        'title': title,
        'source': src
    }

    channel.basic_publish(
        exchange="",
        routing_key="messages",
        body=json.dumps(payload),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print(f"Mensaje enviado: {body}")

    connection.close()