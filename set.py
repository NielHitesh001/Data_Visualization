branch1 = ["P101", "P102", "P103", "P104"]
branch2 = ["P103", "P104", "P105", "P106"]

set1 = set(branch1)
set2 = set(branch2)

unique_ids = set1 | set2
common_ids = set1 & set2

print("Unique Product IDs:", unique_ids)
print("Common Product IDs:", common_ids)