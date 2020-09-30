from abc import abstractmethod
from shipping_fee.parcel.parcel_interface import IParcel


class IParcelCostRule(IParcel):

	@abstractmethod
	def get_cost(self) -> str:
		raise NotImplementedError

	@abstractmethod
	def check_condition(self) -> bool:
		raise NotImplementedError
