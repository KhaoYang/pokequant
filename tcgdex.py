from tcgdexsdk import TCGdex, Language
import asyncio
tcgdex = TCGdex() # Initialize with default language (English)
async def main():
    tcgdex = TCGdex("en")

# Or using the Language enum
    tcgdex = TCGdex(Language.EN)
    for i in range (1, 10):
        card =  await tcgdex.card.get(f"base1-{i}")
        print(card.pricing.cardmarket.trend)
        print(card.name)

    
# Initialize with language as string
asyncio.run(main())