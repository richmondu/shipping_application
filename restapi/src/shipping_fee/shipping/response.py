from flask import jsonify


class ShippingFeeResponse:

	def __init__(self, discounted_price: str, percent_discount: str, original_price: str):
		self.discounted_price = discounted_price
		self.percent_discount = percent_discount
		self.original_price = original_price

	def get(self):
		if self.discounted_price == "N/A":
			return jsonify(price=self.discounted_price)
		if code is None:
			return jsonify(price=self.discounted_price, currency="PHP")
		return jsonify(price=self.discounted_price, discount=self.percent_discount, original_price=self.original_price, currency="PHP")
