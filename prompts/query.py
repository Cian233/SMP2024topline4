from llama_index.core.prompts.base import PromptTemplate
from llama_index.core.prompts.prompt_type import PromptType
DUNC_DOC_QA_PROMPT_TMPL = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "你只能从上述信息中寻找答案，不能无中生有"
    "答案必须包含函数名，参数，返回，示例，描述"
    """
    示例：
         - **函数名**: 
        - average_internal_degree
        - **参数**: 
        - `summary`: （可选，默认值为True）如果为True，则返回分区的整体汇总（最小值、最大值、平均值、标准差）；如果为False，则返回基于社区的分数列表。

        - **返回**: 
        - `a FitnessResult object/a list of community-wise score`。

        - **示例**:
        ```python
        from cdlib.algorithms import louvain
        g = nx.karate_club_graph()
        communities = louvain(g)
        mod = communities.average_internal_degree()
        ```

        - **描述**: 
        - 计算具有较高内部度（degree）的算法节点的比例，具体而言，返回在分区中，内部度高于中位数度值的算法节点的比例。
        \[
        f(S) = \frac{{| \{{u: u \in S,| \{{(u,v): v \in S\}}| > d_m \}}| }}{{n_S}}
        \]
        其中 \(d_m\) 是内部度的中位数值。
    """
    "Query: {query_str}\n"
    "Answer: "
)

DUNC_DOC_QA_PROMPT = PromptTemplate(
    DUNC_DOC_QA_PROMPT_TMPL, prompt_type=PromptType.QUESTION_ANSWER
)