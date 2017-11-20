import requests
import ast
'''
var	signal2G			= +codedString.charAt(0);
		var signal3G			= +codedString.charAt(1);
		var signal4G			= +codedString.charAt(2) === 1 ? signal3G : 0;
		var signalBand4			= +codedString.charAt(3);
		var signalBand2			= +codedString.charAt(4);
		var signalBand12		= +codedString.charAt(5);
		var signalBand71		= +codedString.charAt(23);
		var roamSignal			= +codedString.charAt(7);
		var roamType			= +codedString.charAt(8);
		var verifiedType		= +codedString.charAt(9);
		var coverageDiffValue	= +codedString.charAt(20) ? +codedString.charAt(20) : 0;
		var signalU1900			= +codedString.charAt(21);
		var signalU2100			= +codedString.charAt(22);
'''

request_url="https://maps.t-mobile.com/Rest/pcc-getcoverage.php?point={0},{1}"

HIGH_LAT="49.38407"
LOW_LAT="25.11567"
EAST="-66.94975"
WEST="-124.73004"

current_lat=HIGH_LAT
current_lon=WEST

foundit = []

while float(current_lon) < float(EAST):
    print "checking coords: {0}, {1}".format(current_lat, current_lon)
    q = requests.get(request_url.format(current_lat,current_lon))
    result = ast.literal_eval(q.content)['response'][23]
    if int(result) > 0:
        foundit.append({'lat': current_lat,
                        'lon': current_lon,
                        'strength': result})
        print foundit

    if float(current_lat) <= float(LOW_LAT):
        current_lat = HIGH_LAT
        if float(current_lon) < float(EAST):
            current_lon = float(current_lon) + 0.1
        else:
            break
    else:
        current_lat = float(current_lat) - 0.1


print foundit


