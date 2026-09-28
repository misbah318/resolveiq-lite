import json
import streamlit as st

from memory import retain_incident, recall_incidents
from agent import generate_reply


# ---------------------------------------------------------
# APP CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="ResolveIQ Lite",
    layout="wide"
)

st.title("ResolveIQ Lite: support agent with memory")
st.caption(
    "Prototype with fictional customers and orders. "
    "No real refunds or order changes."
)


# ---------------------------------------------------------
# LOAD CUSTOMERS
# ---------------------------------------------------------

with open("data/customers.json") as f:
    customers = {
        c["id"]: c["name"]
        for c in json.load(f)
    }


# ---------------------------------------------------------
# SESSION HISTORY
# ---------------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

cid = st.sidebar.selectbox(
    "Customer",
    list(customers),
    format_func=lambda c: c + " - " + customers[c]
)

use_memory = st.sidebar.toggle(
    "Hindsight memory ON",
    value=True
)

if st.sidebar.button("Start new session"):
    # Clears the chat screen only.
    # It does NOT delete Hindsight memory.
    st.session_state.history = []
    st.rerun()

st.sidebar.caption(
    "New session wipes the screen only. "
    "Memory in Hindsight stays."
)


# ---------------------------------------------------------
# CUSTOMER MESSAGE
# ---------------------------------------------------------

query = st.text_area(
    "Customer message",
    placeholder="I still haven't received my replacement."
)


# ---------------------------------------------------------
# SEND MESSAGE
# ---------------------------------------------------------

if st.button("Send", type="primary") and query.strip():

    with st.spinner("Recalling memory and writing reply..."):

        try:
            # Recall previous incidents if memory is enabled
            memories = (
                recall_incidents(cid, query)
                if use_memory
                else []
            )

            # Generate response
            reply = generate_reply(
                cid,
                query,
                memories
            )

            # Store this interaction
            retain_incident(
                cid,
                "Customer said: " + query +
                "\nSupport replied: " + reply
            )

            # Save to current Streamlit session
            st.session_state.history.append(
                (
                    cid,
                    query,
                    reply,
                    memories,
                    use_memory
                )
            )

        except Exception as e:
            st.error(
                "Something went wrong: " + str(e)
            )


# ---------------------------------------------------------
# THREE MAIN PANELS
# ---------------------------------------------------------

if st.session_state.history:

    _, q, reply, mems, used = (
        st.session_state.history[-1]
    )

    c1, c2, c3 = st.columns(3)

    # Panel 1: Current query
    with c1:
        st.subheader("1. Current query")
        st.info(q)

    # Panel 2: Generated response
    with c2:
        st.subheader("2. Generated response")
        st.success(reply)

    # Panel 3: Recalled memory
    with c3:
        st.subheader("3. Recalled memory")

        if not used:
            st.warning("Memory is OFF for this message")

        elif mems:
            for m in mems:
                st.write("- " + m)

        else:
            st.write(
                "No prior memory found for this customer."
            )


# ---------------------------------------------------------
# SESSION HISTORY
# ---------------------------------------------------------

if st.session_state.history:

    with st.expander("Session history"):

        for cid_, q_, r_, m_, u_ in st.session_state.history:

            st.write(
                "**" + cid_ + "**: " + q_
            )

            st.write(
                "-> " + r_
            )