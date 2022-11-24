from pydantic import BaseModel
from typing import Optional
from enum import Enum


class DeliveryMethodType(Enum):
    FOB = "FOB"
    DES = "DES"
    CFR = "CFR"
    CIF = "CIF"


class ContractType(Enum):
    Spot = "spot"
    Term = "term"


class TradeType(Enum):
    Load = "load",
    Discharge = "discharge"


class Trade(BaseModel):
    buyer_label: Optional[str] = None
    buyer_id: Optional[str] = None
    seller_label: Optional[str] = None
    seller_id: Optional[str] = None
    contract_type: Optional[ContractType] = None
    delivery_method: Optional[DeliveryMethodType] = None
    type: Optional[TradeType] = None
