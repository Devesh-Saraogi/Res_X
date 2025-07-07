from agents.idea_generator import IdeaGeneratorAgent
from agents.novelty_verifier import NoveltyVerifierAgent
from agents.feasibility_estimator import FeasibilityEstimatorAgent
from utils.evolution import evolve_population, select_top
from config import MAX_ITER, NOVELTY_THRESHOLD, FEASIBILITY_THRESHOLD


def main():
    topic = input("Enter research field/topic: ")
    idea_agent = IdeaGeneratorAgent()
    novelty_agent = NoveltyVerifierAgent()
    feasibility_agent = FeasibilityEstimatorAgent()

    population = idea_agent.generate_population(topic)
    for iteration in range(MAX_ITER):
        print(f"\nIteration {iteration+1}")
        novelty_scores = [novelty_agent.verify_novelty(idea) for idea in population]
        feasibility_scores = [feasibility_agent.estimate_feasibility(idea) for idea in population]
        for i, idea in enumerate(population):
            print(f"Idea: {idea}\n  Novelty: {novelty_scores[i]:.2f}, Feasibility: {feasibility_scores[i]:.2f}")
        # Select ideas that pass thresholds
        selected = [idea for i, idea in enumerate(population)
                    if novelty_scores[i] >= NOVELTY_THRESHOLD and feasibility_scores[i] >= FEASIBILITY_THRESHOLD]
        if selected:
            print("\nHigh-quality research ideas found:")
            for idea in selected:
                print(f"- {idea}")
            break
        # Evolve population
        population = evolve_population(select_top(population, novelty_scores))
    else:
        print("\nNo idea met the thresholds. Best candidates:")
        for idea in select_top(population, [n+f for n, f in zip(novelty_scores, feasibility_scores)]):
            print(f"- {idea}")

if __name__ == "__main__":
    main()
