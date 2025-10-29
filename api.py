from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Configure API key from environment variable
api_key = os.getenv('POKEMON_TCG_API_KEY')
if not api_key:
    raise ValueError("POKEMON_TCG_API_KEY environment variable is not set. Please set it with your API key.")

RestClient.configure(api_key)
print(f"API Key configured: {RestClient.api_key is not None}")

print("Fetching card...")
cards = Card.where(page=1, pageSize=250)

print(cards)


