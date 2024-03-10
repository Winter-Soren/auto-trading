from typing import TypedDict

class PlaceOrderParamsType(TypedDict):
    quantity: float
    product: str
    validity: str
    price: float
    tag: str
    instrument_token: str
    order_type: str
    transaction_type: str
    disclosed_quantity: int
    trigger_price: float
    is_amo: bool
