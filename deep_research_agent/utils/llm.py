from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_FLASH_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_FLASH_API_KEY)

def generate_idea(prompt):
    response = llm.invoke(prompt)
    return response.content if hasattr(response, 'content') else str(response)

def mutate_idea(idea):
    mutation_prompt = f"Mutate or evolve this research idea to increase novelty: {idea}"
    return generate_idea(mutation_prompt)
