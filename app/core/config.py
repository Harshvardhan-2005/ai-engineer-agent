from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Optional: debug check
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")