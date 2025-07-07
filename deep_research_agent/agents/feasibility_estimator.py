from utils.llm import generate_idea

class FeasibilityEstimatorAgent:
    def __init__(self):
        pass

    def estimate_feasibility(self, idea):
        prompt = f"Estimate the feasibility of this research idea on a scale of 0 to 1, considering current technology and resources. Just return a float.\nIdea: {idea}"
        score = generate_idea(prompt)
        try:
            return float(score.strip())
        except:
            return 0.5
