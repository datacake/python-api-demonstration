# Python API Demonstration

Example for massive IoT deployments on Datacake using:

- Custom product and device type
- Data ingestion via JSON HTTP feed and custom URL
- Decoding of payload and routing to device
- GraphQL API for creation and access of devices

This shows you how you can use Datacake Backend for your:

- Custom App development
- Custom IoT projects

## Files and Contents

### device-simulator.py

This script simulates sensor data flow and sends it to Datacake API URL for custom API product on Datacake.

### datacake-device-decoder.js / -auto.js

JavaScript code for API HTTP decoder on Datacake API product.

### device-reader.py

This script reads all devices from Datacake Workspace and parses as Python object including primary, secondary field roles, basic chart data, etc.