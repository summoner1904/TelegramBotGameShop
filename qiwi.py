from pyqiwip2p import QiwiP2P
from pyqiwip2p import p2p_types
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime
from config import QIWI_PRIV_KEY

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)


class Bill:
    def create_gta_bill(self, message_id):
        """
        Метод, создающий новый счёт для оплаты аккаунта GTA.
        :param message_id: int (Идентификатор сообщения. Используется для генерации уникального платежа).
        :return: str (Ссылка на оплату счёта).
        """
        gta_bill = p2p.bill(bill_id=message_id, amount=249, lifetime=10)
        return gta_bill.pay_url

    def create_rust_bill(self, message_id):
        """
        Метод, создающий новый счёт для оплаты аккаунта Rust.
        :param message_id: int (Идентификатор сообщения. Используется для генерации уникального платежа).
        :return: str (Ссылка на оплату счёта).
        """
        rust_bill = p2p.bill(bill_id=message_id, amount=199, lifetime=10)
        return rust_bill.pay_url

    def create_fortnite_bill(self, message_id):
        """
        Метод, создающий новый счёт для оплаты аккаунта Fortnite.
        :param message_id: int (Идентификатор сообщения. Используется для генерации уникального платежа).
        :return: str (Ссылка на оплату счёта).
        """
        fortnite_bill = p2p.bill(bill_id=message_id, amount=1799, lifetime=10)
        return fortnite_bill.pay_url

    def create_battlefield_bill(self, message_id):
        """
        Метод, создающий новый счёт для оплаты аккаунта Battlefield.
        :param message_id: int (Идентификатор сообщения. Используется для генерации уникального платежа).
        :return: str (Ссылка на оплату счёта).
        """
        battlefield_bill = p2p.bill(bill_id=message_id, amount=699, lifetime=10)
        return battlefield_bill.pay_url

    def create_cod_bill(self, message_id):
        """
        Метод, создающий новый счёт для оплаты аккаунта Call of Duty.
        :param message_id: int (Идентификатор сообщения. Используется для генерации уникального платежа).
        :return: str (Ссылка на оплату счёта).
        """
        cod_bill = p2p.bill(bill_id=message_id, amount=699, lifetime=10)
        return cod_bill.pay_url

    def create_dota_bill(self, message_id):
        """
        Метод, создающий новый счёт для оплаты аккаунта Dota 2.
        :param message_id: int (Идентификатор сообщения. Используется для генерации уникального платежа).
        :return: str (Ссылка на оплату счёта).
        """
        dota_bill = p2p.bill(bill_id=message_id, amount=3299, lifetime=10)
        return dota_bill.pay_url

    def check_pay(self, message_id):
        """
        Метод, использующийся для проверки статуса (оплаты) счёта.
        :param message_id: int (Идентификатор сообщения. Используется для нахождения платежа в системе по bill_id).
        :return: bool (Если возвращает True - значит оплата прошла успешно).
        """
        if p2p.check(bill_id=message_id - 1).status == "PAID":
            return True
