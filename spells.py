from dndsdk import Spell

spells = Spell.where(name="Mage Armor")
for spell in spells :
    print(spell.desc)

