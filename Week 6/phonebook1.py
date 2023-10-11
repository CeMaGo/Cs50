
# `people = {}`  is the shortcut for `People = dict()`, `[]` would be for `list()`



people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

# Version 1
# name = input("Name: ")
# if name in people:
#     print(f"Number: {people[name]}")


name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
