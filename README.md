# PokeQuant

A Python application for accessing Pokémon TCG card data and pricing information.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux)
4. Install dependencies: `pip install pokemontcgsdk python-dotenv`
5. Copy `.env.example` to `.env` and add your Pokémon TCG API key:
   ```
   POKEMON_TCG_API_KEY=your_api_key_here
   ```

## Getting an API Key

1. Sign up for an account at the [Pokémon TCG Developer Portal](https://dev.pokemontcg.io/)
2. Generate your free API key
3. Add it to your `.env` file

## Usage

Run the API script:
```bash
python pokequant/api.py
```

## Security

- Never commit your `.env` file to version control
- Keep your API key secure and don't share it publicly
- If you think your API key has been compromised, generate a new one immediately