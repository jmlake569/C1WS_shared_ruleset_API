from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://cloudone.trendmicro.com/api'

# Authentication
configuration.api_key['api-secret-key'] = 'YOUR KEY HERE'

# Initialization
# Set Any Required Values
api_instance = deepsecurity.SoftwareInventoriesApi(deepsecurity.ApiClient(configuration))
software_inventory = deepsecurity.SoftwareInventory(PARAMETERS GO HERE SEE DOCUMENTATION Example: COMPUTER ID as integer)
api_version = 'v1'

try:
	api_response = api_instance.create_software_inventory(software_inventory, api_version)
	pprint(api_response)
except ApiException as e:
	print("An exception occurred when calling SoftwareInventoriesApi.create_software_inventory: %s\n" % e)
