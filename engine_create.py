from llama_index.core.memory import ChatMemoryBuffer
from index_creater import new_index
from setup_chromadb import create_or_get_vectordb
from setup_embedding_model import embed_model


def create_query_engine():
        """
        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        index = new_index(create_or_get_vectordb(), embed_model())
        query_engine = index.as_chat_engine(
            chat_mode="context",
            memory=memory,
            system_prompt= 
            You are a professional AI Assistant receptionist working in Aditya's one of the best restaurant called Adii's Khana Khazana,
            Ask questions mentioned inside square brackets which you have to ask from customer, DON'T ASK THESE QUESTIONS 
            IN ONE go and keep the conversation engaging! Always ask questions one by one only!
            
            [Ask Name and contact number, what they want to order, and end the conversation with greetings!]

            If you don't know the answer, just say that you don't know, don't try to make up an answer.
            Provide concise and short answers not more than 10 words, and don't chat with yourself!
        ,
        )
        """
        

        index = new_index(create_or_get_vectordb(), embed_model())
        query_engine = index.as_query_engine()
        return query_engine

def interact_with_llm(customer_query):
        #print("Command: ", customer_query)
        query_engine = create_query_engine()
        response = query_engine.query(customer_query)
        #AgentChatResponse = query_engine.chat(customer_query)
        #answer = AgentChatResponse.response
        return response