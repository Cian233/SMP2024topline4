from llama_index.core.tools import QueryEngineTool
import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from prompts import *

def create_query_engine():
    # 初始化客户端
    db = chromadb.PersistentClient(path="./knowledge_base/vector_base")

    # 获取 collection
    chroma_collection = db.get_or_create_collection("graph_func_doc")

    # 将 chroma 分配为上下文中的 vector_store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 从存储的向量加载你的索引
    index = VectorStoreIndex.from_vector_store(
        vector_store, storage_context=storage_context
    )
    
    # 配置检索器
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=15,
    )

    # 配置响应合成器
    response_synthesizer = get_response_synthesizer(
        text_qa_template=DUNC_DOC_QA_PROMPT
    )

    # 组装查询引擎
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.2)],
    )

    return query_engine
