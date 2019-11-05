'''
This is the file heading docstring
'''
from python_sdk.movements import CargoMovements

result = CargoMovements().search(
    filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
    filter_time_min="2019-08-29T00:00:00.000Z",
    filter_time_max="2019-10-30T00:00:00.000Z",
)

print(result[0])


# CHINA
print("Done!")
