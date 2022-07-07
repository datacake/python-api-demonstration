"""
Datacake Python API Example on how to create device programmatically
"""
import requests
import time

# Replace with your API token
headers = {"Authorization": "Token YOURTOKENHERE"}

# Set device details here
number_of_sensors = 100
existing_product = "EXISTINGPRODUCTUUIDHERE"
workspace = "YOURWORKSPACEUUIDHERE"
serial_prefix = "level-"
name_prefix = "Fill Level Sensor "

# Function to call Datacake GraphQL query
def run_query(query):
    request = requests.post('https://api.datacake.co/graphql/', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

# Create devices
for i in range(1, number_of_sensors+1):

    # Query for creating devices
    query = """
        mutation {{
        createApiDevices(input:{{
            workspace:"{workspace}",
            plan:"free",
            planCode:"CODE",
            productKind:EXISTING,
            existingProduct:"{product}",
            devices:[
            {{
                name:"{name}",
                serial:"{serial}"
            }}     
            ]
        }}) {{
            ok
            devices {{
            id
            verboseName
            serialNumber
            }}
        }}    
        }}
    """.format(name=name_prefix+str(i), serial=serial_prefix+str(i), workspace=workspace, product=existing_product)    

    result = run_query(query) # Execute the query
    print(result)

    # Give Datacake API a bit of rest
    time.sleep(0.25)
