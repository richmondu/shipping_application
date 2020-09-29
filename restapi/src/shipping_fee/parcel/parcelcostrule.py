from shipping_fee.parcel.parcelcostrule_interface import IParcelCostRule


class RejectParcel(IParcelCostRule):

	def get_cost(self) -> str:
		return "N/A"

	def check_condition(self) -> bool:
		return self.weight > 50


class HeavyParcel(IParcelCostRule):

	def get_cost(self) -> str:
		return str(20 * self.weight)

	def check_condition(self) -> bool:
		return self.weight > 10


class SmallParcel(IParcelCostRule):

	def get_cost(self) -> str:
		return str(0.03 * self.get_volume())

	def check_condition(self) -> bool:
		return self.get_volume() < 1500


class MediumParcel(IParcelCostRule):

	def get_cost(self) -> str:
		return str(0.04 * self.get_volume())

	def check_condition(self) -> bool:
		return self.get_volume() < 2500


class LargeParcel(IParcelCostRule):

	def get_cost(self) -> str:
		return str(0.05 * self.get_volume())

	def check_condition(self) -> bool:
		return True