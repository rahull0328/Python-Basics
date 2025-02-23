friends = ["Rahul", "Amit", "Sneha", "Priya", "Vikram"]

bff_nicknames = {
    "Rahul": "Rahu",
    "Sneha": "Snehu",
    "Vikram": "Viku"
}

for i in range(len(friends)):
    if friends[i] in bff_nicknames:
        friends[i] = bff_nicknames[friends[i]]

print("Updated Friends List:", friends)
