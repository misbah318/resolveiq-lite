from memory import retain_incident, recall_incidents

retain_incident(
    "C999",
    "Customer said: My order A104 arrived damaged. "
    "I want a replacement. Support replied: replacement requested."
)

print(
    "Same customer:",
    recall_incidents(
        "C999",
        "I still haven't received my replacement"
    )
)

print(
    "New customer:",
    recall_incidents(
        "C998",
        "Where is my order?"
    )
)