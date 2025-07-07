import random
from utils.llm import mutate_idea

def evolve_population(population):
    # Simple mutation for each idea
    return [mutate_idea(idea) for idea in population]

def select_top(population, scores, k=3):
    # Select top-k ideas based on scores
    scored = list(zip(population, scores))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in scored[:k]]
