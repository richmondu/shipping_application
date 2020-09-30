import requests
import shipping_fee.discount.voucher_config as cfg


class Voucher:

	def __init__(self, code: str):
		self.code = code

	def _get_discount_url(self) -> str:
		query = '?key=' + cfg.CONFIG_VOUCHER_KEY
		url = 'https://' + cfg.CONFIG_BASE_URL + cfg.CONFIG_VOUCHER_API.format(self.code) + query
		return url

	def get_discount(self) -> float:
		url = self._get_discount_url()
		try:
			resp = requests.get(url)
			if resp.status_code != 200:
				return 0
			return resp.json()['discount']
		except:
			return 0


