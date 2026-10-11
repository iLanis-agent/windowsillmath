# Windowsill math

How many pots actually fit the sill, how many kilograms of wet soil they add up to, and how many liters of water they drink a week. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/windowsillmath/

## The three tools

- **Pot plan** - `potPlan(sillLCm, sillDCm, potDCm)`: pots across, rows and total on the sill.
- **Weight plan** - `weightPlan(pots, litersEach, kgPerL)`: soil liters and kilograms on the sill.
- **Water plan** - `waterPlan(pots, mlEach, daysBetween)`: milliliters and liters to carry each week.

## Labeled norms (illustrative estimates, not structural advice)

- Pot: 14 cm across. Wet soil: 1.3 kg a liter. Drink: 250 ml per pot every 3 days. Your sill, pots and plants decide the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (17 cases, 74 checks)

Regenerate the oracle expectations: `python3 oracle.py`
