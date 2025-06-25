#!/usr/bin/env python3
def famous_births(name_and_date_of_birth):
    def sort_key(scientist):
        return scientist["date_of_birth"]
    
    scientists = list(name_and_date_of_birth.values())
    scientists = sorted(scientists, key=sort_key)

    for scientist in scientists:
        print(f"{scientist['name']} was born in {scientist['date_of_birth']}")

    
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)


#chmod +x persons_of_interest.py