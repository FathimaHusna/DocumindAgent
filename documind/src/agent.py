from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.rag import get_retriever, get_llm
import numexpr

def calculator(expression):
    try:
        return str(numexpr.evaluate(expression))
    except Exception as e:
        return str(e)

def search_documind(query):
    retriever = get_retriever()
    docs = retriever.invoke(query)
    return "\n\n".join(doc.page_content for doc in docs)

class DocuMindAgent:
    def __init__(self):
        self.llm = get_llm()
    
    def decide_tool(self, query):
        template = """Question: {question}
        Options:
        A) Math calculation
        B) Information about DocuMind
        C) General chat
        
        Answer (A, B, or C):"""
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.llm | StrOutputParser()
        response = chain.invoke({"question": query})
        
        if "A" in response or "Math" in response:
            return "Calculator"
        elif "B" in response or "DocuMind" in response:
            return "Search"
        else:
            return "None"

    def run_tool(self, tool_name, query):
        if "Calculator" in tool_name:
            import re
            # Simple regex to extract math expression (numbers and operators)
            expression = "".join(re.findall(r"[\d\+\-\*\/\.\(\)\s]", query)).strip()
            print(f"Extracted Expression: {expression}")
            return calculator(expression)
            
        elif "Search" in tool_name:
            return search_documind(query)
            
        return None

    def final_answer(self, query, tool_output):
        template = """Answer the question based on the context.
        
        Question: {question}
        Context: {context}
        
        Answer:"""
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"question": query, "context": tool_output})

    def invoke(self, inputs):
        query = inputs["input"]
        print(f"Thinking about: {query}")
        
        tool = self.decide_tool(query)
        print(f"Decided to use: {tool}")
        
        if "None" in tool:
            # Direct answer
            return {"output": self.final_answer(query, "No context needed.")}
            
        tool_output = self.run_tool(tool, query)
        print(f"Tool Output: {tool_output}")
        
        if "Calculator" in tool:
            return {"output": tool_output}
            
        response = self.final_answer(query, tool_output)
        return {"output": response}

def get_agent():
    return DocuMindAgent()
