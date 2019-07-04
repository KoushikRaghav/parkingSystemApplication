vehicleList = ["Car","Bike"]
class Floor:
	def __init__(self, floordata):
		self.floordata = floordata
		self.vehicles = []
	
	def addVehicles(self, vehicless):
		self.vehicles.append(vehicless)

	def showVehicles(self):
		return self.vehicles

	def getFloorData(self):
		return self.floordata

	def isVehicleAvailable(self, vehicleName):
		return True if self.floordata[vehicleName] > 0 else False	

def unparkVehicle(vehicledata):
	park = parkingData.getAllData()
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle Number: "))
	for floors in park:
		for vehicles in floors.showVehicles():
			if vehicles.getnumber() == getVehNum:
				print "\nYour vehicle is found in floor: {}".format(park.index(floors))
  				print "\n\tVehicle Type: {}".format(vehicles.getVType())
				print "\n\tVehicle Number: {}".format(vehicles.getnumber())
				print "\n\t!!! UNPARKED !!!"
				park[park.index(floors)].getFloorData()[vehicleList[vehicles.getVType()]]+= 1
				print park[park.index(floors)].getFloorData()[vehicleList[vehicles.getVType()]]

