print("lesson 4 for lists and appenders")

flowers = ["rose", "lily", "tulip", "daisy", "sunflower"]
print("Flowers:", flowers)

flowers.append("orchid")
print("Updated Flowers:", flowers)

print("Iterating through the list of flowers:")
for flower in flowers:
    print(flower)

print("remove a flower from the list")
flowers.remove("lily")
print("Updated Flowers:", flowers)
