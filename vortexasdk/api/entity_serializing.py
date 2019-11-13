from itertools import groupby
from typing import List

import jsons
# noinspection PyProtectedMember
from flatten_dict import flatten

from vortexasdk.api.cargo_movement import CargoEvent, CargoMovement
from vortexasdk.api.shared_types import Entity
from vortexasdk.api.vessel import VesselEntity


def _group_by_layer(entity_list: List[Entity]) -> dict:
    return {e.layer: e for e in entity_list}


def _format_keys(dictionary):
    flat_with_formatted_keys = {}
    for k, v in dictionary.items():
        nice_path = ".".join([str(i) for i in k])
        flat_with_formatted_keys[nice_path] = v
    return flat_with_formatted_keys


def serialize(dataclass):
    """Serialize data class attributes."""
    return jsons.loads(jsons.dumps(dataclass))


def _serialize_ve_layer(ve: VesselEntity) -> dict:
    d = serialize(ve)
    d.update({"corporate_entities": _group_by_layer(ve.corporate_entities)})
    return serialize(d)


def _serialize_ce_layer(ce: CargoEvent) -> dict:
    d = serialize(ce)
    d.update({"location": _group_by_layer(ce.location)})
    return serialize(d)


def _group_cme_attributes_by_layer(cme: CargoMovement) -> dict:
    """Group relevant CargoMovementEntity attributes by `Entity.layer`."""
    vessels = [_serialize_ve_layer(ve) for ve in cme.vessels]
    products = _group_by_layer(cme.product)

    events = {event_type: list(g) for event_type, g in groupby(cme.events, lambda x: x.event_type)}
    events_attributes = {event_type: [_serialize_ce_layer(ce) for ce in es] for event_type, es in
                         events.items()}

    d = serialize(cme)
    d.update({"product": products})
    d.update({"vessels": vessels})
    d.update({"events": events_attributes})
    return serialize(d)


def convert_cme_to_flat_dict(cme: CargoMovement, cols='all') -> dict:
    """Convert nested `CargoMovementEntity` object to flat dictionary, keeping *cols*."""
    as_dict = _group_cme_attributes_by_layer(cme)

    flat = flatten(as_dict, enumerate_types=(list,))

    formatted = _format_keys(flat)

    if cols == 'all':
        return formatted
    else:
        return {k: v for k, v in formatted.items() if k in cols}
