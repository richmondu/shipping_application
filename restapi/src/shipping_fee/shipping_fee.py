from shipping_fee.parcel.parcel import Parcel
from shipping_fee.discount.voucher import Voucher


class ShippingFee:

	def __init__(self, voucher, weight, height, width, length):
		self.parcel = Parcel(weight, height, width, length)
		self.voucher = Voucher(voucher)

	def _get_discounted_price(self, cost, discount):
		return cost * (100-discount) / 100

	def get_fee(self):
		original_price = self.parcel.get_cost()
		discount = self.voucher.get_discount()

		if original_price == "N/A":
			return original_price, original_price, original_price
		if discount == 0:
			return original_price, "0%", original_price

		discounted_price = self._get_discounted_price(float(original_price), discount)
		return str(discounted_price), str(discount)+"%", original_price

