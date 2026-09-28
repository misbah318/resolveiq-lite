# How ResolveIQ Lite uses Hindsight memory

Memory is the core of this project. Without Hindsight the agent is a generic chatbot;
with it, the agent knows each customer's history.

## 1. Memory design: one bank per customer

Each customer gets their own Hindsight memory bank, named resolveiq-<customer id>
(for example resolveiq-c101).

Why: it keeps customers isolated. Customer C102 can never receive a reply based on
customer C101's damaged order.

## 2. Retain: what is saved and when

After every reply, app.py calls retain_incident() in memory.py, which calls Hindsight's
retain operation. The saved text looks like:

  Customer said: <customer message>
  Support replied: <agent reply>

We also seed a few fictional past incidents per customer (seed_data.py) so the demo shows
memory from earlier days.

## 3. Recall: what is fetched and when

Before writing a reply, app.py calls recall_incidents(customer_id, query) in memory.py,
which calls Hindsight's recall operation on that customer's bank. Recall runs BEFORE
retain, so the current message is not treated as an old one.

## 4. How recalled memory changes the reply

agent.py sends the customer's new message plus the recalled memories to the Groq LLM.
The system prompt tells the model to refer to the earlier incident, never to invent
details, and never to claim that a refund or replacement was actually processed.

## 5. What the user sees

The Streamlit screen has three panels: current query, generated response, and recalled
memory. A sidebar toggle turns Hindsight memory ON or OFF so the difference is visible.

## 6. Persistence across sessions

"Start new session" clears the chat on screen but not Hindsight. The customer's memory is
still there, which proves this is persistent memory and not chat history.

## 7. Result (before / after)

[ADD AFTER TESTING]
- Memory OFF: "I still haven't received my replacement" -> [paste generic reply]
- Memory ON: same message -> [paste reply that mentions order A104 and the replacement]

## 8. Files involved

- memory.py: retain_incident(), recall_incidents()
- agent.py: generate_reply()
- app.py: calls recall, then reply, then retain
- seed_data.py: loads fictional past incidents into Hindsight

## 9. Limitations

- Uses fictional data only.
- Recall quality depends on Hindsight's processing time; a brand-new memory may take a
  few seconds to become searchable.
