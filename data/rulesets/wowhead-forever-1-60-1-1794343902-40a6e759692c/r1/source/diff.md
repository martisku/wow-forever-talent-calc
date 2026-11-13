# Wowhead vs. current canonical data

Wowhead version 1.60.1, data revision 1794343902, matched by talent name (normalised).

| class | talents (Wowhead / current) | new | gone | position | maxRank | ranks | requires | icons |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| druid | 52 / 52 | 7 | 7 | 6 | 0 | 66 | 0 | 5 |
| hunter | 50 / 50 | 0 | 0 | 2 | 0 | 51 | 0 | 14 |
| mage | 53 / 53 | 5 | 5 | 7 | 4 | 46 | 0 | 9 |
| paladin | 51 / 52 | 6 | 7 | 26 | 8 | 65 | 5 | 12 |
| priest | 52 / 53 | 2 | 3 | 4 | 0 | 69 | 0 | 5 |
| rogue | 54 / 53 | 9 | 8 | 19 | 6 | 41 | 5 | 1 |
| shaman | 50 / 50 | 2 | 2 | 14 | 0 | 60 | 4 | 10 |
| warlock | 52 / 52 | 3 | 3 | 0 | 0 | 68 | 0 | 8 |
| warrior | 53 / 54 | 6 | 7 | 10 | 3 | 54 | 4 | 5 |

## druid

**New (Wowhead only)**

- `wh-104947` Blood Frenzy - feral-combat r3c3
- `wh-104918` Bloom - restoration r2c3
- `wh-104949` Lacerate - feral-combat r3c1
- `wh-104950` Natural Instinct - feral-combat r4c3
- `wh-104951` Predatory Discipline - feral-combat r3c2
- `wh-104956` Primal Bite - feral-combat r6c1
- `wh-113563` Shifting Power - feral-combat r6c2

**Gone (current only)**

- `balance-of-nature` Balance of Nature - balance r2c3
- `berserk` Berserk - feral-combat r6c1
- `gift-of-the-earthmother` Gift of the Earthmother - restoration r2c3
- `king-of-the-jungle` King of the Jungle - feral-combat r4c3
- `mangle` Mangle - feral-combat r3c1
- `predatory-instincts` Predatory Instincts - feral-combat r4c0
- `primal-fury` Primal Fury - feral-combat r3c3

**Tree moved**

| talent | Wowhead | current |
|---|---|---|
| Furor | `feral-combat` | `restoration` |
| Heart of the Wild | `restoration` | `feral-combat` |

**Position**

| talent | Wowhead | current |
|---|---|---|
| Natural Reaction | `[5, 3]` | `[5, 0]` |
| Predatory Strikes | `[3, 0]` | `[3, 2]` |
| Reflection | `[1, 1]` | `[2, 1]` |
| Rend and Tear | `[5, 0]` | `[5, 2]` |
| Shredding Attacks | `[2, 0]` | `[3, 0]` |
| Subtlety | `[2, 1]` | `[1, 1]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Feral Charge | `ability_hunter_pet_bear` | `crop-feral-charge` |
| Genesis | `spell_arcane_arcane03` | `crop-genesis` |
| Improved Wrath | `spell_nature_abolishmagic` | `crop-improved-wrath` |
| Nature's Splendor | `spell_nature_natureresistancetotem` | `crop-natures-splendor` |
| Nature's Swiftness | `spell_nature_ravenform` | `crop-natures-swiftness` |

**Rank text (66 differing rank(s))**

- **Brutal Impact** rank 2
  - Wowhead: Increases the stun duration of your Bash and Pounce abilities by 1 sec and reduces the cooldown of Bash by 30 sec.
  - current:   Increases the stun duration of your Bash and Pounce abilities by 0.5 sec and reduces the cooldown of Bash by 15 sec.
- **Eclipse** rank 2
  - Wowhead: Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.33 sec. Stores up to 4 charges. Lasts 15 sec.
  - current:   Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.17 sec. Stores up to 4 charges. Lasts 15 sec.
- **Eclipse** rank 3
  - Wowhead: Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.50 sec. Stores up to 4 charges. Lasts 15 sec.
  - current:   Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.17 sec. Stores up to 4 charges. Lasts 15 sec.
- **Feral Charge** rank 1
  - Wowhead: Requires Bear Form, Dire Bear Form Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec. Feral Charge (Cat) 8 - 25 yd range Instant 30 sec cooldownRequires Druid Requires level 1 Requires Cat Form Leap behind an enemy.
  - current:   Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec. Feral Charge (Cat): Leap behind an enemy, Dazing them for 3 sec.
- **Feral Instinct** rank 1
  - Wowhead: Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 levels higher.
  - current:   Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 level higher.
- **Ferocity** rank 1
  - Wowhead: Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 1 Rage or Energy.
  - current:   Reduces the cost of your Maul, Mangle, Swipe, Claw, and Rake abilities by 1 Rage or Energy.
- **Ferocity** rank 2
  - Wowhead: Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 2 Rage or Energy.
  - current:   Reduces the cost of your Maul, Mangle, Swipe, Claw, and Rake abilities by 2 Rage or Energy.
- **Ferocity** rank 3
  - Wowhead: Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 3 Rage or Energy.
  - current:   Reduces the cost of your Maul, Mangle, Swipe, Claw, and Rake abilities by 3 Rage or Energy.
- **Ferocity** rank 4
  - Wowhead: Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 4 Rage or Energy.
  - current:   Reduces the cost of your Maul, Mangle, Swipe, Claw, and Rake abilities by 4 Rage or Energy.
- **Ferocity** rank 5
  - Wowhead: Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy.
  - current:   Reduces the cost of your Maul, Mangle, Swipe, Claw, and Rake abilities by 5 Rage or Energy.
- **Furor** rank 1
  - Wowhead: Gives you a 20% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20% of the Energy you had when last in Cat Form, plus 2 Energy per second spent outside Bear Form or Dire Bear Form, up to 20 Energy.
  - current:   Gives you a 20% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 20% of the Energy you had when you were last in Cat Form, plus 2 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 20 Energy.
- **Furor** rank 2
  - Wowhead: Gives you a 40% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 40% of the Energy you had when last in Cat Form, plus 4 Energy per second spent outside Bear Form or Dire Bear Form, up to 40 Energy.
  - current:   Gives you a 20% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 20% of the Energy you had when you were last in Cat Form, plus 2 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 20 Energy.
- **Furor** rank 3
  - Wowhead: Gives you a 60% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 60% of the Energy you had when last in Cat Form, plus 6 Energy per second spent outside Bear Form or Dire Bear Form, up to 60 Energy.
  - current:   Gives you a 20% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 20% of the Energy you had when you were last in Cat Form, plus 2 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 20 Energy.
- **Furor** rank 4
  - Wowhead: Gives you a 80% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 80% of the Energy you had when last in Cat Form, plus 8 Energy per second spent outside Bear Form or Dire Bear Form, up to 80 Energy.
  - current:   Gives you a 20% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 20% of the Energy you had when you were last in Cat Form, plus 2 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 20 Energy.
- **Furor** rank 5
  - Wowhead: Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy.
  - current:   Gives you a 20% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 20% of the Energy you had when you were last in Cat Form, plus 2 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 20 Energy.
- **Genesis** rank 1
  - Wowhead: Increases the periodic damage and healing done by your spells and abilities by 2%.
  - current:   Increases the periodic damage and healing done by your spells and abilities by 1%.
- **Genesis** rank 2
  - Wowhead: Increases the periodic damage and healing done by your spells and abilities by 4%.
  - current:   Increases the periodic damage and healing done by your spells and abilities by 2%.
- **Genesis** rank 3
  - Wowhead: Increases the periodic damage and healing done by your spells and abilities by 6%.
  - current:   Increases the periodic damage and healing done by your spells and abilities by 3%.
- **Genesis** rank 4
  - Wowhead: Increases the periodic damage and healing done by your spells and abilities by 8%.
  - current:   Increases the periodic damage and healing done by your spells and abilities by 4%.
- **Genesis** rank 5
  - Wowhead: Increases the periodic damage and healing done by your spells and abilities by 10%.
  - current:   Increases the periodic damage and healing done by your spells and abilities by 5%.
- **Improved Wrath** rank 2
  - Wowhead: Reduces the cast time of your Wrath spell by 0.2 sec and its Mana cost by 20%.
  - current:   Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%.
- **Improved Wrath** rank 3
  - Wowhead: Reduces the cast time of your Wrath spell by 0.3 sec and its Mana cost by 30%.
  - current:   Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%.
- **Improved Wrath** rank 4
  - Wowhead: Reduces the cast time of your Wrath spell by 0.4 sec and its Mana cost by 40%.
  - current:   Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%.
- **Improved Wrath** rank 5
  - Wowhead: Reduces the cast time of your Wrath spell by 0.5 sec and its Mana cost by 50%.
  - current:   Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%.
- **Insect Swarm** rank 1
  - Wowhead: The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec.
  - current:   The enemy target is swarmed by insects, decreasing their chance to hit by 2% and causing 55 Nature damage over 12 sec.
- **Leader of the Pack** rank 1
  - Wowhead: While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%.
  - current:   While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura.
- **Moonfury** rank 1
  - Wowhead: Increases the damage done by your Arcane and Nature spells by 2%.
  - current:   Increases the damage done by your Arcane and Nature spells by 1%.
- **Moonfury** rank 2
  - Wowhead: Increases the damage done by your Arcane and Nature spells by 4%.
  - current:   Increases the damage done by your Arcane and Nature spells by 2%.
- **Moonfury** rank 3
  - Wowhead: Increases the damage done by your Arcane and Nature spells by 6%.
  - current:   Increases the damage done by your Arcane and Nature spells by 3%.
- **Moonfury** rank 4
  - Wowhead: Increases the damage done by your Arcane and Nature spells by 8%.
  - current:   Increases the damage done by your Arcane and Nature spells by 4%.
- **Moonfury** rank 5
  - Wowhead: Increases the damage done by your Arcane and Nature spells by 10%.
  - current:   Increases the damage done by your Arcane and Nature spells by 5%.
- **Moonglow** rank 1
  - Wowhead: Reduces the Mana cost of your damaging spells by 8%.
  - current:   Reduces the Mana cost of your spells by 3%.
- **Moonglow** rank 2
  - Wowhead: Reduces the Mana cost of your damaging spells by 17%.
  - current:   Reduces the Mana cost of your spells by 6%.
- **Moonglow** rank 3
  - Wowhead: Reduces the Mana cost of your damaging spells by 25%.
  - current:   Reduces the Mana cost of your spells by 9%.
- **Moonkin Form** rank 1
  - Wowhead: Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells. The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects.
  - current:   Transforms the Druid into Moonkin Form. While in this form, the armor contribution from items is increased by 360% and all party members within 45 yards have their critical chance increased by 3%, exclusive with Leader of the Pack. The Moonkin cannot cast healing spells while shapeshifted. The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects.
- **Natural Reaction** rank 2
  - Wowhead: Increases your dodge chance by 2%, and gives you a 40% chance to gain 5 Rage each time you dodge.
  - current:   Increases your dodge chance by 1%, and gives you a 20% chance to gain 5 Rage each time you dodge.
- **Natural Reaction** rank 3
  - Wowhead: Increases your dodge chance by 3%, and gives you a 60% chance to gain 5 Rage each time you dodge.
  - current:   Increases your dodge chance by 1%, and gives you a 20% chance to gain 5 Rage each time you dodge.
- **Natural Reaction** rank 4
  - Wowhead: Increases your dodge chance by 4%, and gives you a 80% chance to gain 5 Rage each time you dodge.
  - current:   Increases your dodge chance by 1%, and gives you a 20% chance to gain 5 Rage each time you dodge.
- **Natural Reaction** rank 5
  - Wowhead: Increases your dodge chance by 5%, and gives you a 100% chance to gain 5 Rage each time you dodge.
  - current:   Increases your dodge chance by 1%, and gives you a 20% chance to gain 5 Rage each time you dodge.
- **Naturalist** rank 1
  - Wowhead: Reduces the cast time of your Healing Touch and Wild Growth spells by 0.1 sec and increases all damage you deal by 2%.
  - current:   Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%.
- **Naturalist** rank 2
  - Wowhead: Reduces the cast time of your Healing Touch and Wild Growth spells by 0.2 sec and increases all damage you deal by 4%.
  - current:   Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%.
- **Naturalist** rank 3
  - Wowhead: Reduces the cast time of your Healing Touch and Wild Growth spells by 0.3 sec and increases all damage you deal by 6%.
  - current:   Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%.
- **Naturalist** rank 4
  - Wowhead: Reduces the cast time of your Healing Touch and Wild Growth spells by 0.4 sec and increases all damage you deal by 8%.
  - current:   Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%.
- **Naturalist** rank 5
  - Wowhead: Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%.
  - current:   Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%.
- **Nature's Focus** rank 1
  - Wowhead: Gives your Arcane and Nature spells a 14% chance to not lose casting time when you take damage.
  - current:   Gives you a 14% chance to avoid interruption caused by damage while casting Arcane and Nature spells.
- **Nature's Focus** rank 2
  - Wowhead: Gives your Arcane and Nature spells a 28% chance to not lose casting time when you take damage.
  - current:   Gives you a 28% chance to avoid interruption caused by damage while casting Arcane and Nature spells.
- **Nature's Focus** rank 3
  - Wowhead: Gives your Arcane and Nature spells a 42% chance to not lose casting time when you take damage.
  - current:   Gives you a 42% chance to avoid interruption caused by damage while casting Arcane and Nature spells.
- **Nature's Focus** rank 4
  - Wowhead: Gives your Arcane and Nature spells a 56% chance to not lose casting time when you take damage.
  - current:   Gives you a 56% chance to avoid interruption caused by damage while casting Arcane and Nature spells.
- **Nature's Focus** rank 5
  - Wowhead: Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage.
  - current:   Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells.
- **Nature's Reach** rank 1
  - Wowhead: Increases the range of your offensive Balance spells by 10% and improves your chance to hit by 2%.
  - current:   Increases the range of your offensive Balance spells by 10% and increases the chance for all your spells and attacks to hit by 2%.
- **Nature's Reach** rank 2
  - Wowhead: Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%.
  - current:   Increases the range of your offensive Balance spells by 20% and increases the chance for all your spells and attacks to hit by 4%.
- **Predatory Strikes** rank 1
  - Wowhead: Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 50% of your level.
  - current:   Increases your melee Attack Power by 50% of your level.
- **Predatory Strikes** rank 2
  - Wowhead: Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 100% of your level.
  - current:   Increases your melee Attack Power by 100% of your level.
- **Predatory Strikes** rank 3
  - Wowhead: Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level.
  - current:   Increases your melee Attack Power by 150% of your level.
- **Reflection** rank 2
  - Wowhead: Allows 33% of your Mana regeneration to continue while casting.
  - current:   Allows 34% of your Mana regeneration to continue while casting.
- **Reflection** rank 3
  - Wowhead: Allows 50% of your Mana regeneration to continue while casting.
  - current:   Allows 51% of your Mana regeneration to continue while casting.
- **Rend and Tear** rank 1
  - Wowhead: Increases damage done by your melee abilities on Bleeding targets by 3%.
  - current:   Increases damage done by your melee abilities on Bleeding targets by 2%.
- **Rend and Tear** rank 2
  - Wowhead: Increases damage done by your melee abilities on Bleeding targets by 6%.
  - current:   Increases damage done by your melee abilities on Bleeding targets by 4%.
- **Rend and Tear** rank 3
  - Wowhead: Increases damage done by your melee abilities on Bleeding targets by 9%.
  - current:   Increases damage done by your melee abilities on Bleeding targets by 6%.
- **Rend and Tear** rank 4
  - Wowhead: Increases damage done by your melee abilities on Bleeding targets by 12%.
  - current:   Increases damage done by your melee abilities on Bleeding targets by 8%.
- ... 6 more (see the JSON report)


## hunter

**Position**

| talent | Wowhead | current |
|---|---|---|
| Improved Revive Pet | `[1, 2]` | `[1, 3]` |
| Pathfinding | `[2, 0]` | `[1, 2]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Counterattack | `ability_warrior_challange` | `crop-counterattack` |
| Deadly Aspects | `spell_nature_ravenform` | `crop-deadly-aspects` |
| Deterrence | `ability_whirlwind` | `crop-deterrence` |
| Endurance Training | `spell_nature_reincarnation` | `crop-endurance-training` |
| Improved Stings | `ability_hunter_quickshot` | `crop-improved-stings` |
| Improved Wing Clip | `ability_rogue_trip` | `crop-improved-wing-clip` |
| Lacerating Strikes | `ability_gouge` | `crop-lacerating-strikes` |
| Predator's Edge | `ability_dualwield` | `crop-predators-edge` |
| Rapid Killing | `ability_hunter_rapidkilling` | `crop-rapid-killing` |
| Sniper Shot | `hunter_pvp_snipershot` | `crop-sniper-shot` |
| Spirit Bond | `ability_druid_demoralizingroar` | `classic_ability_druid_demoralizingroar` |
| Strider Kick | `ability_hunter_pet_tallstrider` | `crop-strider-kick` |
| Survival Tactics | `ability_ensnare` | `crop-survival-tactics` |
| Survivalist's Discipline | `ability_hunter_mastertactitian` | `crop-survivalists-discipline` |

