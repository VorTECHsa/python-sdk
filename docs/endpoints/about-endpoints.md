# About VortexaSDK Endpoints

The endpoints module allows you to query Vortexa's data.

The VortexaSDK currently contains the following endpoints:

1. Cargo Movements
1. Voyages
1. Charterers
1. Geographies
1. Products
1. Vessels
1. Cargo Time Series
1. EIA Forecasts
1. Tonne-miles
1. Vessel Availability
1. Crude Onshore Inventories
1. Freight Pricing
1. Vessel Summary
1. Vessel Positions
1. Canal transit
1. Canal transit Time Series

Each endpoint offers either one, or both, of two different functionalities:

1. **Lookup by ID**. Retrieve an object matching a certain id. In sql speak this is the equivalent of `SELECT * FROM vessels WHERE id = 12345;`
2. **Search**. Retrieve a number of objects matching given search parameters. In sql speak this is the equivalent of `SELECT * FROM vessels WHERE name ~* 'ocean' AND vessel_class = 'vlcc';`

Let's explain with some examples:

Find all aframax vessels

```python
from vortexasdk import Vessels
df = Vessels().search(vessel_classes='oil_aframax').to_df()
```

Find the vessel that has with id 12345

```python
vessel = Vessels().reference(id='12345')
```
