from src.rag.rag_service import Document_Parser

file_path = "sample_data/Adaptive Screen Capture Video Analysis.pdf"
parser = Document_Parser(file_path)

info = parser.get_document_info()
doc_obj = parser.create_document_object()


corpus = parser.get_corpus()

# print(corpus[0])

import re

text = re.sub(r'\s+', ' ', corpus)
text.strip()

words = text.split()
print(len(words))

# chunks = []
# start = 0
# while start < len(corpus)
def chunk_words(words, chunk_size=300, overlap=20):
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap  # sliding window

    return chunks

chunks = chunk_words(words)
print("Total chunks:", len(chunks))
print(chunks[17])





from src.rag.sent_transformer import sentence_embeddder
embeddings_corpus = []

for i,c in enumerate(chunks):
    print(f'total chunks {len(chunks)}')
    embeddings = sentence_embeddder.encode(c)
    embeddings_corpus.append(embeddings)


