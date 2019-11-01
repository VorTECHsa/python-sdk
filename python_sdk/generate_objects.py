import jsons

from python_sdk.api.resources.product_entry import ProductEntity

a = ProductEntity("Sf", "grade", 0.444, "Grane")

serialized = open("./python_sdk/examples/product_entry1.json", 'r').read()
print(serialized)

deserialized = jsons.loads(serialized, ProductEntity)
print(deserialized)
