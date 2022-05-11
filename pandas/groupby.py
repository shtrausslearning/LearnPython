# aggregate

print(g['price'].agg(np.sum))
print("---------------------------------")
# method 2, use the native function to sum the price for each group
print(g.sum()["price"])

df = pd.read_csv("sample2.csv", sep=",")
g = df.groupby("name")
print("calculate the sum/mean/std for name group price column")
print(g["price"].agg([np.sum, np.mean, np.std]))

# iterate groupby

df = pd.read_csv("sample2.csv", sep=",")
g = df.groupby("name")

for name, gr in g:
    print("current group is {}".format(name))
    print(f"the corresponding data under group {name}")
    print("------------------------------------")
    print(gr)
    print("------------------------------------")
