from abc import abstractmethod, ABC
from shipping_fee.parcel.parcel_interface import IParcel


class IParcelCostRule(IParcel):

	@abstractmethod
	def get_cost(self) -> str:
		raise NotImplementedError

	@abstractmethod
	def check_condition(self):
		raise NotImplementedError
