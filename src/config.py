import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import streamlit as st
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

CHROMA_DB_PATH = "./chroma_db"

CHUNK_SIZE = 400
CHUNK_OVERLAP = 40

TOP_K_RESULTS = 3

CONFIDENCE_THRESHOLD = 0.45

SENSITIVE_KEYWORDS = [
    "billing",
    "refund",
    "chargeback",
    "legal",
    "lawsuit",
    "account hacked",
    "account modification"
]

