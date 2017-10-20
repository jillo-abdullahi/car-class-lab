class Car(object):
	"""Boiler plate for a car class"""
	def __init__(self,name="General",model="GM",type_="saloon"):
		self.num_of_doors = 4
		self.num_of_wheels = 4
		self.speed = 0
		self.name = name
		self.model = model
		self.type_ = type_

		#Override the class variable num_of_doors based on name of car
		if self.name == "Porshe" or self.name == "Koenigsegg":
			self.num_of_doors = 2

		#Override the class variable num_of_wheels based on type of car
		if self.type_ == "trailer":
			self.num_of_wheels = 8

	#Method to check if type of car is a saloon. Return false if it is not
	def is_saloon(self):
		if self.type_ != 'saloon':
			return False
		return True
		
	#Driving your car
	def drive(self,car_speed):
		if car_speed == 3:
			self.speed = 1000
			return self
		elif car_speed == 7:
			self.speed = 77
			return self
		return self






