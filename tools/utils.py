from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from langchain_openai import ChatOpenAI
import pandas as pd

from config import *

embeddings=OpenAIEmbedding(
    model=EMBEDDING_MODEL_NAME,
    embed_batch_size=100,
    api_base=OPENAI_BASE_URL_EMB,
    api_key=OPENAI_API_KEY_EMB
)

question_path = r'answer\Final_Example.json'

def get_llm(model=None,**kwargs):
    if model==None:
        model_name=LLM_MODEL_NAME
    elif model=='gpt-4o':
        model_name='gpt-4o-2024-08-06'
    else:
        model_name=model
    llm = OpenAI(
    temperature=1,
    model=model_name,
    api_base=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
    **kwargs 
    )
    return llm

def get_langchain_llm():
    llm=ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    #model='gpt-4o-2024-08-06'
    model='gpt-4o-mini'
    )
    return llm


def get_embed():
    return embeddings

def get_question():
    try:
        df = pd.read_json(question_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file {question_path} was not found.")
        return pd.DataFrame()  # 返回空 DataFrame
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()