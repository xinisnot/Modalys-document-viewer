# Get mlys object from the directory of the Modays package
# "modalisp", "description" and "url" were entered manually.

import glob
import csv

files       = glob.glob('/Users/Shared/Max 8/Packages/modalys/externals/*/*.mxo')
mxos        = []
output_name = 'mlys_object_list.csv'
keys        = [ 'name', 'category', 'modalisp', 'description', 'url' ]

for file in files:
    mxo_category = file.split('/')[-2]
    mxo_name     = file.split('/')[-1]
    info         = { keys[0]: mxo_name, keys[1]: mxo_category, keys[2]: "", keys[3]: "", keys[4]: "" }    
    mxos.append(info)

with open(output_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    writer.writerows(mxos)