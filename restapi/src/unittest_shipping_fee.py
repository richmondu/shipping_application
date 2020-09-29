import unittest
from shipping_fee.shipping_fee import ShippingFee


class ShippingFeeUnitTest(unittest.TestCase):

	def test_RejectParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 51, 1, 1, 1)
		self.assertEqual(shipping.get_fee(), "N/A")

	def test_RejectParcel_GFI(self):
		shipping = ShippingFee("GFI", 51, 1, 1, 1)
		self.assertEqual(shipping.get_fee(), "N/A")

	def test_RejectParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 51, 1, 1, 1)
		self.assertEqual(shipping.get_fee(), "N/A")


	def test_HeavyParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 11, 1, 1, 1)
		self.assertEqual(shipping.get_fee(), "193.05")

	def test_HeavyParcel_GFI(self):
		shipping = ShippingFee("GFI", 11, 1, 1, 1)
		self.assertEqual(shipping.get_fee(), "203.5")

	def test_HeavyParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 11, 1, 1, 1)
		self.assertEqual(shipping.get_fee(), "220")


	def test_SmallParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 1, 10, 10, 10)
		self.assertEqual(shipping.get_fee(), "26.325")

	def test_SmallParcel_GFI(self):
		shipping = ShippingFee("GFI", 1, 10, 10, 10)
		self.assertEqual(shipping.get_fee(), "27.75")

	def test_SmallParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 1, 10, 10, 10)
		self.assertEqual(shipping.get_fee(), "30.0")


	def test_MediumParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 1, 20, 10, 10)
		self.assertEqual(shipping.get_fee(), "70.2")

	def test_MediumParcel_GFI(self):
		shipping = ShippingFee("GFI", 1, 20, 10, 10)
		self.assertEqual(shipping.get_fee(), "74.0")

	def test_MediumParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 1, 20, 10, 10)
		self.assertEqual(shipping.get_fee(), "80.0")


	def test_LargeParcel_MYNT(self):
		shipping = ShippingFee("MYNT", 1, 30, 10, 10)
		self.assertEqual(shipping.get_fee(), "131.625")

	def test_LargeParcel_GFI(self):
		shipping = ShippingFee("GFI", 1, 30, 10, 10)
		self.assertEqual(shipping.get_fee(), "138.75")

	def test_LargeParcel_skdlks(self):
		shipping = ShippingFee("skdlks", 1, 30, 10, 10)
		self.assertEqual(shipping.get_fee(), "150.0")


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(ShippingFeeUnitTest)
	unittest.TextTestRunner(verbosity=2).run(suite)








