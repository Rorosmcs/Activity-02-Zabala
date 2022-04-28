import random
print(""" A Lv. 95 Electiviter  Electric, Sp. Atk: 85 attacks a Lv. 95 Electivire Marshtomp(Water/Ground, Sp, Def: 175) with Thurder Wave, a Electric type moves
with a Power of 105 and agains same-type attack bonus.. It hits the target normally but it deals a super effective damage. 
The weather on the field is normal. Given the following conditions, determine how much damage Electivire will deal.""")

targets = 1
weather = 1
badge = 1
crit = random.randint(1,2)
random1 = round(random.uniform(0.85, 1.00),2)
stab = 1
type = round(random.uniform(0.25, 0.50),2)
other = 1
opt = random.randint(0,1)

modifier = targets * weather * badge * crit * random1 * stab * type * other
damage = round(((((2*95)/5+2)*105*(85/175))/50)+2,2)
tdamage = round((damage * modifier),2)

print("Modifiers: ")
print("Target: ",targets)
print("Weather: ",weather)
print("Badge:",badge)
print("Crit: ",crit)
print("Random: ",random1)
print("Stab: ", stab)
print("Type: ",type)
print("Other: ",other)

print("Damage: ",damage)
print("Modifier: ",modifier)
print("Total Damage: ",round((tdamage),2))
