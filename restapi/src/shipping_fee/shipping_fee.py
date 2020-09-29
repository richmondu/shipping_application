from shipping_fee.parcel.parcel import Parcel
from shipping_fee.discount.voucher import Voucher


class ShippingFee:

	def __init__(self, voucher, weight, height, width, length):
		self.parcel = Parcel(weight, height, width, length)
		self.voucher = Voucher(voucher)

	def _get_discounted_price(self, cost, discount):
		return cost * (100-discount) / 100

	def get_fee(self):
		cost = self.parcel.get_cost()
		discount = self.voucher.get_discount()

		if cost == "N/A":
			return cost
		if discount == 0:
			return cost

		discounted_price = str(self._get_discounted_price(float(cost), discount))
		return discounted_price

