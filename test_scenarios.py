from memory import retain_incident, recall_incidents
from agent import generate_reply

SCENARIOS = [
    ("C101", "My order A104 arrived damaged. I want a replacement."),
    ("C101", "I still haven't received my replacement."), # must recall A104
    ("C102", "I still haven't received my replacement."), # must NOT mention A104
    ("C106", "Hi, where is my order?"),                  # customer with little/no history
    ("C101", "Any update?"),                             # vague follow-up
]

for cid, q in SCENARIOS:
    mem = recall_incidents(cid, q)
    reply = generate_reply(cid, q, mem)
    retain_incident(cid, "Customer said: " + q + "\nSupport replied: " + reply)
    print("=" * 60)
    print(cid, "|", q)
    print("MEMORY:", mem)
    print("REPLY :", reply)