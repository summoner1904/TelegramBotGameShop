from pyqiwip2p import QiwiP2P
from pyqiwip2p import p2p_types
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime
from config import QIWI_PRIV_KEY

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

class Bill:
    def create_gta_bill(self, message_id):
        gta_bill = p2p.bill(bill_id=message_id,amount=1, lifetime=10)
        return gta_bill.pay_url

    def create_rust_bill(self, message_id):
        rust_bill = p2p.bill(bill_id=message_id,amount=1, lifetime=10)
        return rust_bill.pay_url

    def create_fortnite_bill(self, message_id):
        fortnite_bill = p2p.bill(bill_id=message_id,amount=1, lifetime=10)
        return fortnite_bill.pay_url

    def create_battlefield_bill(self, message_id):
        battlefield_bill = p2p.bill(bill_id=message_id,amount=1, lifetime=10)
        return battlefield_bill.pay_url

    def create_cod_bill(self, message_id):
        cod_bill = p2p.bill(bill_id=message_id,amount=1, lifetime=10)
        return cod_bill.pay_url

    def create_dota_bill(self, message_id):
        dota_bill = p2p.bill(bill_id=message_id,amount=1, lifetime=10)
        return dota_bill.pay_url

    def check_pay(self, message_id):
        if p2p.check(bill_id=message_id-1).status == "PAID":
            return True
