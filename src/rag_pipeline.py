import os
import chromadb

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import (
    CHROMA_DB_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K_RESULTS
)


class LocalRAGPipeline:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.chroma_client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.collection = self.chroma_client.get_or_create_collection(
            name="support_kb"
        )

    def load_documents(self, folder="data"):

        docs = []

        for filename in os.listdir(folder):

            filepath = os.path.join(folder, filename)

            try:

                # Skip PDF temporarily
                if filename.endswith(".pdf"):
                    continue

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

                docs.append({
                    "source": filename,
                    "content": text
                })

            except Exception as e:

                print(
                    f"Error loading {filename}: {e}"
                )

        return docs

    def get_embedding(self, text):

        return self.embedding_model.encode(
            text
        ).tolist()

    def chunk_documents(self, docs):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        chunks = []

        for doc in docs:

            split_chunks = splitter.split_text(
                doc["content"]
            )

            for idx, chunk in enumerate(split_chunks):

                chunks.append({
                    "id": f"{doc['source']}_{idx}",
                    "text": chunk,
                    "source": doc["source"]
                })

        return chunks

    def build_vector_store(self):

        docs = self.load_documents()

        chunks = self.chunk_documents(docs)

        print(f"Chunks Created: {len(chunks)}")

        for chunk in chunks:

            embedding = self.get_embedding(
                chunk["text"]
            )

            try:

                self.collection.add(
                    ids=[chunk["id"]],
                    embeddings=[embedding],
                    documents=[chunk["text"]],
                    metadatas=[
                        {
                            "source":
                            chunk["source"]
                        }
                    ]
                )

            except Exception:
                pass

        print("Vector Store Ready")

    def retrieve_context(
        self,
        query,
        top_k=TOP_K_RESULTS
    ):

        query_embedding = self.get_embedding(
            query
        )

        results = self.collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=top_k
        )

        retrieved = []

        if results["documents"]:

            for i in range(
                len(results["documents"][0])
            ):

                retrieved.append({

                    "text":
                    results["documents"][0][i],

                    "source":
                    results["metadatas"][0][i]["source"],

                    "score":
                    1.0
                })

        return retrieved