**Rank text (51 differing rank(s))**

- **Barrage** rank 1
  - Wowhead: Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 5%.
  - current:   Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 3%.
- **Barrage** rank 2
  - Wowhead: Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%.
  - current:   Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 6%.
- **Barrage** rank 3
  - Wowhead: Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 15%.
  - current:   Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 9%.
- **Counterattack** rank 1
  - Wowhead: A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 26 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried.
  - current:   A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried.
- **Deadly Aspects** rank 1
  - Wowhead: While Aspect of the Hawk is active, Auto Shot has a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
  - current:   While Aspect of the Hawk is active, all normal ranged attacks have a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
- **Deadly Aspects** rank 2
  - Wowhead: While Aspect of the Hawk is active, Auto Shot has a 4% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 4% chance of increasing melee attack speed by 30% for 12 sec.
  - current:   While Aspect of the Hawk is active, all normal ranged attacks have a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
- **Deadly Aspects** rank 3
  - Wowhead: While Aspect of the Hawk is active, Auto Shot has a 6% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 6% chance of increasing melee attack speed by 30% for 12 sec.
  - current:   While Aspect of the Hawk is active, all normal ranged attacks have a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
- **Deadly Aspects** rank 4
  - Wowhead: While Aspect of the Hawk is active, Auto Shot has a 8% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 8% chance of increasing melee attack speed by 30% for 12 sec.
  - current:   While Aspect of the Hawk is active, all normal ranged attacks have a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
- **Deadly Aspects** rank 5
  - Wowhead: While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec.
  - current:   While Aspect of the Hawk is active, all normal ranged attacks have a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec.
- **Deflection** rank 1
  - Wowhead: Increases your Parry chance by 1%.
  - current:   Increases your Parry chance by 2%.
- **Deflection** rank 2
  - Wowhead: Increases your Parry chance by 2%.
  - current:   Increases your Parry chance by 4%.
- **Deflection** rank 3
  - Wowhead: Increases your Parry chance by 3%.
  - current:   Increases your Parry chance by 6%.
- **Deflection** rank 4
  - Wowhead: Increases your Parry chance by 4%.
  - current:   Increases your Parry chance by 8%.
- **Deflection** rank 5
  - Wowhead: Increases your Parry chance by 5%.
  - current:   Increases your Parry chance by 10%.
- **Entrapment** rank 2
  - Wowhead: When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 2 sec.
  - current:   When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec.
- **Entrapment** rank 3
  - Wowhead: When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 3 sec.
  - current:   When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec.
- **Entrapment** rank 4
  - Wowhead: When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 4 sec.
  - current:   When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec.
- **Entrapment** rank 5
  - Wowhead: When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 5 sec.
  - current:   When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec.
- **Expose Prey** rank 1
  - Wowhead: Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 5% chance to allow an activation of Mongoose Bite. Lasts 10 sec.
  - current:   Your attacks against targets with Hunter's Mark have a 5% chance to activate your Mongoose Bite for 5 sec.
- **Expose Prey** rank 2
  - Wowhead: Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec.
  - current:   Your attacks against targets with Hunter's Mark have a 5% chance to activate your Mongoose Bite for 5 sec.
- **Focused Fire** rank 1
  - Wowhead: Increases all damage you and your pet deal by 1% while your pet is active.
  - current:   Increases all damage you deal by 1% while your pet is active.
- **Focused Fire** rank 2
  - Wowhead: Increases all damage you and your pet deal by 2% while your pet is active.
  - current:   Increases all damage you deal by 2% while your pet is active.
- **Improved Aspect of the Monkey** rank 2
  - Wowhead: Increases the Dodge bonus of your Aspect of the Monkey by 4%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability.
  - current:   Increases the Dodge bonus of your Aspect of the Monkey by 4%. Additionally, your pet gains 100% of the effect of your Aspect of the Monkey ability.
- **Improved Aspect of the Monkey** rank 3
  - Wowhead: Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability.
  - current:   Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 150% of the effect of your Aspect of the Monkey ability.
- **Improved Mend Pet** rank 2
  - Wowhead: Gives your Mend Pet spell a 50% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 20%.
  - current:   Gives your Mend Pet spell a 15% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 10%.
- **Improved Stings** rank 1
  - Wowhead: Increases the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec.
  - current:   Increased the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec.
- **Improved Stings** rank 2
  - Wowhead: Increases the damage of your Serpent Sting ability by 13%, reduces the cooldown of your Viper Sting ability by 4 sec, and increases the duration of your Scorpid Sting ability by 30 sec.
  - current:   Increased the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec.
- **Improved Stings** rank 3
  - Wowhead: Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec.
  - current:   Increased the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec.
- **Improved Wing Clip** rank 2
  - Wowhead: Gives your Wing Clip ability a 13% chance to immobilize the target for 5 sec.
  - current:   Gives your Wing Clip ability a 14% chance to immobilize the target for 5 sec.
- **Improved Wing Clip** rank 3
  - Wowhead: Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec.
  - current:   Gives your Wing Clip ability a 21% chance to immobilize the target for 5 sec.
- **Lacerating Strikes** rank 1
  - Wowhead: Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec
  - current:   Your Mongoose Bite also causes the target to bleed for damage over 21 sec equal to 40% of the damage done by Mongoose Bite.
- **Lightning Reflexes** rank 1
  - Wowhead: Increases your Agility by 3%.
  - current:   Increases your Agility by 2%.
- **Lightning Reflexes** rank 2
  - Wowhead: Increases your Agility by 6%.
  - current:   Increases your Agility by 4%.
- **Lightning Reflexes** rank 3
  - Wowhead: Increases your Agility by 9%.
  - current:   Increases your Agility by 6%.
- **Lightning Reflexes** rank 4
  - Wowhead: Increases your Agility by 12%.
  - current:   Increases your Agility by 8%.
- **Lightning Reflexes** rank 5
  - Wowhead: Increases your Agility by 15%.
  - current:   Increases your Agility by 10%.
- **Predator's Edge** rank 1
  - Wowhead: Increases your melee ability critical strike damage by 6% and your Off Hand weapon damage by 10%.
  - current:   Increases your melee critical strike damage by 6% and your offhand weapon damage by 10%.
- **Predator's Edge** rank 2
  - Wowhead: Increases your melee ability critical strike damage by 12% and your Off Hand weapon damage by 20%.
  - current:   Increases your melee critical strike damage by 12% and your offhand weapon damage by 20%.
- **Predator's Edge** rank 3
  - Wowhead: Increases your melee ability critical strike damage by 18% and your Off Hand weapon damage by 30%.
  - current:   Increases your melee critical strike damage by 18% and your offhand weapon damage by 30%.
- **Predator's Edge** rank 4
  - Wowhead: Increases your melee ability critical strike damage by 24% and your Off Hand weapon damage by 40%.
  - current:   Increases your melee critical strike damage by 24% and your offhand weapon damage by 40%.
- **Predator's Edge** rank 5
  - Wowhead: Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%.
  - current:   Increases your melee critical strike damage by 30% and your offhand weapon damage by 50%.
- **Rapid Killing** rank 2
  - Wowhead: Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%.
  - current:   Reduces the cooldown on your Rapid Fire ability by 1 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next shot ability within 20 sec by 10%.
- **Rapid Recuperation** rank 1
  - Wowhead: Afflicting a target with Serpent Sting allows 25% of your Mana Regeneration to continue while casting for 15 sec, increased to 50% when Rapid Killing is consumed.
  - current:   Hitting a target with your Serpent Sting ability grants you 25% and consuming Rapid Killing grants you 50% of your Mana regeneration while casting for the next 15 sec.
- **Rapid Recuperation** rank 2
  - Wowhead: Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed.
  - current:   Hitting a target with your Serpent Sting ability grants you 25% and consuming Rapid Killing grants you 50% of your Mana regeneration while casting for the next 15 sec.
- **Resourcefulness** rank 1
  - Wowhead: Reduces the Mana cost of your Trap and melee abilities by 30%, and grants your melee and ranged ability Critical Strikes a 50% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec.
  - current:   Reduces the mana cost of your Trap abilities and melee abilities by 30%. In addition, your critical strikes have a 30% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec.
- **Resourcefulness** rank 2
  - Wowhead: Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec.
  - current:   Reduces the mana cost of your Trap abilities and melee abilities by 30%. In addition, your critical strikes have a 30% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec.
- **Sniper Shot** rank 1
  - Wowhead: A long-range shot that deals ranged damage plus 320 and increases the range of your next 3 Shots by 10 yards for 10 sec.
  - current:   A steady snipe that increases ranged damage by 160.
- **Spirit Bond** rank 2
  - Wowhead: While your pet is active, you and your pet will regenerate 1% of total health every 5 sec.
  - current:   While your pet is active, you and your pet will regenerate 2% of total health every 10 sec.
- **Strider Kick** rank 1
  - Wowhead: A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec.
  - current:   A powerful kick that deals 100% melee weapon damage.
- **Summon Hawk** rank 1
  - Wowhead: Command a hawk to dive-bomb your targeted enemy, dealing [32 / Ferocity: 48 / Unleashed Fury: 52 + (Ranged Attack Power * (0.05))] Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot.
  - current:   Command a hawk to dive-bomb your targeted enemy, dealing 53 Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot.
- **Trueshot Aura** rank 1
  - Wowhead: Increases the Ranged Attack Power of party or raid members within 45 yds by 20.
  - current:   Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min.


## mage

**New (Wowhead only)**

- `wh-105795` Accelerant - fire r0c2
- `wh-113627` Arcane Wrath - arcane r3c3
- `wh-105786` Heating Up - fire r3c2
- `wh-105797` Improved Fire Blast - fire r2c3
- `wh-105778` Precision - frost r0c2

**Gone (current only)**

- `arcane-focus` Arcane Focus - arcane r0c1
- `elemental-precision` Elemental Precision - frost r0c2
- `hot-streak` Hot Streak - fire r3c2
- `piercing-ice` Piercing Ice - frost r2c0
- `wake-of-fire` Wake of Fire - fire r0c0

**Position**

| talent | Wowhead | current |
|---|---|---|
| Arcane Resilience | `[0, 2]` | `[1, 3]` |
| Frost Channeling | `[2, 0]` | `[2, 1]` |
| Frostbite | `[1, 1]` | `[1, 3]` |
| Improved Blizzard | `[2, 1]` | `[2, 3]` |
| Improved Channeling | `[0, 1]` | `[0, 2]` |
| Missile Barrage | `[1, 3]` | `[3, 3]` |
| Permafrost | `[1, 3]` | `[1, 1]` |

**maxRank**

| talent | Wowhead | current |
|---|---|---|
| Arcane Resilience | `3` | `2` |
| Fire Power | `3` | `5` |
| Incineration | `5` | `3` |
| Missile Barrage | `2` | `1` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Arcane Geometry | `inv_ability_mage_radiantspark` | `crop-arcane-geometry` |
| Blast Wave | `spell_holy_excorcism_02` | `crop-blast-wave` |
| Fire Power | `spell_fire_immolation` | `crop-fire-power` |
| Impact | `spell_fire_meteorstorm` | `crop-impact` |
| Improved Channeling | `spell_nature_starfall` | `crop-improved-channeling` |
| Improved Scorch | `spell_fire_soulburn` | `spell_fire_windsofwoe` |
| Incineration | `spell_fire_flameshock` | `crop-incineration` |
| Master of Elements | `spell_fire_masterofelements` | `crop-master-of-elements` |
| Shatter | `spell_frost_frostshock` | `crop-shatter` |

**Rank text (46 differing rank(s))**

- **Arcane Blast** rank 1
  - Wowhead: Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application.
  - current:   Blasts the target with energy, dealing 95 to 104 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast.
- **Arcane Instability** rank 1
  - Wowhead: Increases the damage done by your spells by 1% and your critical strike chance by 1%.
  - current:   Increases the damage done by all your spells by 1% and your critical strike chance with all attacks by 1%.
- **Arcane Instability** rank 2
  - Wowhead: Increases the damage done by your spells by 2% and your critical strike chance by 2%.
  - current:   Increases the damage done by all your spells by 2% and your critical strike chance with all attacks by 2%.
- **Arcane Instability** rank 3
  - Wowhead: Increases the damage done by your spells by 3% and your critical strike chance by 3%.
  - current:   Increases the damage done by all your spells by 3% and your critical strike chance with all attacks by 3%.
- **Arcane Meditation** rank 2
  - Wowhead: Allows 33% of your Mana regeneration to continue while casting.
  - current:   Allows 34% of your Mana regeneration to continue while casting.
- **Arcane Meditation** rank 3
  - Wowhead: Allows 50% of your Mana regeneration to continue while casting.
  - current:   Allows 51% of your Mana regeneration to continue while casting.
- **Arcane Shielding** rank 2
  - Wowhead: Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 33% and increases the resistances granted by your Mage Armor spell by 50%.
  - current:   Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 34% and increases the resistances granted by your Mage Armor spell by 50%.
- **Arcane Subtlety** rank 2
  - Wowhead: Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%.
  - current:   Reduces your target's resistance to all your spells by 16 and reduces the threat caused by your Arcane spells by 30%.
- **Arctic Reach** rank 1
  - Wowhead: Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%.
  - current:   Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%.
- **Arctic Reach** rank 2
  - Wowhead: Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%.
  - current:   Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%.
- **Blast Wave** rank 1
  - Wowhead: A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec.
  - current:   A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 160 to 191 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec.
- **Burning Soul** rank 2
  - Wowhead: Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%.
  - current:   Gives your Fire spells a 46% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%.
- **Burning Soul** rank 3
  - Wowhead: Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%.
  - current:   Gives your Fire spells a 69% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%.
- **Combustion** rank 1
  - Wowhead: When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells.
  - current:   When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 4 non-periodic critical strikes with Fire spells.
- **Fingers of Frost** rank 2
  - Wowhead: Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec.
  - current:   Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 1 spell cast as if the target were frozen. Lasts 15 sec.
- **Fire Power** rank 1
  - Wowhead: Increases the damage done by your Fire spells by 1% per your Fire effects on the target, up to a maximum increase of 4%. Effects which mix multiple schools of magic do not qualify.
  - current:   Increases the damage done by your Fire spells by 2%.
- **Fire Power** rank 2
  - Wowhead: Increases the damage done by your Fire spells by 2% per your Fire effects on the target, up to a maximum increase of 8%. Effects which mix multiple schools of magic do not qualify.
  - current:   Increases the damage done by your Fire spells by 4%.
