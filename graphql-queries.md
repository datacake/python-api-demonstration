
### All Devices in Workspace with Field Role Data

```
query {
  allDevices(inWorkspace:"YOURWORKSPACEUUIDHERE") {
    online
    verboseName
    id
    serialNumber
    roleFields {
      id
      field {
        fieldName
        verboseFieldName
      }
      value
      chartData
    }
  }
}
```

### Devices with matching tags

```
query {
  allDevices(inWorkspace:"YOURWORKSPACEUUIDHERE", searchTags:["group-one"]) {
    online
    verboseName
    serialNumber
    roleFields {
      id
      field {
        fieldName
      }
      value
    }
  }
}
```

### Query Device and current measurement values


'''
query {
  device(deviceId:"YOURDEVICEUUIDHERE") {
    currentMeasurements(allActiveFields: true) {
      value
      field {
        verboseFieldName
      }
    }
  }
}
'''


### Create Devices

```
mutation {
  createApiDevices(input:{
    workspace:"YOURWORKSPACEUUIDHERE",
    plan:"free",
    planCode:"",
    productKind:EXISTING,
    existingProduct:"YOURPRODUCTIDHERE",
    devices:[{
      name:"Filllevel021",
      serial:"level0021"
    }],
  }) {
    ok
    devices {
      id
      verboseName
      serialNumber
      }
  }    
}

```
