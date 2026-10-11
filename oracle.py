import json, math

def r0(x): return math.floor(x + 0.5)
def r1(x): return math.floor(x * 10 + 0.5) / 10
def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word): return str(n) + " " + word + ("" if n == 1 else "s")
def fmt(x): return str(jsnum(x))

def pot_plan(sillL, sillD, potD):
    if not (sillL > 0) or not (sillD > 0) or not (potD > 0):
        return {"error": "sill and pot must be positive"}
    across = math.floor(sillL / potD)
    rows = math.floor(sillD / potD)
    return {"across": across, "rows": rows, "pots": across * rows}

def weight_plan(pots, litersEach, kgPerL):
    if not (pots > 0) or not (litersEach > 0) or not (kgPerL > 0):
        return {"error": "pots, soil and density must be positive"}
    soilL = r1(pots * litersEach)
    kg = r1(pots * litersEach * kgPerL)
    return {"soilL": jsnum(soilL), "kg": jsnum(kg)}

def water_plan(pots, mlEach, daysBetween):
    if not (pots > 0) or not (mlEach > 0) or not (daysBetween > 0):
        return {"error": "pots, water and interval must be positive"}
    mlWeek = r0(pots * mlEach * 7 / daysBetween)
    litersWeek = r1(pots * mlEach * 7 / daysBetween / 1000)
    return {"mlWeek": mlWeek, "litersWeek": jsnum(litersWeek)}

def render_pot(r, sillL, sillD, potD):
    if r["pots"] == 0:
        return ("No " + fmt(potD) + " cm pot fits a " + fmt(sillL) + " x " + fmt(sillD)
                + " cm sill - try a smaller pot.")
    return ("A " + fmt(sillL) + " x " + fmt(sillD) + " cm sill takes " + plural(r["across"], "pot")
            + " of " + fmt(potD) + " cm across " + plural(r["rows"], "row") + " - "
            + plural(r["pots"], "pot") + " of room.")

def render_weight(r, pots, litersEach, kgPerL):
    return (plural(pots, "pot") + " of " + fmt(litersEach) + " L is " + fmt(r["soilL"])
            + " L of soil - about " + fmt(r["kg"]) + " kg on the sill at a labeled "
            + fmt(kgPerL) + " kg a liter.")

def render_water(r, pots, mlEach, daysBetween):
    return (plural(pots, "pot") + " at " + fmt(mlEach) + " ml every " + plural(daysBetween, "day")
            + " is about " + fmt(r["mlWeek"]) + " ml a week - " + fmt(r["litersWeek"]) + " L to carry.")

cases = []
for sillL, sillD, potD in [(120, 20, 14), (90, 15, 12), (30, 12, 14), (100, 30, 10),
                            (0, 20, 14), (120, 0, 14), (120, 20, 0)]:
    r = pot_plan(sillL, sillD, potD)
    cases.append({"fn": "potPlan", "args": [sillL, sillD, potD], "result": r,
                  "render": None if "error" in r else render_pot(r, sillL, sillD, potD)})
for pots, litersEach, kgPerL in [(8, 3, 1.3), (7, 2, 1.2), (30, 1, 1.3), (5, 0.5, 1.1), (0, 3, 1.3)]:
    r = weight_plan(pots, litersEach, kgPerL)
    cases.append({"fn": "weightPlan", "args": [pots, litersEach, kgPerL], "result": r,
                  "render": None if "error" in r else render_weight(r, pots, litersEach, kgPerL)})
for pots, mlEach, daysBetween in [(8, 250, 3), (7, 200, 2), (30, 100, 7), (5, 150, 5), (0, 250, 3)]:
    r = water_plan(pots, mlEach, daysBetween)
    cases.append({"fn": "waterPlan", "args": [pots, mlEach, daysBetween], "result": r,
                  "render": None if "error" in r else render_water(r, pots, mlEach, daysBetween)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