- **Fire Power** rank 3
  - Wowhead: Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify.
  - current:   Increases the damage done by your Fire spells by 6%.
- **Frost Warding** rank 1
  - Wowhead: Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 15%, gives your Frost Ward a 10% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 10%.
  - current:   Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active.
- **Frost Warding** rank 2
  - Wowhead: Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%.
  - current:   Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active.
- **Ice Barrier** rank 1
  - Wowhead: Shield yourself, absorbing [448 + (Frost spell power * 0.1) * (1)] damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage.
  - current:   Instantly shields you, absorbing 431 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage.
- **Ice Lance** rank 1
  - Wowhead: Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets.
  - current:   Deals 28 to 33 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets.
- **Impact** rank 2
  - Wowhead: Gives your Fire spells a 7% chance to stun the target for 2 sec.
  - current:   Gives your Fire spells a 6% chance to stun the target for 2 sec.
- **Impact** rank 3
  - Wowhead: Gives your Fire spells a 10% chance to stun the target for 2 sec.
  - current:   Gives your Fire spells a 9% chance to stun the target for 2 sec.
- **Improved Blizzard** rank 2
  - Wowhead: Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 25% for 1.5 sec.
  - current:   Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 30% for 1.5 sec.
- **Improved Blizzard** rank 3
  - Wowhead: Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 40% for 1.5 sec.
  - current:   Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 45% for 1.5 sec.
- **Improved Channeling** rank 1
  - Wowhead: Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage.
  - current:   Gives you a 20% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 14% chance while casting Arcane Blast.
- **Improved Channeling** rank 2
  - Wowhead: Gives your Arcane Missiles spell a 40% chance and your Arcane Blast and Arcane Wrath spells a 28% chance to not lose casting time when you take damage.
  - current:   Gives you a 40% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 28% chance while casting Arcane Blast.
- **Improved Channeling** rank 3
  - Wowhead: Gives your Arcane Missiles spell a 60% chance and your Arcane Blast and Arcane Wrath spells a 42% chance to not lose casting time when you take damage.
  - current:   Gives you a 60% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 42% chance while casting Arcane Blast.
- **Improved Channeling** rank 4
  - Wowhead: Gives your Arcane Missiles spell a 80% chance and your Arcane Blast and Arcane Wrath spells a 56% chance to not lose casting time when you take damage.
  - current:   Gives you a 80% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 56% chance while casting Arcane Blast.
- **Improved Channeling** rank 5
  - Wowhead: Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage.
  - current:   Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast.
- **Improved Cone of Cold** rank 2
  - Wowhead: Increases the damage dealt by your Cone of Cold spell by 23%.
  - current:   Increases the damage dealt by your Cone of Cold spell by 24%.
- **Improved Cone of Cold** rank 3
  - Wowhead: Increases the damage dealt by your Cone of Cold spell by 35%.
  - current:   Increases the damage dealt by your Cone of Cold spell by 36%.
- **Improved Counterspell** rank 2
  - Wowhead: Your Counterspell also Silences the target for 4 sec.
  - current:   Your Counterspell also Silences the target for 2 sec.
- **Improved Scorch** rank 2
  - Wowhead: Your Scorch spell has a 67% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times.
  - current:   Your Scorch spell has a 66% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times.
- **Missile Barrage** rank 1
  - Wowhead: Gives your Arcane Blast spell a 20% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec.
  - current:   Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles will fire every 0.5 sec.
- **Permafrost** rank 2
  - Wowhead: Increases the duration of your Chill effects by 22% and reduces the target's speed by an additional 7%.
  - current:   Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%.
- **Permafrost** rank 3
  - Wowhead: Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%.
  - current:   Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%.
- **Pyroblast** rank 1
  - Wowhead: Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec.
  - current:   Hurls an immense fiery boulder that causes 155 to 185 Fire damage and an additional 76 Fire damage over 12 sec.
- **Shatter** rank 1
  - Wowhead: Increases the critical strike chance of all your spells against Frozen targets by 17%.
  - current:   Increases the critical strike chance of all your spells against Frozen targets by 50%.
- **Shatter** rank 2
  - Wowhead: Increases the critical strike chance of all your spells against Frozen targets by 33%.
  - current:   Increases the critical strike chance of all your spells against Frozen targets by 50%.
- **Winter's Chill** rank 1
  - Wowhead: Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 20% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times.
  - current:   Gives your frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times.
- **Winter's Chill** rank 2
  - Wowhead: Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 40% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times.
  - current:   Gives your frost damage spells a 40% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times.
- **Winter's Chill** rank 3
  - Wowhead: Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 60% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times.
  - current:   Gives your frost damage spells a 60% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times.
- **Winter's Chill** rank 4
  - Wowhead: Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 80% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times.
  - current:   Gives your frost damage spells a 80% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times.
- **Winter's Chill** rank 5
  - Wowhead: Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 100% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times.
  - current:   Gives your frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times.


## paladin

**New (Wowhead only)**

- `wh-113631` Boundless Light - holy r4c2
- `wh-105330` Oath of Light - holy r3c2
- `wh-110875` Shieldsworn - protection r6c1
- `wh-105639` Stoicism - protection r4c0
- `wh-113629` Turn Evil - combat r4c0
- `wh-105692` Unsealed Wrath - combat r6c1

**Gone (current only)**

- `crusade` Crusade - retribution r3c3
- `improved-holy-strike` Improved Holy Strike - holy r0c0
- `improved-seal-of-fury` Improved Seal of Fury - protection r2c0
- `instrument-of-law` Instrument of Law - retribution r5c2
- `one-handed-weapon-specialization` One-Handed Weapon Specialization - protection r3c1
- `twist-of-light` Twist of Light - retribution r6c1
- `voice-of-truth` Voice of Truth - holy r2c0

**Tree moved**

| talent | Wowhead | current |
|---|---|---|
| Benediction | `combat` | `retribution` |
| Champion of the Light | `combat` | `retribution` |
| Conviction | `combat` | `retribution` |
| Deflection | `combat` | `retribution` |
| Divine Intellect | `protection` | `holy` |
| Eye for an Eye | `combat` | `retribution` |
| Holy Conduit | `holy` | `retribution` |
| Improved Judgement | `combat` | `retribution` |
| Pursuit of Justice | `combat` | `retribution` |
| Repentance | `combat` | `retribution` |
| Sacred Arbiter | `combat` | `retribution` |
| Sanctified Judgement | `combat` | `retribution` |
| Seal of Command | `combat` | `retribution` |
| Two-Handed Weapon Specialization | `combat` | `retribution` |
| Unyielding Faith | `combat` | `holy` |
| Vengeance | `combat` | `retribution` |
| Vindication | `combat` | `retribution` |

**Position**

| talent | Wowhead | current |
|---|---|---|
| Anticipation | `[3, 2]` | `[1, 3]` |
| Champion of the Light | `[5, 2]` | `[5, 1]` |
| Consecrated Ground | `[4, 0]` | `[4, 2]` |
| Conviction | `[1, 1]` | `[1, 2]` |
| Divine Favor | `[2, 0]` | `[3, 2]` |
| Divine Intellect | `[0, 1]` | `[0, 2]` |
| Divine Precision | `[3, 0]` | `[4, 0]` |
| Divine Strength | `[0, 2]` | `[0, 1]` |
| Holy Conduit | `[2, 2]` | `[1, 1]` |
| Holy Shield | `[4, 1]` | `[6, 1]` |
| Illumination | `[2, 1]` | `[3, 1]` |
| Improved Hammer of Justice | `[2, 1]` | `[3, 2]` |
| Improved Righteous Fury | `[3, 1]` | `[2, 1]` |
| Infusion of Light | `[3, 1]` | `[3, 0]` |
| Purifying Power | `[1, 3]` | `[2, 2]` |
| Repentance | `[4, 1]` | `[4, 2]` |
| Reverence | `[1, 1]` | `[2, 1]` |
| Sacred Arbiter | `[3, 1]` | `[3, 2]` |
| Sacred Duty | `[1, 3]` | `[2, 3]` |
| Sanctified Judgement | `[1, 2]` | `[2, 1]` |
| Spiritual Focus | `[0, 1]` | `[1, 1]` |
| Templar's Bulwark | `[2, 0]` | `[4, 1]` |
| Toughness | `[2, 3]` | `[0, 1]` |
| Two-Handed Weapon Specialization | `[3, 3]` | `[4, 0]` |
| Unyielding Faith | `[2, 1]` | `[1, 3]` |
| Vengeance | `[4, 2]` | `[4, 1]` |

**maxRank**

| talent | Wowhead | current |
|---|---|---|
| Champion of the Light | `5` | `3` |
| Conviction | `3` | `5` |
| Divine Precision | `2` | `3` |
| Improved Seals | `5` | `3` |
| Iron Creed | `3` | `5` |
| Reverence | `2` | `3` |
| Shield Specialization | `2` | `3` |
| Spiritual Focus | `5` | `2` |

**Prerequisites**

