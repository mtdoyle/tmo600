import fiona
import pika
import shapely.geometry
import multiprocessing
import write_to_db
from shapely.ops import cascaded_union, unary_union

def process_coords(coords):
    lat = coords.split(',')[0]
    lon = coords.split(',')[1].rstrip()
    for feat in fiona.open("shapefile/tl_2013_27_cousub.shp"):
        # Use Shapely to create the polygon
        shape = shapely.geometry.asShape(feat['geometry'])
        # print "processing {0}".format(coords)
        point = shapely.geometry.Point(float(lon),float(lat)) # longitude, latitude

        if shape.contains(point):
            write_to_db.write_mn_coords_to_db(lat, lon)


def callback(ch, method, properties, body):
    process_coords(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='tmo600', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='tmo600')

    print ' [*] Waiting for messages. To exit press CTRL+C'
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        pass


def work():
    workers = 6
    pool = multiprocessing.Pool(processes=workers)
    for i in xrange(0, workers):
        pool.apply_async(consume)

    # Stay alive
    try:
        while True:
            continue
    except KeyboardInterrupt:
        print ' [*] Exiting...'
        pool.terminate()
        pool.join()

if __name__ == '__main__':
    work()
