# bus_waiting_times.py
#
# Example using requests to web, geting, parsing and printing from xml

import urllib.request

bus_stop_predictions = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')

from xml.etree.ElementTree import parse

doc = parse(bus_stop_predictions)

bus_stop = doc.find('./nm').text
print('Bus stop name:', bus_stop)
print('--------------')

# "pre" node have the bus and route info
for pre in doc.findall('./pre'):
    route_number = pre.find('./rn').text
    destination = pre.find('./fd').text
    estimated_time = pre.find('./pt').text
    
    print(f'Ruta #: {route_number}')
    print(f'Destination: {destination}')
    print(f'Estimated arrival time: {estimated_time}')
    print('--------------')