from flask import Blueprint, jsonify, abort, request
from shipping_fee.util.api_logger import ApiLogger
from shipping_fee.util.api_exception import ApiException
from shipping_fee.shipping_fee import ShippingFee


blueprint_shippingfee = Blueprint('blueprint_shippingfee', __name__)


@blueprint_shippingfee.route("/fee", methods=['GET'])
@ApiException.handle
@ApiLogger.log
def compute_shipping_fee():

	weight = float(request.args.get('weight'))
	height = float(request.args.get('height'))
	width = float(request.args.get('width'))
	length = float(request.args.get('length'))
	code = request.args.get('code')
	print(code)

	shipping = ShippingFee(code, weight, height, width, length)
	shipping_fee = shipping.get_fee()
	return jsonify(fee=shipping_fee)



