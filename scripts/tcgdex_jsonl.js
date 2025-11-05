import TCGdex from '@tcgdex/sdk'
import fs from 'fs'
const sdk = new TCGdex('en')

const stream = fs.createWriteStream('data.jsonl', { flags: 'w', encoding: 'utf8' })

const metadata = {
  metadata: {
    source: "TCGDex API",
    language: "en",
    exportedAt: new Date().toISOString()
  }
}
stream.write(JSON.stringify(metadata) + '\n')

const allCards = await sdk.card.list()
console.log(`Found ${allCards.length} cards total.`)

let processed = 0

for (const cardRef of allCards) {
  processed++
  console.log(`Processing card ${processed}/${allCards.length}: ${cardRef.id}`)

  try {
    const fullCard = await cardRef.getCard()
    if (!fullCard) continue

    const cardData = {
      name: fullCard.name,
      id: fullCard.id,
      rarity: fullCard.rarity,
      illustrator: fullCard.illustrator || 'Unknown',
      variant: fullCard.variants || 'Unknown',
      set: fullCard.set?.name || 'Unknown',
      setId: fullCard.set?.id || 'Unknown',
      regulationMark: fullCard.regulationMark || 'Unknown',
      legal: fullCard.legal || 'Unknown',
      pricing: {
        cardmarket: null,
        tcgplayer: null
      }
    }

    // Cardmarket pricing
    if (fullCard.pricing?.cardmarket) {
      const cm = fullCard.pricing.cardmarket
      cardData.pricing.cardmarket = {
        updated: cm.updated || null,
        unit: cm.unit || 'EUR',
        avg: cm.avg || null,
        low: cm.low || null,
        trend: cm.trend || null,
        avg1: cm.avg1 || null,
        avg7: cm.avg7 || null,
        avg30: cm.avg30 || null,
        'avg-holo': cm['avg-holo'] || null,
        'low-holo': cm['low-holo'] || null,
        'trend-holo': cm['trend-holo'] || null,
        'avg1-holo': cm['avg1-holo'] || null,
        'avg7-holo': cm['avg7-holo'] || null,
        'avg30-holo': cm['avg30-holo'] || null
      }
    }
    if (fullCard.pricing?.tcgplayer) {
      const tcp = fullCard.pricing.tcgplayer
      cardData.pricing.tcgplayer = {
        updated: tcp.updated || null,
        unit: tcp.unit || 'USD',
        normal: tcp.normal ? {
          lowPrice: tcp.normal.lowPrice || null,
          midPrice: tcp.normal.midPrice || null,
          highPrice: tcp.normal.highPrice || null,
          marketPrice: tcp.normal.marketPrice || null,
          directLowPrice: tcp.normal.directLowPrice || null
        } : null,
        'reverse-holofoil': tcp['reverse-holofoil'] ? {
          lowPrice: tcp['reverse-holofoil'].lowPrice || null,
          midPrice: tcp['reverse-holofoil'].midPrice || null,
          highPrice: tcp['reverse-holofoil'].highPrice || null,
          marketPrice: tcp['reverse-holofoil'].marketPrice || null,
          directLowPrice: tcp['reverse-holofoil'].directLowPrice || null
        } : null,
        holofoil: tcp.holofoil ? {
          lowPrice: tcp.holofoil.lowPrice || null,
          midPrice: tcp.holofoil.midPrice || null,
          highPrice: tcp.holofoil.highPrice || null,
          marketPrice: tcp.holofoil.marketPrice || null,
          directLowPrice: tcp.holofoil.directLowPrice || null
        } : null
      }
    }
    stream.write(JSON.stringify(cardData) + '\n')
  } catch (err) {
    console.error(`Error processing card ${cardRef.id}:`, err.message)
  }
}

stream.end()
console.log('Export completed: data.jsonl')
