"""
Datacake Python GraphQL API example on how to read devices from workspace
"""
import requests

# Replace with your API token
headers = {"Authorization": "Token YOURTOKENHERE"}

# GraphQL Query helper function
def run_query(query):
    request = requests.post('https://api.datacake.co/graphql/', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

# Helper class to convert dictionary parsed from JSON to Python Object
class DictObj:
    def __init__(self, in_dict:dict):
        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
               setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
            else:
               setattr(self, key, DictObj(val) if isinstance(val, dict) else val)

# Actual Datacake Query
query = """
query {
  allDevices(inWorkspace:"YOURWORKSPACEUUIDHERE") {
    online
    verboseName
    id
    serialNumber
    roleFields {
      field {
        fieldName
        verboseFieldName
      }
      value
      chartData
      role
    }
  }
}
"""

# Run query
result = run_query(query) # Execute the query
my_obj = DictObj(result)

print(my_obj)

averageLevel = 0

for device in my_obj.data.allDevices:
    print("")
    print(f"Device: {device.verboseName}, Serial: {device.serialNumber}")
    for field in device.roleFields:
        print("Field: " +str(field.field.fieldName) + ", Value: " + str(field.value) + ", Chart: " + str(field.chartData))
        if field.role == "PRIMARY":
            averageLevel = averageLevel + float(field.value)
    print("")

print("")
print("Number of Sensors Total: " + str(len(my_obj.data.allDevices)))
print("")

averageLevel = averageLevel / len(my_obj.data.allDevices)

print("Average Level: " + str(averageLevel))
print("")