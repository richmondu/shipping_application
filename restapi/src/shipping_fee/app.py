from shipping_fee.blueprint_shippingfee import blueprint_shippingfee


class ShippingFeeApp:

	def __init__(self, app):
		app.register_blueprint(blueprint_shippingfee, url_prefix="/api/v1/shipping")
