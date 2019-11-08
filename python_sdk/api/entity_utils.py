from itertools import groupby
from typing import List

import jsons
# noinspection PyProtectedMember
from flatten_dict import flatten

from python_sdk.api.entities import CargoEventEntity, CargoMovementEntity, Entity, VesselEntity


def group_by_layer(entity_list: List[Entity]) -> dict:
    return {e.layer: e for e in entity_list}


def serde(dataclass):
    return jsons.loads(jsons.dumps(dataclass))


def format_keys(dictionary):
    flat_with_formatted_keys = {}
    for k, v in dictionary.items():
        nice_path = ".".join([str(i) for i in k])
        flat_with_formatted_keys[nice_path] = v
    return flat_with_formatted_keys


def group_ve_layer_attributes(ve: VesselEntity) -> dict:
    d = serde(ve)
    d.update({"corporate_entities": group_by_layer(ve.corporate_entities)})
    return serde(d)


def group_ce_layer_attributes(ce: CargoEventEntity) -> dict:
    d = serde(ce)
    d.update({"location": group_by_layer(ce.location)})
    return serde(d)


def group_cme_layer_attributes(cme: CargoMovementEntity) -> dict:
    vessels = [group_ve_layer_attributes(ve) for ve in cme.vessels]
    products = group_by_layer(cme.product)

    events = {event_type: list(g) for event_type, g in groupby(cme.events, lambda x: x.event_type)}
    events_attributes = {event_type: [group_ce_layer_attributes(ce) for ce in es] for event_type, es in events.items()}

    d = serde(cme)
    d.update({"product": products})
    d.update({"vessels": vessels})
    d.update({"events": events_attributes})
    return serde(d)


def extract_dict_from_cme(cme: CargoMovementEntity, cols=None) -> dict:
    as_dict = group_cme_layer_attributes(cme)

    flat = flatten(as_dict, enumerate_types=(list,))

    formatted = format_keys(flat)

    default = [
        'events.cargo_port_load_event.0.label',
        'events.cargo_port_unload_event.0.label',
        'product.group.label',
        'quantity',
        'vessels.0.name',
        'events.cargo_port_load_event.0.start_timestamp',
        'events.cargo_port_unload_event.0.start_timestamp',
    ]

    if cols == 'all':
        return formatted

    if cols is None:
        cols = default

    return {k: v for k, v in formatted.items() if k in cols}
