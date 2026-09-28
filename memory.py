import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY"),
)

def _bank(customer_id):
    return "resolveiq-" + customer_id.lower()

def retain_incident(customer_id, text):
    client.retain(
        bank_id=_bank(customer_id),
        content=text,
        context="customer support interaction",
    )

def recall_incidents(customer_id, query):
    try:
        results = client.recall(
            bank_id=_bank(customer_id),
            query=query
        )
        return [r.text for r in results.results]
    except Exception:
        return []