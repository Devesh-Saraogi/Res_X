from utils.llm import generate_idea
from config import POPULATION_SIZE

class IdeaGeneratorAgent:
    def __init__(self):
        pass

    def generate_population(self, topic):
        prompt = f"Propose a highly novel and feasible research idea in the field of {topic}."
        return [generate_idea(prompt) for _ in range(POPULATION_SIZE)]
