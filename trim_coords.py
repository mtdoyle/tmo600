import fiona
import pika
import shapely.geometry
import multiprocessing
import write_to_db

def process_coords(coords):
    with fiona.open("shapefile/cb_2016_us_nation_5m.shp") as fiona_collection:
        # In this case, we'll assume the shapefile only has one record/layer (e.g., the shapefile
        # is just for the borders of a single country, etc.).
        shapefile_record = fiona_collection.next()

        # Use Shapely to create the polygon
        shape = shapely.geometry.asShape(shapefile_record['geometry'])
        # print "processing {0}".format(coords)
        lat = coords.split(',')[0]
        lon = coords.split(',')[1].rstrip()
        point = shapely.geometry.Point(float(lon),float(lat)) # longitude, latitude

        if shape.contains(point):
            write_to_db.write_coords_to_db(lat, lon)


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
    workers = 8
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