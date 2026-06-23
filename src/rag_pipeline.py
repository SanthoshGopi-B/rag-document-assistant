from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def generate_answer(docs, query):

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=200
    )

    return result[0]["generated_text"]