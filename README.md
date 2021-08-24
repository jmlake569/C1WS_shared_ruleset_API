# C1WS_shared_ruleset_API

1.	Download the Deep Security SDK (Deep Security Library).
  a.	API Reference: https://cloudone.trendmicro.com/docs/workload-security/api-reference/
  b.	Python SDK: https://cloudone.trendmicro.com/docs/workload-security/sdk-python/
  c.	Must have Python 3.4+
2.	Use list_computers.py to find the ID of the computer so we can use that to generate a software inventory list.
3.	Once we find the ID of the computer, we then use the create_software_inventory.py script to start building the inventory list of the computer (this should be a computer that matches the inventory of others).
  a.	You can then list the software inventories list_software_inventory.py (when we run the command to create the inventory list it should send a JSON response with the new inventory ID it created). 
4.	Create the shared ruleset by running the create_shared_ruleset.py script. The settings will then appear in the console, and you can assign them to other computers. 
