import unittest
from shipping_fee.shipping.shipping_fee import ShippingFee
from shipping_fee.shipping.response import ShippingFeeResponse


class ShippingFeeUnitTest(unittest.TestCase):

	def test_RejectParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 51, 1, 1, 1)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("N/A", "N/A", "N/A"))

	def test_RejectParcel_GFI(self):
		shipping = ShippingFee("GFI", 51, 1, 1, 1)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("N/A", "N/A", "N/A"))

	def test_RejectParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 51, 1, 1, 1)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("N/A", "N/A", "N/A"))


	def test_HeavyParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 11, 1, 1, 1)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("193.05", "12.25%", "220"))

	def test_HeavyParcel_GFI(self):
		shipping = ShippingFee("GFI", 11, 1, 1, 1)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("203.5", "7.5%", "220"))

	def test_HeavyParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 11, 1, 1, 1)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("220", "0%", "220"))


	def test_SmallParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 1, 10, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("26.325", "12.25%", "30.0"))

	def test_SmallParcel_GFI(self):
		shipping = ShippingFee("GFI", 1, 10, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("27.75", "7.5%", "30.0"))

	def test_SmallParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 1, 10, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("30.0", "0%", "30.0"))


	def test_MediumParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 1, 20, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("70.2", "12.25%", "80.0"))

	def test_MediumParcel_GFI(self):
		shipping = ShippingFee("GFI", 1, 20, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("74.0", "7.5%", "80.0"))

	def test_MediumParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 1, 20, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("80.0", "0%", "80.0"))


	def test_LargeParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 1, 30, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("131.625", "12.25%", "150.0"))

	def test_LargeParcel_GFI(self):
		shipping = ShippingFee("GFI", 1, 30, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("138.75", "7.5%", "150.0"))

	def test_LargeParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 1, 30, 10, 10)
		self.assertEqual(ShippingFeeResponse(shipping).get(), ("150.0", "0%", "150.0"))


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(ShippingFeeUnitTest)
	unittest.TextTestRunner(verbosity=2).run(suite)








