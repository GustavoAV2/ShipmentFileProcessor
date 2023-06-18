
class Shipment:
    def __init__(self, calendar, debtor, loc, value, key, payer_request, additional_info):
        self.calendar = calendar
        self.debtor = debtor
        self.loc = loc
        self.value = value
        self.key = key
        self.payer_request = payer_request
        self.additional_info = additional_info
