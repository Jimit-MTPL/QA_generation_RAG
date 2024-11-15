from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from load_file import data_ingestion

Settings.llm = Ollama(model="llama3.2:1b", request_timeout=1000)

query = """
    You are tasked with generating high-quality, meaningful question-answer pairs from the context provided. The questions should cover all key points in the text, be diverse, and not repetitive. The answers should be detailed, conversational, accurate, and provide explanations where necessary. Avoid using wording that directly refers back to the text (like "according to the text"). Ensure each question is unique and comprehensive.

    Format your response like this:
    Question: [Insert question here]
    Answer: [Insert detailed, conversational answer here]

    Make sure:
    1. Each question addresses a different key aspect or detail from the text.
    2. The answers are well-explained, providing context or additional information when necessary.
    3. Both questions and answers should be clear and specific without direct references to phrases from the text.
    4. The questions should be open-ended (who, what, when, where, why, how) and encourage detailed responses.

    Start generating question-answer pairs from the context provided.
    """

def main():
    data_ingestion(query)
        
if __name__ == "__main__":
    main()
