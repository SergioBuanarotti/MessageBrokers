import pika

with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')

    print(" [x] Sent 'Hello World!'")


