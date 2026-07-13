from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
from vortexasdk import Fixtures
from vortexasdk.api.entity_flattening import convert_to_flat_dict, convert_fixture_to_flat_dict

if __name__ == '__main__':
    print("Fetching fixtures from API...")
    result = Fixtures().search(
        filter_time_min=datetime(2024, 1, 1),
        filter_time_max=datetime(2024, 1, 7),
    )
    raw_records = result.records
    print(f"Got {len(raw_records)} fixtures")

    # Find a record with all three corporate entity layers
    record = None
    for r in raw_records:
        ce = r.get("vessel", {}).get("corporate_entities", [])
        layers = {e.get("layer") for e in ce}
        if {"charterer", "effective_controller", "time_charterer"} <= layers:
            record = r
            break

    if not record:
        # Fallback: find one with at least 2
        for r in raw_records:
            ce = r.get("vessel", {}).get("corporate_entities", [])
            if len(ce) > 1:
                record = r
                break

    if not record:
        record = raw_records[0]

    ce = record.get("vessel", {}).get("corporate_entities", [])
    layers = [e.get("layer") for e in ce]
    print(f"Using fixture: {record['vessel']['name']} (layers: {layers})\n")

    expected = [
        "vessel.name",
        "vessel.imo",
        "tonnes",
        "vessel.corporate_entities.charterer.label",
        "vessel.corporate_entities.effective_controller.label",
        "vessel.corporate_entities.time_charterer.label",
    ]

    print("BEFORE FIX (convert_to_flat_dict):")
    flat_before = convert_to_flat_dict(record, columns="all")
    for col in expected:
        print(f"  {'✅' if col in flat_before else '❌'} {col} = {flat_before.get(col, 'MISSING')}")

    print("\nAFTER FIX (convert_fixture_to_flat_dict):")
    flat_after = convert_fixture_to_flat_dict(record, columns="all")
    for col in expected:
        print(f"  {'✅' if col in flat_after else '❌'} {col} = {flat_after.get(col, 'MISSING')}")
