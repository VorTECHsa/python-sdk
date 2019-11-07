# # noinspection PyUnresolvedReferences
# from typing import List
#
# # noinspection PyUnresolvedReferences
# from python_sdk.api.entities import CargoMovementEntity, VesselEntity
#
# # noinspection PyUnresolvedReferences
# import pandas as pd
#
# # noinspection PyUnresolvedReferences
# import jsons
#
# from python_sdk.endpoints.cargo_movements import CargoMovements
# from python_sdk.endpoints.vessels import Vessels
#
# # print(tabulate(v, headers='keys', tablefmt='pipe'))
#
# movements = CargoMovements().search(
#     filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
#     filter_time_min="2019-08-29T00:00:00.000Z",
#     filter_time_max="2019-10-30T00:00:00.000Z",
# )[:10]
#
# from flatten_dict import flatten
#
# cm = movements[0]
#
# #
# CARGO_MOVEMENT_ID = "cargo_movement_id"
# QUANTITY = "quantity"
# STATUS = "status"
# VESSEL_ID = "vessel_id"
# VESSEL_NAME = "vessel_name"
# top_level = [CARGO_MOVEMENT_ID, QUANTITY, STATUS]
#
#
# def extract_dict(dataclass, cols) -> dict:
#     as_dict = jsons.loads(jsons.dumps(dataclass))
#
#     flat = flatten(as_dict, enumerate_types=(list,))
#
#     flat_with_formatted_keys = {}
#     for k, v in flat.items():
#         nice_path = ".".join([str(i) for i in k])
#         flat_with_formatted_keys[nice_path] = v
#
#     return flat_with_formatted_keys
#
#
# records = [extract_dict(cm, top_level) for cm in movements]
# df = pd.DataFrame(records)
# #
# # v = movements[0]
# #
# # v_json = jsons.dumps(v)
# # v_dict = jsons.loads(v_json)
# # flat = flatten(v_dict, enumerate_types=(list,))
