import json
import glob
import os

with open('maps.json') as json_file:
    data = json.load(json_file)
with open('maps.bak', 'w') as outfile:
    json.dump(data, outfile)

dirMaps = ([os.path.basename(x[:-4]) for x in glob.glob('*.png')])
minKey = min(g['id'] for g in data['maps'])
newMapJson = {'maps': []}

print("Rebuilding map list with these maps:")

for p in dirMaps:
    print(p)
    map = {'id':(minKey), 'name':p, 'custom':True}
    newMapJson['maps'].append(map)
    minKey = minKey+1

with open('maps.json', 'w') as outfile:
    json.dump(newMapJson, outfile)
print ("Done!")
print ("Don't forget to restart the server to load the new maps.")