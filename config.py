from decouple import config

USR=config('USR')
PASSWORD=config('PASSWORD')
TOKEN=config('TOKEN')

# a list of objects to create classes for. 
# they are case sensitive and need to be the exact name of the object in salesforce
OBJECT_NAMES = []