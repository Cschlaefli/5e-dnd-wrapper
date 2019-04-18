from dndsdk import Spell

with open('spell_dump', 'w') as f :
    for spell in Spell.all() :
        f.write(str(spell)+ "\n")
