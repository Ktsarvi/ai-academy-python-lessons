# # Demonstrating built-in hash values
# print(hash("hello"))      # Returns an integer hash for the string
# print(hash((1, 2, 3)))   # Returns an integer hash for the tuple

hashes = {}
inputs = ["apple", "banana", "orange", "grape"]

for value in inputs:
    h = hash(value)

    if h in hashes:
        print("Collision found:")
        print(hashes[h], "and", value)
        print("Hash:", h)
    else:
        hashes[h] = value