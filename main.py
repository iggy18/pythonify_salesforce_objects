from builder import Builder
from config import USR, PASSWORD, TOKEN, OBJECT_NAMES
from simple_salesforce import Salesforce

print(USR, PASSWORD, TOKEN)
sf = Salesforce(username=USR, password=PASSWORD, security_token=TOKEN)

def get_field_names_for(sObject):
    field_names = {}
    metadata = getattr(sf, sObject).describe()
    fields = metadata.get('fields')
    
    for field in fields:
        field_names[field['name']] = None
    
    return field_names


with open('results.py', 'w') as f:
    for obj in OBJECT_NAMES:
        fields = get_field_names_for(obj)
        class_text = Builder(obj, fields)
        finished = class_text.results()
        for line in finished:
            f.write(line)
