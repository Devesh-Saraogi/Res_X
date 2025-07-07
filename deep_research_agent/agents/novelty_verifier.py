from utils.search import search_arxiv, search_duckduckgo
from utils.llm import generate_idea

class NoveltyVerifierAgent:
    def __init__(self):
        pass

    def verify_novelty(self, idea):
        # Search arXiv and web for similar ideas
        arxiv_results = search_arxiv(idea)
        web_results = search_duckduckgo(idea)
        # Summarize similarity using LLM
        prompt = f"Given the following research idea: {idea}\nAnd these related works: {arxiv_results}\n{web_results}\nHow novel is the idea on a scale of 0 to 1? Just return a float."
        score = generate_idea(prompt)
        try:
            return float(score.strip())
        except:
            return 0.5
