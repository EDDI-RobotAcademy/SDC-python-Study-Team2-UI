from custom_protocol.entity.CustomProtocol import CustomProtocol
from order_form.repository.OrderFormRepository import OrderFormRepository
from utility.keyboard.KeyboardInput import KeyboardInput


class OrderFormRepositoryImpl(OrderFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("OrderFormRepositoryImpl 초기화")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createOrderPurchaseForm(self):
        print("상품을 구매합니다.")
        return

    def createOrderListForm(self):
        print("주문 내역을 출력합니다.")
        return

    def createOrderDeleteForm(self):
        print("주문을 취소합니다.")
        return