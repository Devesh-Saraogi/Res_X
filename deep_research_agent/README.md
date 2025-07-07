# Deep Research Agent

A Dynamic Multi-Agent Workflow for Generating High-Quality Research Ideas (High Novelty & Feasibility)

## Features
- Multi-agent orchestration using LangGraph
- Google Flash 2.5 API for LLM-based idea generation and analysis
- Free APIs for web and research paper search (arXiv, SerpAPI/Bing)
- Evolutionary algorithm for iterative idea refinement

## Setup

1. **Python Environment**
   - Python 3.9+
   - Recommended: Use a virtual environment

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **API Keys**
   - Set your Google Flash 2.5 API key in `.env`
   - (Optional) Set SerpAPI or Bing Web Search API key in `.env`

4. **Run the Agent**
   ```bash
   python main.py
   ```

## Project Structure
- `main.py` — Entry point, runs the agent loop
- `agents/` — Contains agent implementations
- `utils/` — Helper functions (API calls, evolutionary ops)
- `config.py` — Configuration and constants
- `.env` — API keys (not committed)

## Notes
- All APIs/tools used are free tier or open access
- Designed for extensibility and research prototyping
