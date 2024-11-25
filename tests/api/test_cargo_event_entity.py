from unittest import TestCase

from vortexasdk.api.cargo_movement import CargoPortUnloadEvent


class TestCargoEventEntity(TestCase):
    def test_serialize(self) -> None:
        CargoPortUnloadEvent.model_validate(
            {
                "event_type": "cargo_port_unload_event",
                "location": [
                    {
                        "id": "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
                        "layer": "country",
                        "label": "United Kingdom",
                        "source": "model",
                        "probability": 1,
                    }
                ],
                "probability": 1,
                "pos": [-0.256674902984994, 53.74191566386998],
                "vessel_id": "c1dd5bcc5814a98afdd94bc90eeb6f2dcd1b30367dd08f112ca49e84db88876c",
                "start_timestamp": "2019-10-24T13:16:43+0000",
                "end_timestamp": "2019-10-25T00:40:46+0000",
            }
        )
