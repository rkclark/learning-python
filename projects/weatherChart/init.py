from os import path, getenv
from dotenv import load_dotenv
from get_postcode import get_postcode

current_dir = path.dirname(path.abspath(__file__))
dotenv_path = path.join(current_dir, ".env")

load_dotenv(dotenv_path, verbose=True)

OPEN_WEATHER_API_KEY = getenv("OPEN_WEATHER_API_KEY")

postcode = get_postcode()
print("Got postcode:\n" + postcode)