| talent | Wowhead | current |
|---|---|---|
| Divine Precision | `[]` | `[('holy shock', 1)]` |
| Holy Shield | `[]` | `[("templar's bulwark", 1)]` |
| Illumination | `[('reverence', 2)]` | `[('reverence', 3)]` |
| Swift Judgement | `[("templar's bulwark", 1)]` | `[('improved seal of fury', 1)]` |
| Vengeance | `[('seal of command', 1)]` | `[('sanctified judgement', 3)]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Conviction | `spell_holy_retributionaura` | `crop-conviction` |
| Divine Favor | `spell_holy_heal` | `crop-divine-favor` |
| Divine Intellect | `spell_nature_sleep` | `crop-divine-intellect` |
| Divine Precision | `spell_holy_mindsooth` | `crop-divine-precision` |
| Holy Conduit | `spell_holy_devineaegis` | `crop-holy-conduit` |
| Holy Shield | `spell_holy_blessingofprotection` | `classic_spell_holy_blessingofprotection` |
| Iron Creed | `spell_holy_improvedresistanceauras` | `crop-iron-creed` |
| Sacred Arbiter | `inv_sword_08` | `crop-sacred-arbiter` |
| Sacred Duty | `spell_holy_divineintervention` | `crop-sacred-duty` |
| Sanctified Judgement | `ability_paladin_judgementblue` | `spell_holy_righteousfury` |
| Shield Specialization | `inv_shield_06` | `crop-shield-specialization` |
| Templar's Bulwark | `ability_paladin_shieldofthetemplar` | `crop-templars-bulwark` |

**Rank text (65 differing rank(s))**

- **Champion of the Light** rank 1
  - Wowhead: Increases your spell damage by up to 12% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.2 sec.
  - current:   Increases your spell damage and healing by up to 33% of your Intellect.
- **Champion of the Light** rank 2
  - Wowhead: Increases your spell damage by up to 24% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.4 sec.
  - current:   Increases your spell damage and healing by up to 66% of your Intellect.
- **Champion of the Light** rank 3
  - Wowhead: Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec.
  - current:   Increases your spell damage and healing by up to 99% of your Intellect.
- **Consecrated Ground** rank 2
  - Wowhead: Gives your Holy spells 10% increased damage against the first 4 enemies that enter your Consecration.
  - current:   Gives your Holy spells 10% increased damage against the first 8 enemies that enter your Consecration.
- **Conviction** rank 1
  - Wowhead: Improves your chance to get a critical strike with all spells and attacks by 2%.
  - current:   Increases your chance to get a critical strike with melee attacks by 1%.
- **Conviction** rank 2
  - Wowhead: Improves your chance to get a critical strike with all spells and attacks by 4%.
  - current:   Increases your chance to get a critical strike with melee attacks by 2%.
- **Conviction** rank 3
  - Wowhead: Improves your chance to get a critical strike with all spells and attacks by 6%.
  - current:   Increases your chance to get a critical strike with melee attacks by 3%.
- **Divine Precision** rank 1
  - Wowhead: Improves your chance to hit with Holy spells by 4%, and reduces the duration of Silence effects on you by 10%.
  - current:   Increases your chance to hit with Holy spells by 6%.
- **Divine Precision** rank 2
  - Wowhead: Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%.
  - current:   Increases your chance to hit with Holy spells by 12%.
- **Holy Power** rank 1
  - Wowhead: Increases the critical strike healing bonus of your Holy spells by 10%.
  - current:   Increases the critical strike chance of your Holy Shock spell by 3%, and all other spells by 1%.
- **Holy Power** rank 2
  - Wowhead: Increases the critical strike healing bonus of your Holy spells by 20%.
  - current:   Increases the critical strike chance of your Holy Shock spell by 6%, and all other spells by 2%.
- **Holy Power** rank 3
  - Wowhead: Increases the critical strike healing bonus of your Holy spells by 30%.
  - current:   Increases the critical strike chance of your Holy Shock spell by 9%, and all other spells by 3%.
- **Holy Power** rank 4
  - Wowhead: Increases the critical strike healing bonus of your Holy spells by 40%.
  - current:   Increases the critical strike chance of your Holy Shock spell by 12%, and all other spells by 4%.
- **Holy Power** rank 5
  - Wowhead: Increases the critical strike healing bonus of your Holy spells by 50%.
  - current:   Increases the critical strike chance of your Holy Shock spell by 15%, and all other spells by 5%.
- **Holy Shield** rank 1
  - Wowhead: Increases chance to block by 30% for 10 sec, and deals 75 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges.
  - current:   Increases chance to block by 20% for 10 sec. and deals 110 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges.
- **Illumination** rank 2
  - Wowhead: After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 40% chance to gain Mana equal to 50% of the base cost of the spell.
  - current:   After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 40% chance to gain Mana equal to 100% of the base cost of the spell.
- **Illumination** rank 3
  - Wowhead: After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 60% chance to gain Mana equal to 50% of the base cost of the spell.
  - current:   After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 60% chance to gain Mana equal to 150% of the base cost of the spell.
- **Illumination** rank 4
  - Wowhead: After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 80% chance to gain Mana equal to 50% of the base cost of the spell.
  - current:   After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 80% chance to gain Mana equal to 200% of the base cost of the spell.
- **Illumination** rank 5
  - Wowhead: After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell.
  - current:   After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 250% of the base cost of the spell.
- **Improved Righteous Fury** rank 1
  - Wowhead: While Righteous Fury is active, all damage taken is reduced by 3%.
  - current:   While Righteous Fury is active, all damage taken is reduced by 2%.
- **Improved Righteous Fury** rank 2
  - Wowhead: While Righteous Fury is active, all damage taken is reduced by 6%.
  - current:   While Righteous Fury is active, all damage taken is reduced by 4%.
- **Improved Righteous Fury** rank 3
  - Wowhead: While Righteous Fury is active, all damage taken is reduced by 9%.
  - current:   While Righteous Fury is active, all damage taken is reduced by 6%.
- **Improved Seals** rank 1
  - Wowhead: Increases the damage done by your Seals and Judgements by 3%.
  - current:   Increases the damage done by your Seals and Judgements by 5%.
- **Improved Seals** rank 2
  - Wowhead: Increases the damage done by your Seals and Judgements by 6%.
  - current:   Increases the damage done by your Seals and Judgements by 10%.
- **Improved Seals** rank 3
  - Wowhead: Increases the damage done by your Seals and Judgements by 9%.
  - current:   Increases the damage done by your Seals and Judgements by 15%.
- **Infusion of Light** rank 2
  - Wowhead: Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec.
  - current:   Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec.
- **Iron Creed** rank 1
  - Wowhead: Increases the threat generated by your Holy Strike ability by 10%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2% for 6 sec.
  - current:   Increases the threat generated by your Holy Strike ability 5%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2% for 6 sec.
- **Iron Creed** rank 2
  - Wowhead: Increases the threat generated by your Holy Strike ability by 20%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 4% for 6 sec.
  - current:   Increases the threat generated by your Holy Strike ability 5%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2% for 6 sec.
- **Iron Creed** rank 3
  - Wowhead: Increases the threat generated by your Holy Strike ability by 30%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 6% for 6 sec.
  - current:   Increases the threat generated by your Holy Strike ability 5%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2% for 6 sec.
- **Light's Vigil** rank 1
  - Wowhead: Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 326 to 344. Only one Vigil per Paladin may be active in each party.
  - current:   Applies Light's Vigil to the target for 30 sec. Your next Holy Shock cast on them triggers no cooldown and causes friendly targets to heal their party for 315 to 333, or enemy targets to suffer 175 to 189 Holy damage and refund 75% of Light's Vigil's Mana cost. You may only have 1 Light's Vigil active per Paladin, per party.
- **Precision** rank 1
  - Wowhead: Improves your chance to hit by 1%.
  - current:   Increases your chance to hit with all spells and attacks by 1%.
- **Precision** rank 2
  - Wowhead: Improves your chance to hit by 2%.
  - current:   Increases your chance to hit with all spells and attacks by 2%.
- **Precision** rank 3
  - Wowhead: Improves your chance to hit by 3%.
  - current:   Increases your chance to hit with all spells and attacks by 3%.
- **Purifying Power** rank 2
  - Wowhead: Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%.
  - current:   Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 34%.
- **Pursuit of Justice** rank 2
  - Wowhead: Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects.
  - current:   Increases movement speed and mounted movement speed by 16%. This does not stack with other movement speed increasing effects.
- **Reckoning** rank 1
  - Wowhead: Gives you a 8% chance after Blocking and a 20% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.
  - current:   Gives you a 8% chance to gain an extra attack after Blocking a melee attack and a 20% chance to gain an extra attack after being the victim of a non-periodic critical strike.
- **Reckoning** rank 2
  - Wowhead: Gives you a 16% chance after Blocking and a 40% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.
  - current:   Gives you a 16% chance to gain an extra attack after Blocking a melee attack and a 40% chance to gain an extra attack after being the victim of a non-periodic critical strike.
- **Reckoning** rank 3
  - Wowhead: Gives you a 24% chance after Blocking and a 60% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.
  - current:   Gives you a 24% chance to gain an extra attack after Blocking a melee attack and a 60% chance to gain an extra attack after being the victim of a non-periodic critical strike.
- **Reckoning** rank 4
  - Wowhead: Gives you a 32% chance after Blocking and a 80% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.
  - current:   Gives you a 32% chance to gain an extra attack after Blocking a melee attack and a 80% chance to gain an extra attack after being the victim of a non-periodic critical strike.
- **Reckoning** rank 5
  - Wowhead: Gives you a 40% chance after Blocking and a 100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.
  - current:   Gives you a 40% chance to gain an extra attack after Blocking a melee attack and a 100% chance to gain an extra attack after being the victim of a non-periodic critical strike.
- **Redoubt** rank 2
  - Wowhead: Damaging melee attacks against you have a 10% chance to increase your chance to block by 12%. Lasts 10 sec or 5 blocks.
  - current:   Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks.
- **Redoubt** rank 3
  - Wowhead: Damaging melee attacks against you have a 10% chance to increase your chance to block by 18%. Lasts 10 sec or 5 blocks.
  - current:   Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks.
- **Redoubt** rank 4
  - Wowhead: Damaging melee attacks against you have a 10% chance to increase your chance to block by 24%. Lasts 10 sec or 5 blocks.
  - current:   Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks.
- **Redoubt** rank 5
  - Wowhead: Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks.
  - current:   Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks.
- **Reverence** rank 1
  - Wowhead: Allows 15% of your Mana regeneration to continue while casting.
  - current:   Allows 10% of your Mana regeneration to continue while casting.
- **Reverence** rank 2
  - Wowhead: Allows 30% of your Mana regeneration to continue while casting.
  - current:   Allows 20% of your Mana regeneration to continue while casting.
- **Sacred Arbiter** rank 1
  - Wowhead: Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target.
  - current:   Increases the damage of your Holy Strike ability by 10% and causes it to refresh all Judgement effects on the target.
- **Sacred Duty** rank 1
  - Wowhead: Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec, and reduces the duration of Forbearance by 5 sec.
  - current:   Increases your total Stamina by 2% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec.
- **Sacred Duty** rank 2
  - Wowhead: Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec.
  - current:   Increases your total Stamina by 2% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec.
- **Sanctified Judgement** rank 3
  - Wowhead: Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal.
  - current:   Gives your Judgement ability a 99% chance to return 60% of the Mana cost of the judged seal.
- **Seal of Command** rank 1
  - Wowhead: Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec. Unleashing this Seal's energy will judge an enemy, instantly causing 69 to 73 Holy damage, 138 to 146 if the target is stunned or incapacitated.
  - current:   Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec. Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 146 if the target is stunned or incapacitated.
- **Shield Specialization** rank 1
  - Wowhead: Increases the amount of damage absorbed by your shield by 15%, and gives your blocks a 50% chance to restore 4% of your maximum Mana. May only occur once every 3 sec.
  - current:   Increases the amount of damage absorbed by your shield by 10%, and gives your blocks a 33% chance to restore 6% of your maximum Mana. May only occur once every 3 sec.
- **Shield Specialization** rank 2
  - Wowhead: Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 4% of your maximum Mana. May only occur once every 3 sec.
  - current:   Increases the amount of damage absorbed by your shield by 10%, and gives your blocks a 33% chance to restore 6% of your maximum Mana. May only occur once every 3 sec.
- **Spiritual Focus** rank 1
  - Wowhead: Gives your Flash of Light, Holy Light, and Light's Vigil spells a 14% chance to not lose casting time when you take damage.
  - current:   Gives your Flash of Light, Holy Light, and Light's Vigil spells a 35% chance to not lose casting time when you take damage.
- **Spiritual Focus** rank 2
  - Wowhead: Gives your Flash of Light, Holy Light, and Light's Vigil spells a 28% chance to not lose casting time when you take damage.
  - current:   Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage.
- **Swift Judgement** rank 1
  - Wowhead: Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability.
  - current:   Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%.
- **Two-Handed Weapon Specialization** rank 1
  - Wowhead: Increases the Physical and Holy damage you deal by 2%, and reduces all threat you generate by 7% while a two-handed melee weapon is equipped.
  - current:   Increases the damage you deal with two-handed melee weapons by 3%.
- **Two-Handed Weapon Specialization** rank 2
  - Wowhead: Increases the Physical and Holy damage you deal by 4%, and reduces all threat you generate by 14% while a two-handed melee weapon is equipped.
  - current:   Increases the damage you deal with two-handed melee weapons by 6%.
- **Two-Handed Weapon Specialization** rank 3
  - Wowhead: Increases the Physical and Holy damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped.
  - current:   Increases the damage you deal with two-handed melee weapons by 9%.
- **Vengeance** rank 1
  - Wowhead: Increases your Physical and Holy damage dealt by 1% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times.
  - current:   Increases your Physical and Holy damage dealt by 1% for 30 sec after landing a critical strike. Stacks up to 5 times.
- ... 5 more (see the JSON report)


## priest

**New (Wowhead only)**

- `wh-105823` Dark Inspiration - shadow r3c0
- `wh-105856` Holy Binding - holy r3c3

**Gone (current only)**

- `binding-heal` Binding Heal - holy r3c3
- `improved-fade` Improved Fade - shadow-magic r3c0
- `shadow-affinity` Shadow Affinity - shadow-magic r1c0

**Tree moved**

| talent | Wowhead | current |
|---|---|---|
| Blackout | `shadow` | `shadow-magic` |
| Darkness | `shadow` | `shadow-magic` |
| Devouring Contagion | `shadow` | `shadow-magic` |
| Early Demise | `shadow` | `shadow-magic` |
| Improved Mind Blast | `shadow` | `shadow-magic` |
| Improved Mind Flay | `shadow` | `shadow-magic` |
| Improved Psychic Scream | `shadow` | `shadow-magic` |
| Improved Shadow Word: Pain | `shadow` | `shadow-magic` |
| Mind Flay | `shadow` | `shadow-magic` |
| Shadow Focus | `shadow` | `shadow-magic` |
| Shadow Reach | `shadow` | `shadow-magic` |
| Shadow Weaving | `shadow` | `shadow-magic` |
| Shadowform | `shadow` | `shadow-magic` |
| Silence | `shadow` | `shadow-magic` |
| Spirit Tap | `shadow` | `shadow-magic` |
| Vampiric Embrace | `shadow` | `shadow-magic` |

**Position**

| talent | Wowhead | current |
|---|---|---|
| Improved Mana Burn | `[3, 1]` | `[3, 3]` |
| Improved Mind Blast | `[1, 0]` | `[2, 0]` |
| Improved Power Word: Shield | `[2, 2]` | `[1, 2]` |
| Mental Strength | `[1, 2]` | `[3, 1]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Devouring Contagion | `spell_shadow_devouringplague` | `crop-devouring-contagion` |
| Improved Renew | `spell_holy_renew` | `crop-improved-renew` |
| Power in Light | `spell_holy_searinglight` | `crop-power-in-light` |
| Twilight Focus | `spell_holy_healingfocus` | `crop-twilight-focus` |
| Twin Disciplines | `spell_holy_sealofvengeance` | `crop-twin-disciplines` |

**Rank text (69 differing rank(s))**

- **Blessed Recovery** rank 2
  - Wowhead: After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 17% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing.
  - current:   After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 8% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing.
- **Blessed Recovery** rank 3
  - Wowhead: After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 25% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing.
  - current:   After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 8% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing.
- **Devouring Contagion** rank 1
  - Wowhead: Reduces the mana cost of your Devouring Plague by 25%. Targets that die while Devouring Plague is active spreads it, jumping to 2 nearby enemies within 5 yds for the remaining duration.
  - current:   Reduces the mana cost of your Devouring Plague by 25%. Targets that die while Devouring Plague is active spreads it, jumping to a nearby enemy within 5 yards for the remaining duration.
- **Devouring Contagion** rank 2
  - Wowhead: Reduces the mana cost of your Devouring Plague by 50%. Targets that die while Devouring Plague is active spreads it, jumping to 2 nearby enemies within 10 yds for the remaining duration.
  - current:   Reduces the mana cost of your Devouring Plague by 50%. Targets that die while Devouring Plague is active spreads it, jumping to a nearby enemy within 10 yards for the remaining duration.
- **Divine Aegis** rank 1
  - Wowhead: Your non-periodic critical heals create a protective shield on the target, absorbing 5% of the amount healed. Shields up to (20 * 60) damage and lasts 12 sec.
  - current:   Your critical heals create a protective shield on the target, absorbing 5% of the amount healed. Lasts 12 sec.
- **Divine Aegis** rank 2
  - Wowhead: Your non-periodic critical heals create a protective shield on the target, absorbing 10% of the amount healed. Shields up to (20 * 60) damage and lasts 12 sec.
  - current:   Your critical heals create a protective shield on the target, absorbing 5% of the amount healed. Lasts 12 sec.
- **Divine Aegis** rank 3
  - Wowhead: Your non-periodic critical heals create a protective shield on the target, absorbing 15% of the amount healed. Shields up to (20 * 60) damage and lasts 12 sec.
  - current:   Your critical heals create a protective shield on the target, absorbing 5% of the amount healed. Lasts 12 sec.
- **Early Demise** rank 2
  - Wowhead: Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 30%.
  - current:   Increases Shadow Word: Death's critical strike chance on targets at or below 40% health by 30%.
- **Holy Nova** rank 1
  - Wowhead: Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 50 to 57. These effects cause no threat.
  - current:   Causes an explosion of holy light around the caster, causing 30 to 35 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 64 to 73. These effects cause no threat.
- **Holy Precision** rank 1
  - Wowhead: Improves your chance to hit with Holy spells by 6%.
  - current:   Increases your chance to hit with Holy spells by 6%.
- **Holy Precision** rank 2
  - Wowhead: Improves your chance to hit with Holy spells by 12%.
  - current:   Increases your chance to hit with Holy spells by 12%.
- **Holy Precision** rank 3
  - Wowhead: Improves your chance to hit with Holy spells by 18%.
  - current:   Increases your chance to hit with Holy spells by 18%.
- **Improved Mana Burn** rank 2
  - Wowhead: Reduces the casting time of your Mana Burn spell by 1.0 sec.
  - current:   Reduces the casting time of your Mana Burn spell by 0.5 sec.
- **Improved Mind Flay** rank 1
  - Wowhead: Each instance of damage of Mind Flay deals 10% more damage than its previous instance of damage.
  - current:   Your Mind Flay now deals 10% more damage, gains 5 yards increased range, but slows the target's movement speed by 35%.
- **Improved Mind Flay** rank 2
  - Wowhead: Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage.
  - current:   Your Mind Flay now deals 10% more damage, gains 5 yards increased range, but slows the target's movement speed by 35%.
- **Improved Power Word: Shield** rank 3
  - Wowhead: Increases the damage absorbed by your Power Word: Shield by 20%.
  - current:   Increases the damage absorbed by your Power Word: Shield by 21%.
- **Inner Focus** rank 1
  - Wowhead: When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect.
  - current:   When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is capable of a critical effect.
- **Inspiration** rank 2
  - Wowhead: Your non-periodic critical heals increase your target's Armor by 17% for 15 sec.
  - current:   Your non-periodic critical heals increase your target's Armor by 16% for 15 sec.
- **Martyrdom** rank 2
  - Wowhead: Gives you a 100% chance to gain Focused Casting for 6 sec after being the victim of a melee or ranged critical strike. The Focused Casting effect prevents you from losing casting time when taking damage and increases your resistance to Interrupt effects by 20%.
  - current:   Gives you a 100% chance to gain Focused Casting for 6 sec after being the victim of a melee or ranged critical strike. The Focused Casting effect prevents you from losing Casting time when taking damage and increases your resistance to Interrupt effects by 40%.
- **Meditation** rank 2
  - Wowhead: Allows 33% of your Mana regeneration to continue while casting.
  - current:   Allows 34% of your Mana regeneration to continue while casting.
- **Meditation** rank 3
  - Wowhead: Allows 50% of your Mana regeneration to continue while casting.
  - current:   Allows 51% of your Mana regeneration to continue while casting.
- **Mental Agility** rank 2
  - Wowhead: Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 7%.
  - current:   Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 6%.
- **Mental Agility** rank 3
  - Wowhead: Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%.
  - current:   Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 9%.
- **Mental Strength** rank 1
  - Wowhead: Increases your total Intellect by 2%.
  - current:   Increases your total Intellect by 3%.
- **Mental Strength** rank 2
  - Wowhead: Increases your total Intellect by 4%.
  - current:   Increases your total Intellect by 6%.
- **Mental Strength** rank 3
  - Wowhead: Increases your total Intellect by 6%.
  - current:   Increases your total Intellect by 9%.
- **Mental Strength** rank 4
  - Wowhead: Increases your total Intellect by 8%.
  - current:   Increases your total Intellect by 12%.
- **Mental Strength** rank 5
  - Wowhead: Increases your total Intellect by 10%.
  - current:   Increases your total Intellect by 15%.
- **Mind Flay** rank 1
  - Wowhead: Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%.
  - current:   Assault the target's mind with Shadow energy, causing 119 Shadow damage over 3 sec and slowing their movement speed by 50%.
- **Penance** rank 1
  - Wowhead: Launches a volley of holy light at the target, causing 45 Holy damage to an enemy, or 134 healing to an ally, instantly and every 1 sec for 2 sec.
  - current:   Launches a volley of holy light at the target, causing 93 Holy damage to an enemy, or 223 healing to an ally, instantly and every 1 sec for 2 sec.
- **Power in Light** rank 1
  - Wowhead: Your Smite and Penance spells deal 2% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain.
  - current:   Your Smite and Penance spells deal 2% increased damage to targets afflicted with your Holy Fire.
- **Power in Light** rank 2
  - Wowhead: Your Smite and Penance spells deal 4% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain.
  - current:   Your Smite and Penance spells deal 4% increased damage to targets afflicted with your Holy Fire.
