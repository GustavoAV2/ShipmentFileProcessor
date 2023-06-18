from typing import List

from src.domain.models.additional_info import AdditionalInfo
from src.domain.models.billing_value import BillingValue
from src.domain.models.calendar import Calendar
from src.domain.models.person import Person


class Shipment:
    def __init__(self, calendar: Calendar, debtor: Person, value: BillingValue, key: str, payer_request: str, additional_info: List[AdditionalInfo]):
        self.calendar = calendar
        self.debtor = debtor
        self.value = value
        self.key = key
        self.payer_request = payer_request
        self.additional_info = additional_info
