from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import langchain
langchain.debug = True

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-4-0613")


search = SerpAPIWrapper()

# Define a list of tools offered by the agent
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful when you need to answer questions about current events. You should ask targeted questions.",
    ),

]

agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
)

prompt ="""Imagine you are Indian UPSC evaluator. 
You are evaluating an answer for the question:
{question}. 
The answer wrriten by an anspirant is:
{answer}.
You have to provide a detailed feedback.
You should also provide a score between 0 and 100.
The feedback should be at least 200 words long and you should provide examples and references to support your feedback and score.
Give instances where there is scope for improvement and also mention the positives.
Explain how the aspirant can improve his/her answer.
address the aspirant directly.
"""

def evaluate_answer(question, answer):
    input_text = prompt.format(question=question, answer=answer)
    output_text = agent.run(input_text)
    return output_text