- **Power in Light** rank 3
  - Wowhead: Your Smite and Penance spells deal 6% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain.
  - current:   Your Smite and Penance spells deal 6% increased damage to targets afflicted with your Holy Fire.
- **Power in Light** rank 4
  - Wowhead: Your Smite and Penance spells deal 8% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain.
  - current:   Your Smite and Penance spells deal 8% increased damage to targets afflicted with your Holy Fire.
- **Power in Light** rank 5
  - Wowhead: Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain.
  - current:   Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire.
- **Prayer of Mending** rank 1
  - Wowhead: Places a spell on the target that heals them for [(172 + (Healing * 0.42899999)) * (1 * 1)] the next time they take damage or receive non-periodic healing. When the heal occurs, Prayer of Mending jumps to a party or raid member within 20 yards. Jumps up to 5 times and lasts 30 sec after each jump. This spell can only be placed on one target at a time per caster.
  - current:   Places a spell on the target that heals them for 231 the next time they take damage or receive non-periodic healing. When the heal occurs, Prayer of Mending jumps to a party or raid member within 20 yards. Jumps up to 5 times and lasts 30 sec after each jump. This spell can only be placed on one target at a time per caster.
- **Renewed Hope** rank 1
  - Wowhead: Your heals from Flash Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 2% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 1 sec.
  - current:   Your heals from Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 2% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 1 sec.
- **Renewed Hope** rank 2
  - Wowhead: Your heals from Flash Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 4% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 2 sec.
  - current:   Your heals from Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 2% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 1 sec.
- **Renewed Hope** rank 3
  - Wowhead: Your heals from Flash Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 6% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 3 sec.
  - current:   Your heals from Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 2% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 1 sec.
- **Renewed Hope** rank 4
  - Wowhead: Your heals from Flash Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 8% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 4 sec.
  - current:   Your heals from Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 2% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 1 sec.
- **Renewed Hope** rank 5
  - Wowhead: Your heals from Flash Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 10% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 5 sec.
  - current:   Your heals from Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal, and Penance gain 2% increased critical strike chance when cast on targets with Weakened Soul, and reduce the remaining duration of Weakened Soul on their target by 1 sec.
- **Searing Light** rank 2
  - Wowhead: Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana.
  - current:   Increases your Holy damage done by 4%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana.
- **Shadow Focus** rank 1
  - Wowhead: Improves your chance to hit with Shadow spells by 1%.
  - current:   Increases your chance to hit with your Shadow spells by 1%.
- **Shadow Focus** rank 2
  - Wowhead: Improves your chance to hit with Shadow spells by 2%.
  - current:   Increases your chance to hit with your Shadow spells by 2%.
- **Shadow Focus** rank 3
  - Wowhead: Improves your chance to hit with Shadow spells by 3%.
  - current:   Increases your chance to hit with your Shadow spells by 3%.
- **Shadow Focus** rank 4
  - Wowhead: Improves your chance to hit with Shadow spells by 4%.
  - current:   Increases your chance to hit with your Shadow spells by 4%.
- **Shadow Focus** rank 5
  - Wowhead: Improves your chance to hit with Shadow spells by 5%.
  - current:   Increases your chance to hit with your Shadow spells by 5%.
- **Shadow Weaving** rank 1
  - Wowhead: Your Shadow damage spells have a 33% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times.
  - current:   Your Shadow damage spells have a 33% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times.
- **Shadow Weaving** rank 2
  - Wowhead: Your Shadow damage spells have a 67% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times.
  - current:   Your Shadow damage spells have a 66% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times.
- **Shadow Weaving** rank 3
  - Wowhead: Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times.
  - current:   Your Shadow damage spells have a 99% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times.
- **Silent Resolve** rank 1
  - Wowhead: Reduces the threat generated by your spells by 10% and reduces the duration of Stun, Fear, and Silence effects inflicted on you by 5%.
  - current:   Reduces the threat generated by your Holy spells by 10% and reduces the duration of Stun, Fear, and Silence effects inflicted on you by 5%.
- **Silent Resolve** rank 2
  - Wowhead: Reduces the threat generated by your spells by 20% and reduces the duration of Stun, Fear, and Silence effects inflicted on you by 10%.
  - current:   Reduces the threat generated by your Holy spells by 20% and reduces the duration of Stun, Fear, and Silence effects inflicted on you by 10%.
- **Silent Resolve** rank 3
  - Wowhead: Reduces the threat generated by your spells by 30% and reduces the duration of Stun, Fear, and Silence effects inflicted on you by 15%.
  - current:   Reduces the threat generated by your Holy spells by 30% and reduces the duration of Stun, Fear, and Silence effects inflicted on you by 15%.
- **Spirit Tap** rank 1
  - Wowhead: Gives you a 20% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting.
  - current:   Gives you a 20% chance to gain a 100% bonus to your Spirit for 15 sec after killing a non-trivial target. For the duration, your Mana will regenerate at a 50% of normal rate while casting.
- **Spirit Tap** rank 2
  - Wowhead: Gives you a 40% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting.
  - current:   Gives you a 40% chance to gain a 100% bonus to your Spirit for 15 sec after killing a non-trivial target. For the duration, your Mana will regenerate at a 50% of normal rate while casting.
- **Spirit Tap** rank 3
  - Wowhead: Gives you a 60% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting.
  - current:   Gives you a 60% chance to gain a 100% bonus to your Spirit for 15 sec after killing a non-trivial target. For the duration, your Mana will regenerate at a 50% of normal rate while casting.
- **Spirit Tap** rank 4
  - Wowhead: Gives you a 80% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting.
  - current:   Gives you a 80% chance to gain a 100% bonus to your Spirit for 15 sec after killing a non-trivial target. For the duration, your Mana will regenerate at a 50% of normal rate while casting.
- **Spirit Tap** rank 5
  - Wowhead: Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting.
  - current:   Gives you a 100% chance to gain a 100% bonus to your Spirit for 15 sec after killing a non-trivial target. For the duration, your Mana will regenerate at a 50% of normal rate while casting.
- **Spiritual Guidance** rank 2
  - Wowhead: Increases your spell healing by up to 10% of your total Spirit and your spell damage by up to 3% of your total Spirit.
  - current:   Increases your spell healing by up to 10% of your total Spirit and your spell damage by up to 2% of your total Spirit.
- **Spiritual Guidance** rank 3
  - Wowhead: Increases your spell healing by up to 15% of your total Spirit and your spell damage by up to 5% of your total Spirit.
  - current:   Increases your spell healing by up to 15% of your total Spirit and your spell damage by up to 3% of your total Spirit.
- ... 9 more (see the JSON report)


## rogue

**New (Wowhead only)**

- `wh-105718` Blood Splatter - assassination r2c1
- `wh-105750` Boot Knife - subtlety r5c2
- `wh-105759` Composure - combat r2c3
- `wh-105708` Coup de Grace - combat r0c0
- `wh-110866` Death Mark - subtlety r6c1
- `wh-105741` Efficient Strikes - combat r0c1
- `wh-105740` Flash of Steel - combat r5c2
- `wh-108100` Flawless Execution - combat r3c1
- `wh-110867` Quick Getaway - subtlety r3c3

**Gone (current only)**

- `cutthroat` Cutthroat - subtlety r5c2
- `improved-distract` Improved Distract - subtlety r2c2
- `improved-eviscerate` Improved Eviscerate - combat r0c0
- `improved-sinister-strike` Improved Sinister Strike - combat r0c1
- `murder` Murder - assassination r1c1
- `quietus` Quietus - subtlety r5c0
- `restless-blades` Restless Blades - combat r3c1
- `thousand-cuts` Thousand Cuts - subtlety r6c1

**Position**

| talent | Wowhead | current |
|---|---|---|
| Aggression | `[3, 3]` | `[5, 2]` |
| Camouflage | `[1, 1]` | `[0, 0]` |
| Dirty Deeds | `[1, 0]` | `[4, 0]` |
| Dirty Tricks | `[1, 3]` | `[1, 2]` |
| Dual Wield Specialization | `[4, 0]` | `[3, 2]` |
| Elusiveness | `[3, 0]` | `[1, 1]` |
| Ghostly Strike | `[3, 1]` | `[2, 1]` |
| Heightened Senses | `[4, 0]` | `[3, 0]` |
| Improved Ambush | `[1, 2]` | `[1, 3]` |
| Improved Expose Armor | `[1, 1]` | `[2, 1]` |
| Improved Sprint | `[1, 3]` | `[2, 3]` |
| Mutilate | `[6, 1]` | `[4, 1]` |
| Premeditation | `[2, 1]` | `[3, 1]` |
| Relentless Strikes | `[4, 0]` | `[2, 0]` |
| Serrated Blades | `[2, 2]` | `[3, 2]` |
| Setup | `[0, 0]` | `[1, 0]` |
| Venom | `[4, 1]` | `[6, 1]` |
| Vigor | `[2, 0]` | `[4, 0]` |
| Weapon Expertise | `[3, 2]` | `[5, 1]` |

**maxRank**

| talent | Wowhead | current |
|---|---|---|
| Camouflage | `3` | `5` |
| Dual Wield Specialization | `2` | `5` |
| Lethality | `2` | `5` |
| Opportunity | `5` | `2` |
| Relentless Strikes | `5` | `1` |
| Seal Fate | `3` | `5` |

**Prerequisites**

| talent | Wowhead | current |
|---|---|---|
| Adrenaline Rush | `[('blade flurry', 1)]` | `[]` |
| Dual Wield Specialization | `[]` | `[('precision', 3)]` |
| Mutilate | `[('venom', 1)]` | `[]` |
| Venom | `[]` | `[('mutilate', 1)]` |
| Weapon Expertise | `[('precision', 3)]` | `[('blade flurry', 1)]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Elusiveness | `spell_magic_lesserinvisibilty` | `crop-elusiveness` |

**Rank text (41 differing rank(s))**

- **Aggression** rank 1
  - Wowhead: Increases the damage of your Sinister Strike and Eviscerate abilities by 5%.
  - current:   Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 2%.
- **Aggression** rank 2
  - Wowhead: Increases the damage of your Sinister Strike and Eviscerate abilities by 10%.
  - current:   Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 4%.
- **Aggression** rank 3
  - Wowhead: Increases the damage of your Sinister Strike and Eviscerate abilities by 15%.
  - current:   Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%.
- **Camouflage** rank 1
  - Wowhead: Reduces your speed penalty from your Stealth ability by 5% and reduces its cooldown by 2 sec.
  - current:   Reduces your speed penalty from your Stealth ability by 3% and reduces its cooldown by 2 sec.
- **Camouflage** rank 2
  - Wowhead: Reduces your speed penalty from your Stealth ability by 10% and reduces its cooldown by 4 sec.
  - current:   Reduces your speed penalty from your Stealth ability by 6% and reduces its cooldown by 4 sec.
- **Camouflage** rank 3
  - Wowhead: Reduces your speed penalty from your Stealth ability by 15% and reduces its cooldown by 6 sec.
  - current:   Reduces your speed penalty from your Stealth ability by 9% and reduces its cooldown by 6 sec.
- **Dual Wield Specialization** rank 1
  - Wowhead: Increases the damage done by your off-hand weapon by 25%.
  - current:   Increases the damage done by your off-hand weapon by 5%.
- **Dual Wield Specialization** rank 2
  - Wowhead: Increases the damage done by your off-hand weapon by 50%.
  - current:   Increases the damage done by your off-hand weapon by 10%.
- **Elusiveness** rank 2
  - Wowhead: Reduces the cooldown of your Vanish and Blind abilities by 90 sec.
  - current:   Reduces the cooldown of your Vanish and Blind abilities by 1.5 min.
- **Ghostly Strike** rank 1
  - Wowhead: A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage, increases your chance to dodge by 15% for 7 sec, and causes your next Ambush or Garrote cast within 7 sec to not require Stealth. Awards 1 combo point.
  - current:   A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point.
- **Hack and Slash** rank 2
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 2% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 2%. Mace: Your attacks ignore 6% of your target's armor.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 1%. Mace: Your attacks ignore 3% of your target's armor.
- **Hack and Slash** rank 3
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 3% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 3%. Mace: Your attacks ignore 9% of your target's armor.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 1%. Mace: Your attacks ignore 3% of your target's armor.
- **Hack and Slash** rank 4
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 4% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 4%. Mace: Your attacks ignore 12% of your target's armor.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 1%. Mace: Your attacks ignore 3% of your target's armor.
- **Hack and Slash** rank 5
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 5% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 5%. Mace: Your attacks ignore 15% of your target's armor.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target. Dagger/Fist: Increases your critical strike chance by 1%. Mace: Your attacks ignore 3% of your target's armor.
- **Heightened Senses** rank 1
  - Wowhead: Increases your Stealth detection as if you were 1 levels higher and reduces your chance to be hit by spells and ranged attacks by 2%.
  - current:   Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%.
- **Heightened Senses** rank 2
  - Wowhead: Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%.
  - current:   Increases your Stealth detection as if you were 2 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%.
- **Hemorrhage** rank 1
  - Wowhead: An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture and Garrote damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point.
  - current:   An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point.
- **Improved Expose Armor** rank 2
  - Wowhead: Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points.
  - current:   Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points.
- **Initiative** rank 2
  - Wowhead: Gives you a 67% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
  - current:   Gives you a 66% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
- **Initiative** rank 3
  - Wowhead: Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
  - current:   Gives you a 99% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
- **Lethality** rank 1
  - Wowhead: Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 10%.
  - current:   Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 6%.
- **Lethality** rank 2
  - Wowhead: Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%.
  - current:   Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%.
- **Master of Deception** rank 1
  - Wowhead: Reduces the chance enemies have to detect you while in Stealth mode as if you were 1 levels higher.
  - current:   Reduces the chance enemies have to detect you while in Stealth mode as if you were 1 level higher.
- **Mutilate** rank 1
  - Wowhead: Instantly attacks with both weapons for 90% weapon damage plus an additional 40 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points.
  - current:   Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points.
- **Opportunity** rank 1
  - Wowhead: Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 4%.
  - current:   Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 5%.
- **Opportunity** rank 2
  - Wowhead: Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%.
  - current:   Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%.
- **Precision** rank 1
  - Wowhead: Improves your chance to hit by 1%.
  - current:   Increases your chance to hit with all attacks and Poisons by 1%.
- **Precision** rank 2
  - Wowhead: Improves your chance to hit by 2%.
  - current:   Increases your chance to hit with all attacks and Poisons by 2%.
- **Precision** rank 3
  - Wowhead: Improves your chance to hit by 3%.
  - current:   Increases your chance to hit with all attacks and Poisons by 3%.
- **Puncturing Wounds** rank 2
  - Wowhead: Increases the critical strike chance of your Backstab by 20% and your Mutilate by 10%, and gives Backstab a 30% chance to add an additional Combo Point.
  - current:   Increases the critical strike chance of your Backstab by 10% and your Mutilate by 5%, and gives Backstab a 15% chance to add an additional Combo Point.
- **Puncturing Wounds** rank 3
  - Wowhead: Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point.
  - current:   Increases the critical strike chance of your Backstab by 10% and your Mutilate by 5%, and gives Backstab a 15% chance to add an additional Combo Point.
- **Relentless Strikes** rank 1
  - Wowhead: Your finishing moves have a 4% chance per Combo Point to restore 25 Energy.
  - current:   Your finishing moves have a 20% chance per Combo Point to restore 25 Energy.
- **Seal Fate** rank 1
  - Wowhead: Your critical strikes from abilities that add Combo Points have a 33% chance to add an additional Combo Point.
  - current:   Your critical strikes from abilities that add Combo Points have a 20% chance to add an additional Combo Point.
- **Seal Fate** rank 2
  - Wowhead: Your critical strikes from abilities that add Combo Points have a 66% chance to add an additional Combo Point.
  - current:   Your critical strikes from abilities that add Combo Points have a 40% chance to add an additional Combo Point.
- **Seal Fate** rank 3
  - Wowhead: Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point.
  - current:   Your critical strikes from abilities that add Combo Points have a 60% chance to add an additional Combo Point.
- **Serrated Blades** rank 2
  - Wowhead: Causes your attacks to ignore 6% of your target's Armor and increases the damage dealt by your Rupture ability by 20%.
  - current:   Causes your attacks to ignore 3% of your target's Armor and increases the damage dealt by your Rupture ability by 20%.
- **Serrated Blades** rank 3
  - Wowhead: Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%.
  - current:   Causes your attacks to ignore 3% of your target's Armor and increases the damage dealt by your Rupture ability by 30%.
- **Setup** rank 1
  - Wowhead: Gives you a 15% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells.
  - current:   Gives you a 33% chance to add a Combo Point to your target after Dodging an attack or fully resisting a spell.
- **Setup** rank 2
  - Wowhead: Gives you a 30% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells.
  - current:   Gives you a 66% chance to add a Combo Point to your target after Dodging an attack or fully resisting a spell.
- **Setup** rank 3
  - Wowhead: Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells.
  - current:   Gives you a 99% chance to add a Combo Point to your target after Dodging an attack or fully resisting a spell.
- **Venom** rank 1
  - Wowhead: Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 sec.
  - current:   Finishing move that increases the damage of your Poisons by 30% and your chance to apply Poisons by 10%. Lasts longer per combo point: 1 point: 9 seconds 2 points: 12 seconds 3 points: 15 seconds 4 points: 18 seconds 5 points: 21 seconds


## shaman

**New (Wowhead only)**

- `wh-104758` Lightning Mastery - elemental-combat r6c1
- `wh-104764` Trial by Fire - elemental-combat r3c0

**Gone (current only)**

- `improved-fire-nova` Improved Fire Nova - elemental-combat r3c0
- `lava-burst` Lava Burst - elemental-combat r6c1

**Position**

| talent | Wowhead | current |
|---|---|---|
| Call of Flame | `[1, 3]` | `[1, 2]` |
| Call of Thunder | `[4, 1]` | `[3, 2]` |
| Earthbound | `[3, 3]` | `[4, 3]` |
| Elemental Alacrity | `[1, 2]` | `[5, 2]` |
| Elemental Devastation | `[1, 0]` | `[1, 3]` |
| Elemental Focus | `[2, 0]` | `[2, 1]` |
| Elemental Fury | `[5, 2]` | `[2, 2]` |
| Elemental Warding | `[2, 1]` | `[1, 0]` |
| Improved Ghost Wolf | `[3, 3]` | `[1, 2]` |
| Improved Lightning Shield | `[1, 2]` | `[1, 3]` |
| Lightning Overload | `[4, 2]` | `[4, 1]` |
| Tidal Focus | `[0, 2]` | `[1, 2]` |
| Tidal Mastery | `[3, 0]` | `[0, 2]` |
| Totemic Focus | `[1, 2]` | `[3, 0]` |

**Prerequisites**

| talent | Wowhead | current |
|---|---|---|
| Call of Thunder | `[]` | `[('elemental fury', 5)]` |
| Elemental Alacrity | `[]` | `[('call of thunder', 1)]` |
| Elemental Fury | `[('lightning overload', 3)]` | `[]` |
| Lightning Overload | `[('elemental alacrity', 3)]` | `[]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Anticipation | `spell_nature_mirrorimage` | `crop-anticipation` |
| Concussion | `spell_nature_earthshock` | `crop-concussion` |
| Convection | `spell_nature_wispsplode` | `crop-convection` |
| Elemental Alacrity | `spell_lightning_lightningbolt01` | `crop-elemental-alacrity` |
| Elemental Devastation | `spell_fire_elementaldevastation` | `crop-elemental-devastation` |
| Elemental Reach | `spell_nature_stormreach` | `crop-elemental-reach` |
| Guardian Totems | `spell_nature_stoneskintotem` | `crop-guardian-totems` |
| Improved Healing Wave | `spell_nature_magicimmunity` | `crop-improved-healing-wave` |
| Improved Lightning Shield | `spell_nature_lightningshield` | `crop-improved-lightning-shield` |
| Riptide | `spell_nature_riptide` | `crop-riptide` |

