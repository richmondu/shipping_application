import unittest
from shipping_fee.discount.voucher import Voucher


class VoucherUnitTest(unittest.TestCase):

	def test_MYNT(self):
		voucher = Voucher("MYNT")
		self.assertEqual(voucher.get_discount(), 12.25)

	def test_GFI(self):
		voucher = Voucher("GFI")
		self.assertEqual(voucher.get_discount(), 7.5)

	def test_skdlks(self):
		voucher = Voucher("skdlks")
		self.assertEqual(voucher.get_discount(), 0)

	def test_random(self):
		voucher = Voucher("random1234")
		self.assertEqual(voucher.get_discount(), 0)


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(VoucherUnitTest)
	unittest.TextTestRunner(verbosity=2).run(suite)