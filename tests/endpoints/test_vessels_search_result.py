from unittest import TestCase

import pandas as pd

from tests.mock_client import example_vessels
from vortexa.endpoints.vessels import VesselsSearchResult


class TestVesselsSearchResult(TestCase):
    vsr = VesselsSearchResult(example_vessels)

    def test_to_df(self):
        df = self.vsr.to_df('all')

        expected = pd.DataFrame({'call_sign': {0: '3269', 1: '839'}, 'dead_weight': {0: 6403, 1: 5000},
                                 'id': {0: '15cdb9941761da4fb069cd6ce153b6ad1c48eallowed_high_entropy_string',
                                        1: '1761da4fb069cd6ce153b6ad1c48e15cdb994allowed_high_entropy_string'},
                                 'mmsi': {0: 900403269, 1: 413771781},
                                 'name': {0: '0', 1: '058'}, 'to_bow': {0: 120, 1: 18}, 'to_port': {0: 30, 1: 47},
                                 'to_starboard': {0: 5, 1: 36},
                                 'to_stern': {0: 5, 1: 28}, 'related_names': {0: ['0'], 1: ['058']},
                                 'current_product_type': {0: [
                                     {
                                         'cargo_movement_id': '12d2cbca522e5570ea988b30850ad5b762e16allowed_high_entropy_string',
                                         'product_type': [
                                             {'id': 'b68cbb746f8b9098c50e2ba36bcad83001a53allowed_high_entropy_string',
                                              'layer': 'group',
                                              'label': 'Clean products'},
                                             {'id': 'fb069cd6ce153b615cdb9941761da4ad1c48eallowed_high_entropy_string',
                                              'layer': 'group_product',
                                              'label': 'Other Clean products'}], 'active': False}], 1: [
                                     {
                                         'cargo_movement_id': '5b74c0aab0353cccb28a1bed34c04d7fa5412allowed_high_entropy_string',
                                         'product_type': [
                                             {'id': 'b68cbb746f8b9098c50e2ba36bcad83001a53allowed_high_entropy_string',
                                              'layer': 'group',
                                              'label': 'Clean products'},
                                             {'id': 'fb069cd6ce153b615cdb9941761da4ad1c48eallowed_high_entropy_string',
                                              'layer': 'group_product',
                                              'label': 'Other Clean products'}], 'active': False},
                                     {
                                         'cargo_movement_id': '85cdb9941fb063b6761da4ad1c48e9cd6ce15allowed_high_entropy_string',
                                         'product_type': [
                                             {'id': 'b68cbb746f8b9098c50e2ba36bcad83001a53allowed_high_entropy_string',
                                              'layer': 'group',
                                              'label': 'Clean products'},
                                             {'id': 'a75fcc09bfc7d16496de3336551bc52b58918allowed_high_entropy_string',
                                              'layer': 'group_product',
                                              'label': 'Biodiesel'}], 'active': False}]},
                                 'parent': {
                                     0: [{'name': 'Tiny Tanker', 'layer': ['vessel_class'], 'id': 'tiny_tanker'}],
                                     1: [{'name': 'Tiny Tanker', 'layer': ['vessel_class'], 'id': 'tiny_tanker'}]},
                                 'ref_type': {0: 'vessel', 1: 'vessel'},
                                 'vessel_status': {0: 'vessel_status_ballast', 1: 'vessel_status_laden_unknown'},
                                 'corporate_entities': {0: [], 1: []},
                                 'leaf': {0: True, 1: True}, 'vessel_class': {0: 'tiny_tanker', 1: 'tiny_tanker'},
                                 'cubic_capacity': {0: 7060, 1: 6318},
                                 'tags': {0: [{'tag': 'vessel_decommissioned_tag',
                                               'start_timestamp': '2016-06-08T09:44:57+0000'}],
                                          1: [{'tag': 'vessel_decommissioned_tag',
                                               'start_timestamp': '2017-07-11T13:42:37+0000'}]},
                                 'layer': {0: ['vessel'], 1: ['vessel']}})

        assert expected.equals(df)
