import json
from memory import retain_incident

with open("data/past_incidents.json") as f:
    incidents = json.load(f)

for i in incidents:
    retain_incident(i["customer_id"], i["text"])
    print("stored for", i["customer_id"])

print("Seeded successfully!")