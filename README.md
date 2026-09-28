# ResolveIQ Lite

An AI customer-support agent with persistent memory, built on Hindsight.

When a customer comes back, most support bots start from zero. ResolveIQ Lite remembers
the customer's earlier issues and uses them to answer the new message, even in a brand-new session.

> Prototype using fictional customers and orders. It does not connect to any real company
> database, process real customer data, issue refunds, or change orders.

## Demo

- Demo video: [ADD YOUTUBE LINK LATER]
- Screenshot: [ADD LATER: images/app-screenshot.png]

## The problem

Customers hate repeating their story. A support agent without memory cannot know that the
same customer reported a damaged order yesterday, so it gives a generic reply.

## What it does

1. Customer sends a message (for example: "My order A104 arrived damaged. I want a replacement.")
2. The agent answers and stores the interaction in Hindsight.
3. Later, even in a fresh session, the customer writes: "I still haven't received my replacement."
4. The agent recalls the earlier incident from Hindsight and replies with that context.
5. The screen shows the current query, the generated response, and the recalled memory.

Memory is stored in Hindsight, not in chat history, so it survives a new session.

## Architecture

![Architecture](images/architecture.png)

Flow: Customer message > Streamlit app > Hindsight recall > Groq LLM > Reply > Hindsight retain.

Design decision: one Hindsight memory bank per customer, so one customer never sees another
customer's history.

## How Hindsight is used

See [HINDSIGHT_USAGE.md](HINDSIGHT_USAGE.md) for the full explanation.

## Tech stack

- Hindsight (Vectorize) for persistent agent memory
- Groq LLM (openai/gpt-oss-120b, with qwen/qwen3-32b as fallback)
- Streamlit for the interface
- Python

## Setup

1. Clone the repo and open it in VS Code.
2. Create a virtual environment and install requirements:
   python -m venv venv
   venv\Scripts\activate        (Mac: source venv/bin/activate)
   pip install -r requirements.txt
3. Copy .env.example to .env and fill in:
   HINDSIGHT_BASE_URL, HINDSIGHT_API_KEY, GROQ_API_KEY
4. Seed the fictional history (run once): python seed_data.py
5. Start the app: streamlit run app.py
6. Open http://localhost:8501

## Try this demo

1. Select customer C101. Send: "My order A104 arrived damaged. I want a replacement."
2. Click "Start new session".
3. Send: "I still haven't received my replacement."
4. The recalled-memory panel shows the earlier damaged-order incident.
5. Switch memory OFF and send it again to see the generic reply.

## Data disclosure

All customers, orders, and past incidents are fictional and seeded for the demo.

## Limitations

- Fictional data only, with no real order system or ticketing integration.
- Single channel (text messages in the app).
- The agent never performs real refunds or order changes.

## Team

[Ms.Misbah,Ms.Heena Meheraj,Ms.Muhammad Shazia,Ms.Afreen Firdose,Ms.Jakka Ankali]