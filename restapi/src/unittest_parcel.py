import unittest
from shipping_fee.parcel.parcel import Parcel


class ParcelUnitTest(unittest.TestCase):

	def test_RejectParcel(self):
		parcel = Parcel(weight=51, height=1, width=1, length=1)
		self.assertEqual(parcel.get_cost(), "N/A")

	def test_HeavyParcel(self):
		parcel = Parcel(11, 1, 1, 1)
		self.assertEqual(parcel.get_cost(), "220")

	def test_SmallParcel(self):
		parcel = Parcel(1, 10, 10, 10)
		self.assertEqual(parcel.get_cost(), "30.0")

	def test_MediumParcel(self):
		parcel = Parcel(1, 20, 10, 10)
		self.assertEqual(parcel.get_cost(), "80.0")

	def test_LargeParcel(self):
		parcel = Parcel(1, 30, 10, 10)
		self.assertEqual(parcel.get_cost(), "150.0")


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(ParcelUnitTest)
	unittest.TextTestRunner(verbosity=2).run(suite)


