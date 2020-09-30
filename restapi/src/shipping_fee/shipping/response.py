from flask import jsonify
from shipping_fee.shipping.shipping_fee import ShippingFee


class ShippingFeeResponse:

	def __init__(self, shipping: ShippingFee):
		self.shipping = shipping

	def get(self):
		discounted_price, percent_discount, original_price = self.shipping.get_fee()
		if discounted_price == "N/A":
			return jsonify(price=discounted_price)
		if self.shipping.get_code() is None:
			return jsonify(price=discounted_price, currency="PHP")
		return jsonify(price=discounted_price, discount=percent_discount, original_price=original_price, currency="PHP")
