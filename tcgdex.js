import TCGdex from '@tcgdex/sdk'

const sdk = new TCGdex('en')
const card = await sdk.card.get('base1-4')

// Access Cardmarket pricing (EUR)
console.log(card.pricing.cardmarket.trend)
console.log(card.pricing.cardmarket.avg30)

// Access TCGplayer pricing (USD)
console.log(card.pricing.tcgplayer.holofoil.marketPrice)
//console.log(card.pricing.tcgplayer.normal.lowPrice)