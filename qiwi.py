from pyqiwip2p import QiwiP2P
from pyqiwip2p import p2p_types
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime
from qiwi_token import QIWI_PRIV_KEY

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

class GenerateBill:
    def create_gta_bill(self):
        gta_bill = p2p.bill(bill_id=3, amount=1, lifetime=10)
        return gta_bill.pay_url

    def check_gta_bill(self):
        status_pay = p2p.check(bill_id=3).status
        return status_pay

    def create_rust_bill(self):
        rust_bill = p2p.bill(bill_id=4, amount=1, lifetime=10)
        return rust_bill.pay_url

    def check_rust_bill(self):
        status_pay = p2p.check(bill_id=4).status
        return status_pay

    def create_fortnite_bill(self):
        fortnite_bill = p2p.bill(bill_id=5, amount=1, lifetime=10)
        return fortnite_bill.pay_url

    def check_fortnite_bill(self):
        status_pay = p2p.check(bill_id=5).status
        return status_pay

    def create_battlefield_bill(self):
        battlefield_bill = p2p.bill(bill_id=6, amount=1, lifetime=10)
        return battlefield_bill.pay_url

    def check_battlefield_bill(self):
        status_pay = p2p.check(bill_id=6).status
        return status_pay

    def create_cod_bill(self):
        cod_bill = p2p.bill(bill_id=7, amount=1, lifetime=10)
        return cod_bill.pay_url

    def check_cod_bill(self):
        status_pay = p2p.check(bill_id=7).status
        return status_pay

    def create_dota_bill(self):
        dota_bill = p2p.bill(bill_id=8, amount=1, lifetime=10)
        return dota_bill.pay_url

    def check_dota_bill(self):
        status_pay = p2p.check(bill_id=8).status
        return status_pay
