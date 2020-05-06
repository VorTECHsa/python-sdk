from enum import Enum


class VesselAttributesEnum(str, Enum):
    """
    These are possible values that the `tag` key of a Vessel Attribute can be

    """

    FlagTag = "vessel_flag_tag"
    ScrubberTag = "vessel_scrubber_tag"


class ScrubbersFittedEnum(str, Enum):
    """
    These are the 3 values that the API expects for this filter

    """

    Off = ("off",)
    Included = ("inc",)
    Excluded = "exc"


class AttributesTypesEnum(str, Enum):
    """
    These are possible values that the `type` arg of the Attribute search can be

    """

    IceClass = ("ice_class",)
    Propulsion = ("propulsion",)
