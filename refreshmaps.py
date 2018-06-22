import json
import glob
import os
from collections import OrderedDict

minKey = 13
try:
    with open('maps.json') as json_file:
        data = json.load(json_file, object_pairs_hook=OrderedDict)
        print('maps.json found!')

except:
    print("No maps.json found. One will be created.")
    data = {"maps":[{"id":13,"name":"TEST","custom":True,"oreGen":True}]}

else:
        minKey = min(g['id'] for g in data['maps'])

finally:
    print('Scanning maps folder. . .')
    print('Renaming maps to lowercase. . .')
    for x in glob.glob('*.png'):
        os.rename(src=x,dst=x.lower())
    print('Done.')
    dirMaps = ([os.path.basename(x[:-4]) for x in glob.glob('*.png')])
    newMapJson = {'maps': []}
    print("Rebuilding map list with these maps:")

    for p in dirMaps:
        dirMaps = ([os.path.basename(x[:-4]) for x in glob.glob('*.png')])
        if 'oregenoff' in p:
            map = {'id': (minKey), 'name': p, 'custom': True, 'oreGen': False}
        else:
            map = {'id':(minKey), 'name':p, 'custom':True,'oreGen':True}
        print(p)
        newMapJson['maps'].append(map)
        minKey = minKey+1

    #[value for key, value in programs.items() if 'new york' in key.lower()]

    with open('maps.json', 'w') as outfile:
        json.dump(newMapJson, outfile, indent=4)
    print ("\nDone!")
    print ("Don't forget to restart the server to load the new maps.")