# About VortexaSDK Endpoints

The endpoints module allows you to query Vortexa's data.

The VortexaSDK currently contains the following endpoints:

1. Cargo Movements
2. Voyages
3. Charterers
4. Geographies
5. Products
6. Vessels
7. Cargo Time Series
8. EIA Forecasts
9. Tonne-miles
10. Vessel Availability
11. Crude Onshore Inventories
12. Freight Pricing

Each endpoint offers either one, or both, of two different functionalities:

1. **Lookup by ID**. Retrieve an object matching a certain id. In sql speak this is the equivalent of `SELECT * FROM vessels WHERE id = 12345;`
2. **Search**. Retrieve a number of objects matching given search parameters. In sql speak this is the equivalent of `SELECT * FROM vessels WHERE name ~* 'ocean' AND vessel_class = 'vlcc';`

Let's explain with some examples:

Find all aframax vessels

```python
from vortexasdk import Vessels
df = Vessels().search(vessel_classes='aframax').to_df()
```


Find the vessel that has with id 12345

```python
vessel = Vessels().reference(id='12345')
```
