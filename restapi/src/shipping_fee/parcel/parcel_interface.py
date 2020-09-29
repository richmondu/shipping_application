from abc import abstractmethod, ABC


class IParcel(ABC):

	def __init__(self, weight: float, height: float, width: float, length: float):
		self.weight = weight # kg
		self.height = height # cm
		self.width  = width  # cm
		self.length = length # cm

	def get_volume(self):
		return self.height * self.width * self.length # cm3

	@abstractmethod
	def get_cost(self):
		raise NotImplementedError