import requests
import shipping_fee.discount.voucher_config as cfg


class Voucher:

	def __init__(self, code):
		self.code = code

	def get_discount(self) -> float:
		query = '?key=' + cfg.CONFIG_VOUCHER_KEY
		url = 'https://' + cfg.CONFIG_BASE_URL + cfg.CONFIG_VOUCHER_API.format(self.code) + query

		try:
			resp = requests.get(url)
			if resp.status_code != 200:
				return 0
			#print(resp.json())
			return resp.json()['discount']
		except:
			return 0


