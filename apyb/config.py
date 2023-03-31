from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).parent
APYB_GITHUB_ORG = config("APYB_GITHUB_ORG", default="apyb")
APYB_GITHUB_COMMUNITY_REPO = config("APYB_GITHUB_COMMUNITY_REPO", default="comunidade")
