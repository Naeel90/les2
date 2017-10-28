import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

Stationsdict = processXML('stationslijsten.xml')
Stations = Stationsdict['Stations']['Station']


print('Dit zijn de codes en types van de',len(Stations),'stations:')
for Station in Stations:
    print('{:5}-{}'.format(Station['Code'],Station['Type']))


print('')
print('Dit zijn alle stations met één of meer synoniemen:')
for Station in Stations:
    if Station['Synoniemen'] is not None:
        print('{:5}-{}'.format(Station['Code'],Station['Synoniemen']))


print('')
print('Dit is de lange naam van elk station:')
for Station in Stations:
    print('{:5}-{}'.format(Station['Code'],Station['Namen']['Lang']))
