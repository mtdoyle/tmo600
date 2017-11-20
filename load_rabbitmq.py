import pika
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'coords.txt'

f = open(filename,'r')

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

channel = connection.channel()

channel.queue_delete(queue='tmo600')

channel.queue_declare(queue='tmo600', durable=True)

channel.queue_purge(queue='tmo600')

for item in f.readlines():
    channel.basic_publish(exchange='',
                          routing_key='tmo600',
                          body=item.strip(),)


connection.close()
