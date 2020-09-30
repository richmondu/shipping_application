from shipping_fee.parcel.parcel import Parcel
from shipping_fee.discount.voucher import Voucher
from typing import Tuple


class ShippingFee:

	def __init__(self, voucher: str, weight: float, height: float, width: float, length: float):
		self.parcel = Parcel(weight, height, width, length)
		self.voucher = Voucher(voucher)

	def get_code(self):
		return self.voucher.get_code()

	def _get_discounted_price(self, cost: float, percent_discount: float) -> float:
		return cost * (100-percent_discount) / 100

	def get_fee(self) -> Tuple[str, str, str]:
		original_price = self.parcel.get_cost()
		percent_discount = self.voucher.get_discount()

		if original_price == "N/A":
			return original_price, original_price, original_price
		if percent_discount == 0:
			return original_price, "0%", original_price

		discounted_price = self._get_discounted_price(float(original_price), percent_discount)
		return str(discounted_price), str(percent_discount)+"%", original_price

