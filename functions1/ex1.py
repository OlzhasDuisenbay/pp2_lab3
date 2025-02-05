"""A recipe you are reading states how many grams you need for the ingredient. Unfortunately,
your store only sells items in ounces. Create a function to convert grams to ounces.
ounces = 28.3495231 * grams"""
def func(grams):
    return grams * 28.3495231
gram = float(input("how many grams: "))
print(func(gram),"ounces")
#400 >>> 11339.809239999999 ounces
