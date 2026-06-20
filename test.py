from src.rag_pipeline import LocalRAGPipeline

rag = LocalRAGPipeline()

rag.build_vector_store()

results = rag.retrieve_context(
    "API authentication failed"
)

print(results)