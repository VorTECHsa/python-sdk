# # noinspection PyUnresolvedReferences
# from dataclasses import asdict
# from itertools import groupby
#
# # noinspection PyUnresolvedReferences
# import jsons
# # noinspection PyUnresolvedReferences
# import pandas as pd
# # noinspection PyUnresolvedReferences
# from tabulate import tabulate
#
# # noinspection PyUnresolvedReferences
# from python_sdk.api.entities import CargoEventEntity, CargoMovementEntity, Entity, VesselEntity
# from python_sdk.api.entity_utils import group_by_layer
# from python_sdk.endpoints.cargo_movements import CargoMovements
# # noinspection PyUnresolvedReferences
# from python_sdk.endpoints.vessels import Vessels
#
# # print(tabulate(v, headers='keys', tablefmt='pipe'))
#
# movements = CargoMovements().search(
#     filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
#     filter_time_min="2019-08-29T00:00:00.000Z",
#     filter_time_max="2019-10-30T00:00:00.000Z",
# )
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