**Rank text (60 differing rank(s))**

- **Ancestral Healing** rank 2
  - Wowhead: Increases your target's armor value by 17% for 15 sec after getting a critical effect from one of your healing spells.
  - current:   Increases your target's armor value by 16% for 15 sec after getting a critical effect from one of your healing spells.
- **Call of Flame** rank 1
  - Wowhead: Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 5%, as well as increases the duration of your Flame Shock spell by 3 sec.
  - current:   Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 5%.
- **Call of Flame** rank 2
  - Wowhead: Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 10%, as well as increases the duration of your Flame Shock spell by 6 sec.
  - current:   Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 10%.
- **Call of Flame** rank 3
  - Wowhead: Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec.
  - current:   Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%.
- **Call of Thunder** rank 1
  - Wowhead: Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 5%.
  - current:   Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 3%.
- **Convection** rank 1
  - Wowhead: Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 2%.
  - current:   Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 2%.
- **Convection** rank 2
  - Wowhead: Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 4%.
  - current:   Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 4%.
- **Convection** rank 3
  - Wowhead: Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 6%.
  - current:   Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 6%.
- **Convection** rank 4
  - Wowhead: Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 8%.
  - current:   Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 8%.
- **Convection** rank 5
  - Wowhead: Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 10%.
  - current:   Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%.
- **Elemental Alacrity** rank 1
  - Wowhead: Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.17 sec.
  - current:   Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.17 sec.
- **Elemental Alacrity** rank 2
  - Wowhead: Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.33 sec.
  - current:   Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.17 sec.
- **Elemental Alacrity** rank 3
  - Wowhead: Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.50 sec.
  - current:   Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.17 sec.
- **Elemental Devastation** rank 1
  - Wowhead: Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3% for 10 sec.
  - current:   Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 3% for 10 sec.
- **Elemental Devastation** rank 2
  - Wowhead: Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 6% for 10 sec.
  - current:   Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 6% for 10 sec.
- **Elemental Devastation** rank 3
  - Wowhead: Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 9% for 10 sec.
  - current:   Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 9% for 10 sec.
- **Elemental Reach** rank 1
  - Wowhead: Increases the range of your Lightning Bolt, Chain Lightning, and Fire Nova spells by 3 yards.
  - current:   Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards, and increases the range of your Flame Shock spell by 8 yards.
- **Elemental Reach** rank 2
  - Wowhead: Increases the range of your Lightning Bolt, Chain Lightning, and Fire Nova spells by 6 yards.
  - current:   Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 6 yards, and increases the range of your Flame Shock spell by 16 yards.
- **Elemental Warding** rank 2
  - Wowhead: Reduces damage taken from Fire, Frost, and Nature effects by 7%.
  - current:   Reduces damage taken from Fire, Frost, and Nature effects by 6%.
- **Elemental Warding** rank 3
  - Wowhead: Reduces damage taken from Fire, Frost, and Nature effects by 10%.
  - current:   Reduces damage taken from Fire, Frost, and Nature effects by 9%.
- **Elemental Weapons** rank 2
  - Wowhead: Increases the melee attack power bonus of your Rockbiter Weapon by 13%, your Windfury Weapon effect by 27% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 10%.
  - current:   Increases the melee attack power bonus of your Rockbiter Weapon by 14%, your Windfury Weapon effect by 27% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 10%.
- **Eye of the Storm** rank 1
  - Wowhead: Gives your Lightning Bolt and Chain Lightning spells a 23% chance to not lose casting time when you take damage.
  - current:   Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 23%.
- **Eye of the Storm** rank 2
  - Wowhead: Gives your Lightning Bolt and Chain Lightning spells a 47% chance to not lose casting time when you take damage.
  - current:   Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 46%.
- **Eye of the Storm** rank 3
  - Wowhead: Gives your Lightning Bolt and Chain Lightning spells a 70% chance to not lose casting time when you take damage.
  - current:   Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 69%.
- **Flurry** rank 1
  - Wowhead: Increases your attack speed by 6% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your attack speed by 5% for your next 3 swings after dealing a melee critical strike.
- **Flurry** rank 2
  - Wowhead: Increases your attack speed by 12% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your attack speed by 10% for your next 3 swings after dealing a melee critical strike.
- **Flurry** rank 3
  - Wowhead: Increases your attack speed by 18% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your attack speed by 15% for your next 3 swings after dealing a melee critical strike.
- **Flurry** rank 4
  - Wowhead: Increases your attack speed by 24% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your attack speed by 20% for your next 3 swings after dealing a melee critical strike.
- **Flurry** rank 5
  - Wowhead: Increases your attack speed by 30% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike.
- **Healing Focus** rank 1
  - Wowhead: Gives your healing spells a 23% chance to not lose casting time when you take damage.
  - current:   Gives you a 23% chance to avoid interruption caused by damage while casting any healing spell.
- **Healing Focus** rank 2
  - Wowhead: Gives your healing spells a 47% chance to not lose casting time when you take damage.
  - current:   Gives you a 46% chance to avoid interruption caused by damage while casting any healing spell.
- **Healing Focus** rank 3
  - Wowhead: Gives your healing spells a 70% chance to not lose casting time when you take damage.
  - current:   Gives you a 69% chance to avoid interruption caused by damage while casting any healing spell.
- **Healing Way** rank 2
  - Wowhead: Increases the amount healed by your Healing Wave spell by 17%.
  - current:   Increases the amount healed by your Healing Wave spell by 16%.
- **Healing Way** rank 3
  - Wowhead: Increases the amount healed by your Healing Wave spell by 25%.
  - current:   Increases the amount healed by your Healing Wave spell by 24%.
- **Improved Ghost Wolf** rank 2
  - Wowhead: Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors.
  - current:   Reduces the cast time of your Ghost Wolf spell by 2 sec, and Ghost Wolf may be used indoors.
- **Improved Reincarnation** rank 2
  - Wowhead: Reduces the cooldown of your Reincarnation spell by 20 min, increases your maximum health by 4%, and increases the amount of health and Mana you reincarnate with by an additional 20%.
  - current:   Reduces the cooldown of your Reincarnation spell by 10 min, increases your maximum health by 2%, and increases the amount of health and Mana you reincarnate with by an additional 10%.
- **Improved Stormstrike** rank 2
  - Wowhead: When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry.
  - current:   When you Stormstrike, you have a 50% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 50% chance to reset each time you Dodge or Parry.
- **Lightning Overload** rank 1
  - Wowhead: Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.
  - current:   Gives your Lightning Bolt and Chain Lightning spells a 3% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.
- **Lightning Overload** rank 2
  - Wowhead: Gives your Lightning Bolt and Chain Lightning spells a 20% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.
  - current:   Gives your Lightning Bolt and Chain Lightning spells a 6% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.
- **Lightning Overload** rank 3
  - Wowhead: Gives your Lightning Bolt and Chain Lightning spells a 30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.
  - current:   Gives your Lightning Bolt and Chain Lightning spells a 9% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat.
- **Maelstrom Weapon** rank 2
  - Wowhead: When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 8%. Stacks up to 5 times. Lasts 30 sec.
  - current:   When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec.
- **Maelstrom Weapon** rank 3
  - Wowhead: When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 12%. Stacks up to 5 times. Lasts 30 sec.
  - current:   When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec.
- **Maelstrom Weapon** rank 4
  - Wowhead: When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 16%. Stacks up to 5 times. Lasts 30 sec.
  - current:   When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec.
- **Maelstrom Weapon** rank 5
  - Wowhead: When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec.
  - current:   When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec.
- **Mental Dexterity** rank 1
  - Wowhead: Increases your Attack Power by an amount equal to 50% of your Intellect.
  - current:   Increases your Attack Power by an amount equal to 33% of your Intellect.
- **Mental Dexterity** rank 2
  - Wowhead: Increases your Attack Power by an amount equal to 100% of your Intellect.
  - current:   Increases your Attack Power by an amount equal to 66% of your Intellect.
- **Mental Dexterity** rank 3
  - Wowhead: Increases your Attack Power by an amount equal to 150% of your Intellect.
  - current:   Increases your Attack Power by an amount equal to 99% of your Intellect.
- **Mindfulness** rank 2
  - Wowhead: Allows 33% of your Mana regeneration to continue while casting.
  - current:   Allows 34% of your Mana regeneration to continue while casting.
- **Mindfulness** rank 3
  - Wowhead: Allows 50% of your Mana regeneration to continue while casting.
  - current:   Allows 51% of your Mana regeneration to continue while casting.
- **Nature's Swiftness** rank 1
  - Wowhead: When activated, your next Nature spell with a casting time less than 10 sec. becomes an instant cast spell.
  - current:   When activated, your next Nature spell with a casting time less than 10 sec becomes an instant cast spell.
- **Rage of the Farseer** rank 1
  - Wowhead: Increases your attack speed by 30% for 25 sec.
  - current:   Increases your melee attack speed and spell casting speed by 30% for 25 sec.
- **Reverberation** rank 5
  - Wowhead: Reduces the cooldown of your Shock spells by 1.0 sec.
  - current:   Reduces the cooldown of your Shock spells by 1 sec.
- **Riptide** rank 1
  - Wowhead: Heals a friendly target for 445 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%.
  - current:   Heals a friendly target for 479 to 528, an additional 499 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%.
- **Stormstrike** rank 1
  - Wowhead: Instantly strike for 150% weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec.
  - current:   Instantly strike for normal weapon damage and increase Nature damage you deal to the target by 20% for 12 sec.
- **Tidal Focus** rank 1
  - Wowhead: Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%.
  - current:   Reduces the Mana cost of your healing spells by 1% and increases your chance to hit with all spells and attacks by 1%.
- **Tidal Focus** rank 2
  - Wowhead: Reduces the Mana cost of your healing spells by 2% and improves your chance to hit by 2%.
  - current:   Reduces the Mana cost of your healing spells by 2% and increases your chance to hit with all spells and attacks by 2%.
- **Tidal Focus** rank 3
  - Wowhead: Reduces the Mana cost of your healing spells by 3% and improves your chance to hit by 3%.
  - current:   Reduces the Mana cost of your healing spells by 3% and increases your chance to hit with all spells and attacks by 3%.
- **Tidal Focus** rank 4
  - Wowhead: Reduces the Mana cost of your healing spells by 4% and improves your chance to hit by 4%.
  - current:   Reduces the Mana cost of your healing spells by 4% and increases your chance to hit with all spells and attacks by 4%.
- **Tidal Focus** rank 5
  - Wowhead: Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%.
  - current:   Reduces the Mana cost of your healing spells by 5% and increases your chance to hit with all spells and attacks by 5%.
- **Water Shield** rank 1
  - Wowhead: The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min. Only one Elemental Shield can be active on the Shaman at any one time.
  - current:   The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's healing spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min. Only one Elemental Shield can be active on the Shaman at any one time.


## warlock

**New (Wowhead only)**

- `wh-105923` Grim Reach - curses r1c0
- `wh-105922` Soul Harvest - curses r1c1
- `wh-105909` Wrack - curses r6c1

**Gone (current only)**

- `drain-hope` Drain Hope - affliction r6c1
- `malediction` Malediction - affliction r1c0
- `soul-harvesting` Soul Harvesting - affliction r1c1

**Tree moved**

