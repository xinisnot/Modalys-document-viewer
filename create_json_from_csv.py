import pandas as pd
import json


# create a dictionary of attributes in the following format

df_mlys_attr = pd.read_csv('work/mlys_attributes.csv').fillna('')
dict_attr    = {}

for mlys in df_mlys_attr['object'].unique():
    df_mlys  = df_mlys_attr.query('object == @mlys').drop('object', axis=1)
    d_tmp    = {}
    
    for index, row in df_mlys.iterrows():
        d_tmp[row[0]] = { 'unit': row[1], 'description': row[2], 'parameter': row[3], 'type': row[4] }
    
    dict_attr[mlys] = d_tmp


# create a dictionary to be used in the Max patch and save it as json
    
df_mlys_list  = pd.read_csv('work/mlys_object_list.csv', index_col=0).fillna('')
df_categories = df_mlys_list['category'].unique()
dict_mlys     = {}

for category in df_categories:
    d = df_mlys_list.query('category == @category').drop('category', axis=1).to_dict(orient='index')
    
    for mlys in d:
        d[mlys]['attribute'] = dict_attr[mlys]
        
    dict_mlys[category] = d

with open('work/mlys_object_list.json', mode='w') as f:
    json.dump(dict_mlys, f)