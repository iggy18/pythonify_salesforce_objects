from builder import Builder
from config import USR, PASSWORD, TOKEN, OBJECT_NAMES
from simple_salesforce import Salesforce
import os

def create_module():
    os.mkdir('sObjects')
    os.mknod('sObjects/__init__.py')

print(USR, PASSWORD, TOKEN)
sf = Salesforce(username=USR, password=PASSWORD, security_token=TOKEN)

def get_all_objects():
    all_objs = []
    metadata = sf.describe()
    for obj in metadata['sobjects']:
        all_objs.append(obj['name'])
    return all_objs

if not OBJECT_NAMES:
    OBJECT_NAMES = get_all_objects()

def get_field_names_for(sObject):
    field_names = {}
    metadata = getattr(sf, sObject).describe()
    fields = metadata.get('fields')
    
    for field in fields:
        field_names[field['name']] = None
    
    return field_names

if not os.path.exists('sObjects'):
    create_module()

for obj in OBJECT_NAMES:
    with open('sObjects/{}.py'.format(obj), 'w') as f:
        print(f'getting field names for {obj}')
        try:
            fields = get_field_names_for(obj)
            class_text = Builder(obj, fields)
            finished = class_text.results()
            for line in finished:
                f.write(line)
        except Exception as e:
            print("encountered an error with the request for {}.".format(obj))
            continue