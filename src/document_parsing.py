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