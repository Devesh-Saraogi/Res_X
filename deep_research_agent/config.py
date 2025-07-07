import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GOOGLE_FLASH_API_KEY = os.getenv("GOOGLE_FLASH_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
BING_API_KEY = os.getenv("BING_API_KEY")

# Evolutionary algorithm parameters
POPULATION_SIZE = 5
MAX_ITER = 10
NOVELTY_THRESHOLD = 0.8
FEASIBILITY_THRESHOLD = 0.7

# Other config
ARXIV_API_URL = "http://export.arxiv.org/api/query"
