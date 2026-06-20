import streamlit as st

from src.classifier import classify_customer_persona
from src.rag_pipeline import LocalRAGPipeline
from src.generator import generate_response
from src.escalator import (
    should_escalate,
    generate_handoff_summary
)

st.set_page_config(
    page_title="Persona Support Agent",
    page_icon="🤖"
)

st.title("🤖 Persona-Adaptive Customer Support Agent")

rag = LocalRAGPipeline()

if "db_built" not in st.session_state:

    rag.build_vector_store()

    st.session_state.db_built = True

query = st.text_area(
    "Enter Customer Query"
)

if st.button("Submit"):

    if query:

        persona_result = classify_customer_persona(
            query
        )

        persona = persona_result["persona"]

        retrieved_docs = rag.retrieve_context(
            query
        )

        escalate = should_escalate(
            query,
            retrieved_docs
        )

        st.subheader("Detected Persona")
        st.write(persona)

        st.subheader("Retrieved Sources")

        for doc in retrieved_docs:

            st.write(
                f"📄 {doc['source']}"
            )

        if escalate:

            st.error(
                "Escalation Required"
            )

            summary = generate_handoff_summary(
                persona,
                query,
                retrieved_docs
            )

            st.subheader(
                "Human Handoff Summary"
            )

            st.code(
                summary,
                language="json"
            )

        else:

            response = generate_response(
                query,
                persona,
                retrieved_docs
            )

            st.subheader(
                "Generated Response"
            )

            st.write(response)