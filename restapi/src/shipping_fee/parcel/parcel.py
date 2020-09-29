from abc import abstractmethod, ABC
from shipping_fee.parcel.parcel_interface import IParcel
from shipping_fee.parcel.parcelcostrule import RejectParcel, HeavyParcel, SmallParcel, MediumParcel, LargeParcel


rules = [
	RejectParcel, 
	HeavyParcel, 
	SmallParcel, 
	MediumParcel, 
	LargeParcel
]

class Parcel(IParcel):

	def get_cost(self):
		for rule in rules:
			obj = rule(self.weight, self.height, self.width, self.length)
			if obj.check_condition():
				return obj.get_cost()