| talent | Wowhead | current |
|---|---|---|
| Amplify Curse | `curses` | `affliction` |
| Curse of Exhaustion | `curses` | `affliction` |
| Decimation | `summoning` | `demonology` |
| Demonic Aegis | `summoning` | `demonology` |
| Demonic Brand | `summoning` | `demonology` |
| Demonic Embrace | `summoning` | `demonology` |
| Demonic Energies | `summoning` | `demonology` |
| Demonic Knowledge | `summoning` | `demonology` |
| Demonic Pact | `summoning` | `demonology` |
| Demonic Sacrifice | `summoning` | `demonology` |
| Fel Concentration | `curses` | `affliction` |
| Fel Domination | `summoning` | `demonology` |
| Fel Vitality | `summoning` | `demonology` |
| Improved Bane of Agony | `curses` | `affliction` |
| Improved Corruption | `curses` | `affliction` |
| Improved Drains | `curses` | `affliction` |
| Improved Felhunter | `summoning` | `demonology` |
| Improved Health Funnel | `summoning` | `demonology` |
| Improved Imp | `summoning` | `demonology` |
| Improved Life Tap | `curses` | `affliction` |
| Improved Sayaad | `summoning` | `demonology` |
| Improved Voidwalker | `summoning` | `demonology` |
| Malevolence | `curses` | `affliction` |
| Master Demonologist | `summoning` | `demonology` |
| Master Summoner | `summoning` | `demonology` |
| Nightfall | `curses` | `affliction` |
| Pandemic | `curses` | `affliction` |
| Shadow Mastery | `curses` | `affliction` |
| Siphon Life | `curses` | `affliction` |
| Soul Link | `summoning` | `demonology` |
| Soul Siphon | `curses` | `affliction` |
| Suppression | `curses` | `affliction` |
| Unholy Power | `summoning` | `demonology` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Decimation | `spell_fire_fireball02` | `crop-decimation` |
| Demonic Aegis | `spell_shadow_ragingscream` | `crop-demonic-aegis` |
| Demonic Brand | `ability_demonhunter_chaoticimprint_fire` | `crop-demonic-brand` |
| Demonic Energies | `spell_shadow_felmending` | `crop-demonic-energies` |
| Demonic Pact | `inv_ability_soulharvesterwarlock_demonicsoul` | `crop-demonic-pact` |
| Improved Sayaad | `ability_warlock_randomizesuccubusincubus` | `crop-improved-sayaad` |
| Pandemic | `spell_shadow_unstableaffliction_2` | `spell_shadow_unstableaffliction_1` |
| Unholy Power | `spell_shadow_shadowworddominate` | `crop-unholy-power` |

**Rank text (68 differing rank(s))**

- **Aftermath** rank 2
  - Wowhead: Increases the initial damage of your Immolate spell by 20% and your Conflagrate spell has a 40% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
  - current:   Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
- **Aftermath** rank 3
  - Wowhead: Increases the initial damage of your Immolate spell by 30% and your Conflagrate spell has a 60% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
  - current:   Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
- **Aftermath** rank 4
  - Wowhead: Increases the initial damage of your Immolate spell by 40% and your Conflagrate spell has a 80% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
  - current:   Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
- **Aftermath** rank 5
  - Wowhead: Increases the initial damage of your Immolate spell by 50% and your Conflagrate spell has a 100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
  - current:   Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
- **Agonizing Flames** rank 2
  - Wowhead: Increases the critical strike chance of your Searing Pain spell by 7% and the damage done by all your Destruction spells by 7%.
  - current:   Increases the critical strike chance of your Searing Pain spell by 6% and the damage done by all your Destruction spells by 6%.
- **Agonizing Flames** rank 3
  - Wowhead: Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%.
  - current:   Increases the critical strike chance of your Searing Pain spell by 9% and the damage done by all your Destruction spells by 9%.
- **Cataclysm** rank 3
  - Wowhead: Reduces the Mana cost of your Destruction spells by 10%.
  - current:   Reduces the Mana cost of your Destruction spells by 9%.
- **Conflagrate** rank 1
  - Wowhead: Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 111 Fire damage and consuming your Immolate effect.
  - current:   Ignites a target that is already afflicted by your Immolate spell, dealing 109 to 132 Fire damage and consuming your Immolate effect.
- **Decimation** rank 2
  - Wowhead: Reduces the cooldown of your Soul Fire spell by 90%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 6% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 40% and costs no Soul Shards.
  - current:   Reduces the cooldown of your Soul Fire spell by 45%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 3% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 20% and costs no Soul Shards.
- **Demonic Brand** rank 1
  - Wowhead: Your Searing Pain generates 17% less threat and brands the target for 10 sec. Your pet's next 2 attacks against the target deal ((((60 - 26) * 1.5) + 14 + (0.078 * ((Shadow spell power)))) * (1 * 1 * 1)) to ((((60 - 26) * 1.5) + 17 + (0.078 * ((Shadow spell power)))) * (1 * 1 * 1)) Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat.
  - current:   Your Searing Pain generates 17% less threat and brands the target for 10 sec. Your pet's next 2 attacks against the target generate high threat and deal 39 to 42 Fire or Shadow damage based on the pet.
- **Demonic Brand** rank 2
  - Wowhead: Your Searing Pain generates 33% less threat and brands the target for 10 sec. Your pet's next 4 attacks against the target deal ((((60 - 26) * 1.5) + 14 + (0.078 * ((Shadow spell power)))) * (1 * 1 * 1)) to ((((60 - 26) * 1.5) + 17 + (0.078 * ((Shadow spell power)))) * (1 * 1 * 1)) Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat.
  - current:   Your Searing Pain generates 17% less threat and brands the target for 10 sec. Your pet's next 2 attacks against the target generate high threat and deal 39 to 42 Fire or Shadow damage based on the pet.
- **Demonic Brand** rank 3
  - Wowhead: Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target deal ((((60 - 26) * 1.5) + 14 + (0.078 * ((Shadow spell power)))) * (1 * 1 * 1)) to ((((60 - 26) * 1.5) + 17 + (0.078 * ((Shadow spell power)))) * (1 * 1 * 1)) Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat.
  - current:   Your Searing Pain generates 17% less threat and brands the target for 10 sec. Your pet's next 2 attacks against the target generate high threat and deal 39 to 42 Fire or Shadow damage based on the pet.
- **Demonic Energies** rank 2
  - Wowhead: You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain.
  - current:   You heal your pet for 16% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain.
- **Demonic Knowledge** rank 1
  - Wowhead: Increases your spell damage and your Demon pet's spell damage by up to 33% of your level while you have a summoned Demon pet active.
  - current:   Increases your spell damage and healing by up to 33% of your level while you have a summoned Demon pet active.
- **Demonic Knowledge** rank 2
  - Wowhead: Increases your spell damage and your Demon pet's spell damage by up to 67% of your level while you have a summoned Demon pet active.
  - current:   Increases your spell damage and healing by up to 66% of your level while you have a summoned Demon pet active.
- **Demonic Knowledge** rank 3
  - Wowhead: Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active.
  - current:   Increases your spell damage and healing by up to 99% of your level while you have a summoned Demon pet active.
- **Destructive Reach** rank 1
  - Wowhead: Increases the range of your Destruction spells by 10%.
  - current:   Increases the range of your damaging spells by 10%.
- **Destructive Reach** rank 2
  - Wowhead: Increases the range of your Destruction spells by 20%.
  - current:   Increases the range of your damaging spells by 20%.
- **Fel Concentration** rank 1
  - Wowhead: Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 23% chance to not lose casting time when you take damage.
  - current:   Gives you a 23% chance to avoid interruption caused by damage while channeling or casting your Drain Life, Drain Mana, or Drain Soul spells.
- **Fel Concentration** rank 2
  - Wowhead: Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 47% chance to not lose casting time when you take damage.
  - current:   Gives you a 46% chance to avoid interruption caused by damage while channeling or casting your Drain Life, Drain Mana, or Drain Soul spells.
- **Fel Concentration** rank 3
  - Wowhead: Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 70% chance to not lose casting time when you take damage.
  - current:   Gives you a 69% chance to avoid interruption caused by damage while channeling or casting your Drain Life, Drain Mana, or Drain Soul spells.
- **Fel Domination** rank 1
  - Wowhead: Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 6 sec and its Mana cost reduced by 50%.
  - current:   Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%.
- **Fire and Brimstone** rank 2
  - Wowhead: Increases the critical strike chance of your Conflagrate spell by 17%.
  - current:   Increases the critical strike chance of your Conflagrate spell by 16%.
- **Fire and Brimstone** rank 3
  - Wowhead: Increases the critical strike chance of your Conflagrate spell by 25%.
  - current:   Increases the critical strike chance of your Conflagrate spell by 24%.
- **Improved Corruption** rank 2
  - Wowhead: Reduces the casting time of your Corruption spell by 0.8 sec and increases the damage it deals by 4%.
  - current:   Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%.
- **Improved Corruption** rank 3
  - Wowhead: Reduces the casting time of your Corruption spell by 1.2 sec and increases the damage it deals by 6%.
  - current:   Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%.
- **Improved Corruption** rank 4
  - Wowhead: Reduces the casting time of your Corruption spell by 1.6 sec and increases the damage it deals by 8%.
  - current:   Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%.
- **Improved Corruption** rank 5
  - Wowhead: Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%.
  - current:   Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%.
- **Improved Drains** rank 1
  - Wowhead: Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 7%.
  - current:   Increases the damage done or health drained by your Drain Life and Drain Soul spells by 2% per each of your other Affliction effects active on the target, up to a maximum increase of 6%. When your Drain Soul damages targets below 20% health, this bonus is tripled. Additionally, your Drain Life range is extended by 3 yards.
- **Improved Drains** rank 2
  - Wowhead: Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 13%.
  - current:   Increases the damage done or health drained by your Drain Life and Drain Soul spells by 2% per each of your other Affliction effects active on the target, up to a maximum increase of 6%. When your Drain Soul damages targets below 20% health, this bonus is tripled. Additionally, your Drain Life range is extended by 3 yards.
- **Improved Drains** rank 3
  - Wowhead: Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 20%.
  - current:   Increases the damage done or health drained by your Drain Life and Drain Soul spells by 2% per each of your other Affliction effects active on the target, up to a maximum increase of 6%. When your Drain Soul damages targets below 20% health, this bonus is tripled. Additionally, your Drain Life range is extended by 3 yards.
- **Improved Felhunter** rank 2
  - Wowhead: Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 20%, and reduces the cooldown of its Spell Lock by 4 sec.
  - current:   Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 10%, and reduces the cooldown of its Spell Lock by 2 sec.
- **Improved Felhunter** rank 3
  - Wowhead: Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 30%, and reduces the cooldown of its Spell Lock by 6 sec.
  - current:   Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 10%, and reduces the cooldown of its Spell Lock by 2 sec.
- **Improved Health Funnel** rank 2
  - Wowhead: Increases the amount of health transferred by your Health Funnel spell by 40%, reduces its health cost by 30%, and reduces all threat your Health Funnel generates by 100%. Allows Health Funnel to be used regardless of your demon's health.
  - current:   Increases the amount of health transferred by your Health Funnel spell by 20%, reduces its health cost by 15%, and reduces all threat your Health Funnel generates by 50%. Allows Health Funnel to be used regardless of your demon's health.
- **Improved Shadow Bolt** rank 2
  - Wowhead: Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 8% for 12 sec.
  - current:   Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec.
- **Improved Shadow Bolt** rank 3
  - Wowhead: Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 12% for 12 sec.
  - current:   Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec.
- **Improved Shadow Bolt** rank 4
  - Wowhead: Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 16% for 12 sec.
  - current:   Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec.
- **Improved Shadow Bolt** rank 5
  - Wowhead: Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec.
  - current:   Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec.
- **Incinerate** rank 1
  - Wowhead: Deals 100 to 114 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate.
  - current:   Deals 125 to 140 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate.
- **Intensity** rank 1
  - Wowhead: Gives your Destruction spells a 23% chance to not lose casting time when you take damage.
  - current:   Gives you a 23% chance to resist interruption caused by damage while casting or channeling any Destruction spell.
- **Intensity** rank 2
  - Wowhead: Gives your Destruction spells a 47% chance to not lose casting time when you take damage.
  - current:   Gives you a 46% chance to resist interruption caused by damage while casting or channeling any Destruction spell.
- **Intensity** rank 3
  - Wowhead: Gives your Destruction spells a 70% chance to not lose casting time when you take damage.
  - current:   Gives you a 69% chance to resist interruption caused by damage while casting or channeling any Destruction spell.
- **Nightfall** rank 1
  - Wowhead: Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 2% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%.
  - current:   Gives your Corruption, Drain Soul, and Drain Life spells a 2% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%.
- **Nightfall** rank 2
  - Wowhead: Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%.
  - current:   Gives your Corruption, Drain Soul, and Drain Life spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%.
- **Pandemic** rank 1
  - Wowhead: Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 33%.
  - current:   Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Drain Hope spells by 33%.
- **Pandemic** rank 2
  - Wowhead: Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 67%.
  - current:   Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Drain Hope spells by 66%.
- **Pandemic** rank 3
  - Wowhead: Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%.
  - current:   Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Drain Hope spells by 99%.
- **Pyroclasm** rank 2
  - Wowhead: Gives your Soul Fire spell a 26% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 26% chance over their duration to Stun targets they damage for 3 sec.
  - current:   Gives your Soul Fire spell a 13% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13% chance over their duration to Stun targets they damage for 3 sec.
- **Shadow and Flame** rank 1
  - Wowhead: Hitting an enemy with Conflagrate increases all Shadow damage you deal by 4% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 4% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.
  - current:   Hitting an enemy with Conflagrate increases all Shadow damage you deal by 2% for 20 sec. and hitting an enemy with Shadowburn increases all Fire damage you deal by 2% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.
- **Shadow and Flame** rank 2
  - Wowhead: Hitting an enemy with Conflagrate increases all Shadow damage you deal by 8% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 8% for 20 sec. In addition, Conflagrate has a 40% chance not to consume Immolate, and Shadowburn has a 40% chance to instantly refund a Soul Shard.
  - current:   Hitting an enemy with Conflagrate increases all Shadow damage you deal by 2% for 20 sec. and hitting an enemy with Shadowburn increases all Fire damage you deal by 2% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.
- **Shadow and Flame** rank 3
  - Wowhead: Hitting an enemy with Conflagrate increases all Shadow damage you deal by 12% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 12% for 20 sec. In addition, Conflagrate has a 60% chance not to consume Immolate, and Shadowburn has a 60% chance to instantly refund a Soul Shard.
  - current:   Hitting an enemy with Conflagrate increases all Shadow damage you deal by 2% for 20 sec. and hitting an enemy with Shadowburn increases all Fire damage you deal by 2% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.
- **Shadow and Flame** rank 4
  - Wowhead: Hitting an enemy with Conflagrate increases all Shadow damage you deal by 16% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 16% for 20 sec. In addition, Conflagrate has a 80% chance not to consume Immolate, and Shadowburn has a 80% chance to instantly refund a Soul Shard.
  - current:   Hitting an enemy with Conflagrate increases all Shadow damage you deal by 2% for 20 sec. and hitting an enemy with Shadowburn increases all Fire damage you deal by 2% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.
- **Shadow and Flame** rank 5
  - Wowhead: Hitting an enemy with Conflagrate increases all Shadow damage you deal by 20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 20% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard.
  - current:   Hitting an enemy with Conflagrate increases all Shadow damage you deal by 2% for 20 sec. and hitting an enemy with Shadowburn increases all Fire damage you deal by 2% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard.
- **Shadow Mastery** rank 1
  - Wowhead: Increases the damage dealt or life drained by your Shadow spells by 2%.
  - current:   Increases the damage dealt or life drained by your Shadow spells by 1%.
- **Shadow Mastery** rank 2
  - Wowhead: Increases the damage dealt or life drained by your Shadow spells by 4%.
  - current:   Increases the damage dealt or life drained by your Shadow spells by 2%.
- **Shadow Mastery** rank 3
  - Wowhead: Increases the damage dealt or life drained by your Shadow spells by 6%.
  - current:   Increases the damage dealt or life drained by your Shadow spells by 3%.
- **Shadow Mastery** rank 4
  - Wowhead: Increases the damage dealt or life drained by your Shadow spells by 8%.
  - current:   Increases the damage dealt or life drained by your Shadow spells by 4%.
- **Shadow Mastery** rank 5
  - Wowhead: Increases the damage dealt or life drained by your Shadow spells by 10%.
  - current:   Increases the damage dealt or life drained by your Shadow spells by 5%.
