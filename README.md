# C1WS_shared_ruleset_API

1.	Download the Deep Security SDK (already included as a zip in this repo - dsm-py-sdk.zip).
2.	Python SDK: https://cloudone.trendmicro.com/docs/workload-security/sdk-python/
3.	API Reference: https://cloudone.trendmicro.com/docs/workload-security/api-reference/
4.	Must have Python 3.4+
5.	Use list_computers_id.py to find the ID of the computer so we can use that to generate a software inventory list.
6.	Once we find the ID of the computer, we then use the create_software_inventory.py script to start building the inventory list of the computer (this should be a computer that matches the inventory of others).
7.	You can then list the software inventories list_software_inventory.py (when we run the command to create the inventory list it should send a JSON response with the new inventory ID it created). 
8.	Create the shared ruleset by running the create_shared_ruleset.py script. The settings will then appear in the console, and you can assign them to other computers. 
