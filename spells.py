from dndsdk import Spell

spells = Spell.where(name="Mage Armor").all()
for spell in spells :
    print(spell.name)

