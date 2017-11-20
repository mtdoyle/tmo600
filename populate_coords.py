HIGH_LAT="49.38407"
LOW_LAT="25.11567"
EAST="-66.94975"
WEST="-124.73004"

current_lat=HIGH_LAT
current_lon=WEST

coords = []

while float(current_lon) < float(EAST):
    coords.append({'lat':current_lat,
                   'lon':current_lon})
    if float(current_lat) <= float(LOW_LAT):
        current_lat = HIGH_LAT
        if float(current_lon) < float(EAST):
            current_lon = float(current_lon) + 0.1
        else:
            break
    else:
        current_lat = float(current_lat) - 0.1

f = open('coords.txt', 'w')
for i in coords:
    f.write("{0},{1}\n".format(i['lat'], i['lon']))
f.close()