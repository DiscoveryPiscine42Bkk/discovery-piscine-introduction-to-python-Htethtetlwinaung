#!/usr/bin/env python3
def array_of_names(names):
    full_names = []
    for first_name, last_name in names.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    return full_names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))

#chmod +x your_namebook.py