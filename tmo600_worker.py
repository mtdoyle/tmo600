import requests
import pika
import ast
import write_to_db

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='tmo600', durable=True)
channel.basic_qos(prefetch_count=1)

def find600(coords):
    request_url="https://maps.t-mobile.com/Rest/pcc-getcoverage.php?point={0}"
    print "checking coords: {0}".format(coords)
    q = requests.get(request_url.format(coords))
    result = ast.literal_eval(q.content)['response'][23]
    if int(result) > 0:
        write_to_db.write_to_db(coords.split(',')[0],coords.split(',')[1],result)

def callback(ch, method, properties, body):
    print(" [x] checking %r" % body)
    find600(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='tmo600')

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()



