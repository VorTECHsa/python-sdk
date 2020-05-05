from enum import Enum


class VesselAttributesEnum(str, Enum):
    FlagTag = "vessel_flag_tag"
    ScrubberTag = "vessel_scrubber_tag"


class ScrubbersFittedEnum(str, Enum):
    Off = ("off",)
    Included = ("inc",)
    Excluded = "exc"
