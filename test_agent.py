from agent import generate_reply

mem = ["Customer said: My order A104 arrived damaged. I want a replacement."]
out = []

def run(label, query, memories):
    reply = generate_reply("C101", query, memories)
    line = f"{label}\nQUERY: {query}\nREPLY: {reply}\nWORDS: {len(reply.split())}\n"
    print(line); out.append(line)

q = "I still haven't received my replacement."
run("WITH MEMORY", q, mem)
run("WITHOUT MEMORY", q, [])

extras = [
    "Any update?",
    "Where is my order?",
    "I want a refund right now.",
    "Give me the tracking number.",
    "How many days does a replacement take?",
    "Was my replacement already shipped?",
]
for e in extras:
    run("EXTRA WITH MEMORY", e, mem)
    run("EXTRA WITHOUT MEMORY", e, [])

import os
os.makedirs("evidence/member2_agent", exist_ok=True)
with open("evidence/member2_agent/test_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))