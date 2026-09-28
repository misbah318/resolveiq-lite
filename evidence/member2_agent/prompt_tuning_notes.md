# Prompt tuning notes

## Round 1 (baseline prompt): 3 pass, 11 fail
- Invented delivery timelines ("2-3 business days", "5-8 days")
- Promised actions ("I can start a refund", "we'll email you the tracking number")
- Acted as if it could look up tracking/shipment status
- Claimed to have the customer's address "on file"

## Round 2: 13 pass, 1 fail
- Added rules against lookups, invented timelines, "on file", photo requests
- Remaining issue: "We've logged your request" (a claim not in memory)

## Round 3: 14 pass, 0 fail
- Added rules against "logged/recorded/approved" and against promising outcomes

## Round 4: 13 pass, 1 fail
- New failure: "Thank you for confirming it's order A104" (customer never confirmed)
- Cause: my earlier rule asked the model to request order confirmation, and it
  treated the request as already answered
- Fix: rule against claiming the customer confirmed anything not in the message or history

## Round 5: 14 pass, 0 fail (final)
- Added rules: never claim the customer confirmed something, do not assume a
  replacement was shipped, and describe the support-team handoff as a next step
- The "thank you for confirming A104" failure is gone
- Remaining borderline: "they'll get back to you" wording, accepted as a limitation

## Final result
- All replies under 90 words
- WITH MEMORY uses A104 and asks the customer to confirm it
- WITHOUT MEMORY asks for the order number and never pretends to remember
- No invented tracking, dates, or policies

## Model fallback finding
- qwen/qwen3-32b (recommended in the project plan) was retired by Groq on 07/17/26.
- Fallback test returned 404 for it, so the chain had no working second model.
- Replaced it with openai/gpt-oss-20b and qwen/qwen3.8-27b (both tested and working).
- Final chain in agent.py: openai/gpt-oss-120b, openai/gpt-oss-20b, qwen/qwen3.8-27b.
- Verified: fake first model -> fallback model answered; all models fake -> safe fallback text.

## Known limitations
- The agent says it will "pass this to our support team for review", but this prototype has
  no real ticketing system behind that wording.
- Model wording varies slightly between runs, so results were judged across several rounds.
- Groq retires models regularly, so the model list may need updating later.