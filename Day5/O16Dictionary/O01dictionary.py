'''
A dictionary is unordered collection of items 
with key value pairs
1. ordered
2. mutable
3. mixed
'''
import pprint
summit = {'k2': "India",
          "Everest": 'Nepal',
          "Kilimanjaro": 'Tanzania',
          "Alps": 'Switzerland'}
pprint.pprint(summit, indent=True)
print(type(summit))

print("_" * 50)
d1 = {}
d2 = dict()
print(type(d1), type(d2))
print("_" * 50)
# dictionary mixed type
summit = {'k2': "India",
          "Everest": 'Nepal',
          "Kilimanjaro": 'Tanzania',
          "Alps": 'Switzerland',
          201: ["nilgiri", "Nandi Hills", "Antara Ganga"],
          202: {"ulagamathi", "nayakanari", "Jansa Pahad"},
          203: ('blue', 'red', 'aqua'),
          204: {1: "Amitabh", 2: "Amir", 3: "Rajni"}
          }

pprint.pprint(summit, indent=True)