- **Shadowburn** rank 1
  - Wowhead: Instantly blasts the target for 65 to 74 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard.
  - current:   Instantly blasts the target for 102 to 111 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard.
- **Siphon Life** rank 1
  - Wowhead: Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec.
  - current:   Transfers 15 health from the target to the caster every 3 sec. Lasts 30 sec.
- ... 8 more (see the JSON report)


## warrior

**New (Wowhead only)**

- `wh-105934` Blood Craze - fury r2c2
- `wh-105953` Furious Precision - fury r2c0
- `wh-113569` Gore Drinker - fury r4c2
- `wh-105977` Improved Whirlwind - fury r5c0
- `wh-110857` Lingering Rage - fury r1c1
- `wh-113636` Reckless Swings - fury r3c1

**Gone (current only)**

- `blood-crazed` Blood Crazed - fury r2c2
- `boundless-rage` Boundless Rage - fury r2c3
- `improved-cleave` Improved Cleave - fury r2c0
- `precision` Precision - fury r4c0
- `raging-blows` Raging Blows - fury r3c1
- `toughness` Toughness - protection r1c2
- `vitality` Vitality - protection r4c3

**Tree moved**

| talent | Wowhead | current |
|---|---|---|
| Iron Will | `protection` | `fury` |

**Position**

| talent | Wowhead | current |
|---|---|---|
| Anticipation | `[1, 0]` | `[0, 2]` |
| Enrage | `[2, 3]` | `[3, 2]` |
| Focused Rage | `[4, 2]` | `[5, 0]` |
| Improved Berserker Rage | `[4, 0]` | `[5, 0]` |
| Improved Bloodrage | `[0, 0]` | `[1, 0]` |
| Improved Disarm | `[2, 2]` | `[3, 1]` |
| Improved Revenge | `[1, 2]` | `[2, 2]` |
| Improved Shield Bash | `[3, 2]` | `[4, 2]` |
| Iron Will | `[0, 2]` | `[1, 1]` |
| Vanguard | `[3, 1]` | `[3, 2]` |

**maxRank**

| talent | Wowhead | current |
|---|---|---|
| Bloodthrill | `2` | `5` |
| Flurry | `3` | `5` |
| Improved Tactical Mastery | `3` | `5` |

**Prerequisites**

| talent | Wowhead | current |
|---|---|---|
| Anger Management | `[('improved tactical mastery', 3)]` | `[('improved tactical mastery', 5)]` |
| Flurry | `[]` | `[('enrage', 5)]` |
| Impale | `[('deep wounds', 3)]` | `[]` |
| Last Stand | `[]` | `[('improved bloodrage', 2)]` |

**Icons**

| talent | Wowhead | current |
|---|---|---|
| Booming Voice | `spell_nature_purge` | `crop-booming-voice` |
| Improved Charge | `ability_warrior_charge` | `crop-improved-charge` |
| Improved Tactical Mastery | `spell_nature_enchantarmor` | `crop-improved-tactical-mastery` |
| Vanguard | `ability_warrior_shieldcharge` | `crop-vanguard` |
| Weaponmaster | `garrison_weaponupgrade` | `crop-weaponmaster` |

**Rank text (54 differing rank(s))**

- **Bloodthirst** rank 1
  - Wowhead: Instantly attack the target causing damage equal to 45% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec.
  - current:   Instantly attack the target causing damage equal to 35% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec.
- **Bloodthrill** rank 1
  - Wowhead: Grants your Main Hand melee attacks against enemies afflicted by your Rend a 10% chance to allow an activation of Overpower.
  - current:   Your melee attacks against targets afflicted by your Rend have a 2% chance to activate your Overpower ability for 1 attack on your current target. Lasts 6 sec.
- **Bloodthrill** rank 2
  - Wowhead: Grants your Main Hand melee attacks against enemies afflicted by your Rend a 20% chance to allow an activation of Overpower.
  - current:   Your melee attacks against targets afflicted by your Rend have a 2% chance to activate your Overpower ability for 1 attack on your current target. Lasts 6 sec.
- **Booming Voice** rank 1
  - Wowhead: Increases the area of effect of your Shouts by 10% and reduces the Rage cost by of your Shouts and Howls by 5%.
  - current:   Increases the radius of your Battle Shout and Demoralizing Shout abilities by 10%.
- **Booming Voice** rank 2
  - Wowhead: Increases the area of effect of your Shouts by 20% and reduces the Rage cost by of your Shouts and Howls by 10%.
  - current:   Increases the radius of your Battle Shout and Demoralizing Shout abilities by 20%.
- **Booming Voice** rank 3
  - Wowhead: Increases the area of effect of your Shouts by 30% and reduces the Rage cost by of your Shouts and Howls by 15%.
  - current:   Increases the radius of your Battle Shout and Demoralizing Shout abilities by 30%.
- **Booming Voice** rank 4
  - Wowhead: Increases the area of effect of your Shouts by 40% and reduces the Rage cost by of your Shouts and Howls by 20%.
  - current:   Increases the radius of your Battle Shout and Demoralizing Shout abilities by 40%.
- **Booming Voice** rank 5
  - Wowhead: Increases the area of effect of your Shouts by 50% and reduces the Rage cost by of your Shouts and Howls by 25%.
  - current:   Increases the radius of your Battle Shout and Demoralizing Shout abilities by 50%.
- **Cruelty** rank 1
  - Wowhead: Improves your chance to get a critical strike with melee attacks by 1%.
  - current:   Increases your chance to get a critical strike with melee attacks by 1%.
- **Cruelty** rank 2
  - Wowhead: Improves your chance to get a critical strike with melee attacks by 2%.
  - current:   Increases your chance to get a critical strike with melee attacks by 2%.
- **Cruelty** rank 3
  - Wowhead: Improves your chance to get a critical strike with melee attacks by 3%.
  - current:   Increases your chance to get a critical strike with melee attacks by 3%.
- **Cruelty** rank 4
  - Wowhead: Improves your chance to get a critical strike with melee attacks by 4%.
  - current:   Increases your chance to get a critical strike with melee attacks by 4%.
- **Cruelty** rank 5
  - Wowhead: Improves your chance to get a critical strike with melee attacks by 5%.
  - current:   Increases your chance to get a critical strike with melee attacks by 5%.
- **Defiance** rank 1
  - Wowhead: Increases all threat generated in Defensive stance by an additional 7% while a shield is equipped.
  - current:   Increases all threat generated in Defensive stance by an additional 5% while a shield is equipped.
- **Defiance** rank 2
  - Wowhead: Increases all threat generated in Defensive stance by an additional 13% while a shield is equipped.
  - current:   Increases all threat generated in Defensive stance by an additional 10% while a shield is equipped.
- **Defiance** rank 3
  - Wowhead: Increases all threat generated in Defensive stance by an additional 20% while a shield is equipped.
  - current:   Increases all threat generated in Defensive stance by an additional 15% while a shield is equipped.
- **Dual Wield Specialization** rank 1
  - Wowhead: Increases the damage done by your off-hand weapon by 5% and the Rage generated by your off-hand attacks by 10%.
  - current:   Increases your off-hand weapon damage by 5%, off-hand Rage generation by 20%, and chance to hit with off-hand attacks by 2%.
- **Dual Wield Specialization** rank 2
  - Wowhead: Increases the damage done by your off-hand weapon by 10% and the Rage generated by your off-hand attacks by 20%.
  - current:   Increases your off-hand weapon damage by 5%, off-hand Rage generation by 20%, and chance to hit with off-hand attacks by 2%.
- **Dual Wield Specialization** rank 3
  - Wowhead: Increases the damage done by your off-hand weapon by 15% and the Rage generated by your off-hand attacks by 30%.
  - current:   Increases your off-hand weapon damage by 5%, off-hand Rage generation by 20%, and chance to hit with off-hand attacks by 2%.
- **Dual Wield Specialization** rank 4
  - Wowhead: Increases the damage done by your off-hand weapon by 20% and the Rage generated by your off-hand attacks by 40%.
  - current:   Increases your off-hand weapon damage by 5%, off-hand Rage generation by 20%, and chance to hit with off-hand attacks by 2%.
- **Dual Wield Specialization** rank 5
  - Wowhead: Increases the damage done by your off-hand weapon by 25% and the Rage generated by your off-hand attacks by 50%.
  - current:   Increases your off-hand weapon damage by 5%, off-hand Rage generation by 20%, and chance to hit with off-hand attacks by 2%.
- **Enrage** rank 2
  - Wowhead: Gives you a 30% chance to deal 4% increased Physical damage for 12 sec after being the victim of any damaging attack.
  - current:   Gives you a 60% chance to deal 2% increased Physical damage for 12 sec after being the victim of any damaging attack.
- **Enrage** rank 3
  - Wowhead: Gives you a 30% chance to deal 6% increased Physical damage for 12 sec after being the victim of any damaging attack.
  - current:   Gives you a 90% chance to deal 2% increased Physical damage for 12 sec after being the victim of any damaging attack.
- **Enrage** rank 4
  - Wowhead: Gives you a 30% chance to deal 8% increased Physical damage for 12 sec after being the victim of any damaging attack.
  - current:   Gives you a 120% chance to deal 2% increased Physical damage for 12 sec after being the victim of any damaging attack.
- **Enrage** rank 5
  - Wowhead: Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack.
  - current:   Gives you a 150% chance to deal 2% increased Physical damage for 12 sec after being the victim of any damaging attack.
- **Flurry** rank 1
  - Wowhead: Increases your melee attack speed by 10% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your melee attack speed by 5% for your next 3 swings after dealing a melee critical strike.
- **Flurry** rank 2
  - Wowhead: Increases your melee attack speed by 20% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your melee attack speed by 10% for your next 3 swings after dealing a melee critical strike.
- **Flurry** rank 3
  - Wowhead: Increases your melee attack speed by 30% for your next 3 swings after dealing a melee critical strike.
  - current:   Increases your melee attack speed by 15% for your next 3 swings after dealing a melee critical strike.
- **Improved Disarm** rank 2
  - Wowhead: Reduces the cooldown of your Disarm ability by 13 secs.
  - current:   Reduces the cooldown of your Disarm ability by 14 secs.
- **Improved Disarm** rank 3
  - Wowhead: Reduces the cooldown of your Disarm ability by 20 secs.
  - current:   Reduces the cooldown of your Disarm ability by 21 secs.
- **Improved Execute** rank 2
  - Wowhead: Reduces the Rage cost of your Execute ability by 5.
  - current:   Reduces the Rage cost of your Execute ability by 6.
- **Improved Rend** rank 2
  - Wowhead: Increases the Bleed damage done by your Rend ability by 23%.
  - current:   Increases the Bleed damage done by your Rend ability by 24%.
- **Improved Rend** rank 3
  - Wowhead: Increases the Bleed damage done by your Rend ability by 35%.
  - current:   Increases the Bleed damage done by your Rend ability by 36%.
- **Improved Shield Wall** rank 2
  - Wowhead: Reduces the cooldown of your Shield Wall ability by 11.0 min.
  - current:   Reduces the cooldown of your Shield Wall ability by 5.5 min.
- **Improved Slam** rank 1
  - Wowhead: Reduces the cooldown of your Slam ability by 2.5 sec, the cast time and global cooldown by 0.25 sec, and Slam no longer interrupts or delays your melee swing.
  - current:   Reduces the global cooldown and cast time of your Slam ability by 0.25 sec. In addition, Slam no longer interrupts your melee swing time.
- **Improved Slam** rank 2
  - Wowhead: Reduces the cooldown of your Slam ability by 5.0 sec, the cast time and global cooldown by 0.50 sec, and Slam no longer interrupts or delays your melee swing.
  - current:   Reduces the global cooldown and cast time of your Slam ability by 0.5 sec. In addition, Slam no longer interrupts your melee swing time.
- **Improved Tactical Mastery** rank 1
  - Wowhead: Tactical Mastery lets you retain up to an additional 5 Rage when you change stances.
  - current:   Tactical Mastery lets you retain up to an additional 3 Rage when you change stances.
- **Improved Tactical Mastery** rank 2
  - Wowhead: Tactical Mastery lets you retain up to an additional 10 Rage when you change stances.
  - current:   Tactical Mastery lets you retain up to an additional 6 Rage when you change stances.
- **Improved Tactical Mastery** rank 3
  - Wowhead: Tactical Mastery lets you retain up to an additional 15 Rage when you change stances.
  - current:   Tactical Mastery lets you retain up to an additional 9 Rage when you change stances.
- **Master of Defense** rank 2
  - Wowhead: Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped.
  - current:   Grants you a 100% chance to generate 10 Rage when you Dodge or Parry while a shield is equipped.
- **Piercing Howl** rank 1
  - Wowhead: Causes all enemies within 10 yds to be Dazed, reducing movement speed by 50% for 6 sec.
  - current:   Causes all nearby enemies to be Dazed, reducing movement speed by 50% for 6 sec.
- **Spearing Strike** rank 1
  - Wowhead: A brutal attack that deals 75% weapon damage. Deals an additional 75% weapon damage against Giants, Dragonkin, and mounted targets. Mounted targets are dismounted.
  - current:   A brutal attack that deals 40% weapon damage. Deals an additional 80% weapon damage against Giants, Dragonkin, and mounted targets. Mounted targets are dismounted.
- **Two-Handed Weapon Specialization** rank 1
  - Wowhead: Increases the damage you deal with two-handed melee weapons by 2%.
  - current:   Increases the damage you deal with two-handed melee weapons by 1%.
- **Two-Handed Weapon Specialization** rank 2
  - Wowhead: Increases the damage you deal with two-handed melee weapons by 4%.
  - current:   Increases the damage you deal with two-handed melee weapons by 2%.
- **Two-Handed Weapon Specialization** rank 3
  - Wowhead: Increases the damage you deal with two-handed melee weapons by 6%.
  - current:   Increases the damage you deal with two-handed melee weapons by 3%.
- **Unbridled Wrath** rank 1
  - Wowhead: Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon.
  - current:   Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons.
- **Unbridled Wrath** rank 2
  - Wowhead: Gives you a 24% chance to generate 1 additional Rage when you deal melee damage with a weapon.
  - current:   Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons.
- **Unbridled Wrath** rank 3
  - Wowhead: Gives you a 36% chance to generate 1 additional Rage when you deal melee damage with a weapon.
  - current:   Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons.
- **Unbridled Wrath** rank 4
  - Wowhead: Gives you a 48% chance to generate 1 additional Rage when you deal melee damage with a weapon.
  - current:   Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons.
- **Unbridled Wrath** rank 5
  - Wowhead: Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon.
  - current:   Gives you a 12% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons.
- **Weaponmaster** rank 2
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 2%. Mace/Staff: Your attacks ignore 6% of your target's armor. Sword: Your successful melee attacks have a 2% chance to trigger an extra attack on the target.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 1%. Mace/Staff: Your attacks ignore 3% of your target's armor. Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target.
- **Weaponmaster** rank 3
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 3%. Mace/Staff: Your attacks ignore 9% of your target's armor. Sword: Your successful melee attacks have a 3% chance to trigger an extra attack on the target.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 1%. Mace/Staff: Your attacks ignore 3% of your target's armor. Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target.
- **Weaponmaster** rank 4
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 4%. Mace/Staff: Your attacks ignore 12% of your target's armor. Sword: Your successful melee attacks have a 4% chance to trigger an extra attack on the target.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 1%. Mace/Staff: Your attacks ignore 3% of your target's armor. Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target.
- **Weaponmaster** rank 5
  - Wowhead: Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 5%. Mace/Staff: Your attacks ignore 15% of your target's armor. Sword: Your successful melee attacks have a 5% chance to trigger an extra attack on the target.
  - current:   Gives your melee weapon attacks a benefit depending on the weapon. Axe/Polearm: Increases your critical strike chance by 1%. Mace/Staff: Your attacks ignore 3% of your target's armor. Sword: Your successful melee attacks have a 1% chance to trigger an extra attack on the target.

