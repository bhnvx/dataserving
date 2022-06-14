import pika
import yaml
import json

from server import Server


with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def main():
    server = Server()

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config['RabbitMQ']['Host'])
    )
    channel = connection.channel()

    channel.queue_declare(queue=config['RabbitMQ']['Queue'])

    def callback(ch, method, properties, body):
        try:
            data = json.loads(body)
            Server.handler(data)
        except Exception as e:
            print(e)

    channel.basic_consume(queue=config['RabbitMQ']['Queue'], on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C. ')
    channel.stop_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted.')
        try:
            import sys
            sys.exit(0)
        except SystemExit:
            import os
            os._exit(0)