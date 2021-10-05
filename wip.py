import copy
from creature import Creature

gremlin = Creature('gremlin')
orc_mage = Creature('orc_mage')
orc_mage2 = copy.deepcopy(orc_mage)

print(gremlin.name)
print(gremlin.spawn_time)
print(gremlin.health)
print(id(gremlin))

print(orc_mage.name)
print(orc_mage.spawn_time)
print(orc_mage.health)
print(id(orc_mage))

print(orc_mage2.name)
print(orc_mage2.spawn_time)
print(orc_mage2.health)
print(id(orc_mage2))
