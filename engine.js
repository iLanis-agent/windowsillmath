(function (root) {
  "use strict";
  function r0(x) { return Math.round(x); }
  function r1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word) { return n + " " + word + (n === 1 ? "" : "s"); }

  function potPlan(sillLCm, sillDCm, potDCm) {
    if (!(sillLCm > 0) || !(sillDCm > 0) || !(potDCm > 0)) return { error: "sill and pot must be positive" };
    var across = Math.floor(sillLCm / potDCm);
    var rows = Math.floor(sillDCm / potDCm);
    var pots = across * rows;
    return { across: across, rows: rows, pots: pots };
  }

  function weightPlan(pots, litersEach, kgPerL) {
    if (!(pots > 0) || !(litersEach > 0) || !(kgPerL > 0)) return { error: "pots, soil and density must be positive" };
    var soilL = r1(pots * litersEach);
    var kg = r1(pots * litersEach * kgPerL);
    return { soilL: soilL, kg: kg };
  }

  function waterPlan(pots, mlEach, daysBetween) {
    if (!(pots > 0) || !(mlEach > 0) || !(daysBetween > 0)) return { error: "pots, water and interval must be positive" };
    var mlWeek = r0(pots * mlEach * 7 / daysBetween);
    var litersWeek = r1(pots * mlEach * 7 / daysBetween / 1000);
    return { mlWeek: mlWeek, litersWeek: litersWeek };
  }

  function renderPot(r, sillL, sillD, potD) {
    if (r.pots === 0) return "No " + potD + " cm pot fits a " + sillL + " x " + sillD + " cm sill - try a smaller pot.";
    return "A " + sillL + " x " + sillD + " cm sill takes " + plural(r.across, "pot") + " of " + potD + " cm across " + plural(r.rows, "row") + " - " + plural(r.pots, "pot") + " of room.";
  }

  function renderWeight(r, pots, litersEach, kgPerL) {
    return plural(pots, "pot") + " of " + litersEach + " L is " + r.soilL + " L of soil - about " + r.kg + " kg on the sill at a labeled " + kgPerL + " kg a liter.";
  }

  function renderWater(r, pots, mlEach, daysBetween) {
    return plural(pots, "pot") + " at " + mlEach + " ml every " + plural(daysBetween, "day") + " is about " + r.mlWeek + " ml a week - " + r.litersWeek + " L to carry.";
  }

  var api = { potPlan: potPlan, weightPlan: weightPlan, waterPlan: waterPlan, renderPot: renderPot, renderWeight: renderWeight, renderWater: renderWater };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.WindowsillMath = api;
})(this);
