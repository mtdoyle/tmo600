import fiona
import shapely.geometry

f = open('coords.txt','r')
g = open('good_coords.txt','w')
with fiona.open("shapefile/cb_2016_us_nation_5m.shp") as fiona_collection:

    # In this case, we'll assume the shapefile only has one record/layer (e.g., the shapefile
    # is just for the borders of a single country, etc.).
    shapefile_record = fiona_collection.next()

    # Use Shapely to create the polygon
    shape = shapely.geometry.asShape(shapefile_record['geometry'])

    for coords in f.readlines():
        # print "processing {0}".format(coords)
        lat = coords.split(',')[0]
        lon = coords.split(',')[1].rstrip()
        point = shapely.geometry.Point(float(lon),float(lat)) # longitude, latitude

        if shape.contains(point):
            g.write("{0}\n".format(coords))

f.close()
g.close()
