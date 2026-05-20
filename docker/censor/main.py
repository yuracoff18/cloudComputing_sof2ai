import pika
import os
import json
import re
import httpx


def callback(ch, method, properties, body):
    try:
        data = json.loads(body)

        print("Mensaje recibido:", data)

        content = data["content"]
        post_id = data["id"]
        title = data["title"]
        src= data['source']

        pattern = r"\bm\s*a\s*l\s*o\b"

        found = (
            re.search(pattern, content, re.IGNORECASE)
            or re.search(pattern, title, re.IGNORECASE)
        )

        if not found:
            print("No encontró palabra prohibida")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        print("Palabra prohibida encontrada")
        print("Intentando borrar post:", post_id)

        response = httpx.delete(
            f"http://api:8000/{src}/{post_id}",
            timeout=10
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        print(f"Post eliminado: {post_id}")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print("Error en worker:", e)
        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=True
        )


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.environ.get("SERVICE", "localhost"),
            port=int(os.environ.get("PORT", 5672)),
            credentials=pika.PlainCredentials(
                os.environ.get("USER", "user"),
                os.environ.get("PASSWORD", "admin")
            )
        )
    )

    channel = connection.channel()

    channel.queue_declare(
        queue="messages",
        durable=True,
    )

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue="messages",
        on_message_callback=callback
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")

    channel.start_consuming()


if __name__ == "__main__":
    main()