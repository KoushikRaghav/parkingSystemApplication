floorData = []
floorObject = 0
vehicleType = 0
numOfFloors = 2
parkingData = []	
vehicleList = ["Car","Bike"]

class Floor:
	def __init__(self, floordata):
		self.floordata = floordata
		self.vehicle = []
		self.Floor = []

	def addfloor(self, Floor):
		self.Floor.append(Floor)

	def showfloor(self):
		return self.Floor	

	def addVehicles(self, vehicless):
		self.vehicle.append(vehicless)
	
	def showVehicles(self):
		return self.vehicle

	def getFloorData(self):
		return self.floordata

	def isVehicleAvailable(self, vehicleName):
		return True if self.floordata[vehicleName] > 0 else False	
		
class Parking:
	def __init__(self):
		self.data = []
	
	def addFloorData(self, floors):
		self.data.append(floors)
	
	def getAllData(self):
		return self.data

class Vehicle:
	def __init__(self,vType,VNumber):
		self.VType = vType
		self.Vnumber = VNumber

	def getVType(self):
		return self.VType

	def getnumber(self):
		return self.Vnumber

def unparkVehicle(vehicledata):
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle Number: "))
	for i in range(len(floorObject.showVehicles())):
		if floorObject.showVehicles()[i].getnumber() == getVehNum:
			print "\nYour vehicle is found in floor: {}".format(floorObject.showfloor()[i])
			print "\n\tVehicle Type: {}".format(vehicleList[floorObject.showVehicles()[i].getVType()])
			print "\n\tVehicle Number: {}".format(floorObject.showVehicles()[i].getnumber())
			floorData[floorObject.showfloor()[i]].getFloorData()[vehicleList[floorObject.showVehicles()[i].getVType()]] += 1
			print floorData[floorObject.showfloor()[i]].getFloorData()[vehicleList[floorObject.showVehicles()[i].getVType()]]
			print "\n\t!!! UNPARKED !!!"
				
def parkVehicle(floorNum,vehicleData):
	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getnumber())
	print "\n\tFloor: {}".format(floorNum)	
	floorData[floorNum].getFloorData()[vehicleList[vehicleType]] -= 1
	print "\n\t!!! PARKED !!!", floorData[floorNum].getFloorData()[vehicleList[vehicleType]]
	
def searchForAvailableFloors():
	print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
	for i in range(2):
		if floorData[i].isVehicleAvailable(vehicleList[vehicleType]) == True:
			print "Floor {} --> AVAILABLE\n\t".format(i)  
		else:
			print "\t"	
	floorNum = int(input("Enter the floorNum: "))
	floorObject.addfloor(floorNum)
	return floorNum

def getVehicleData():
	global vehicleType
	print "\n<--- VEHICLE PARKING --->\n\nEnter Vehicle Type:\n"
	for vehicles in vehicleList:
		print "{}. {}".format(vehicleList.index(vehicles),vehicles)
	vehicleType = int(input("\n"))
	if vehicleType < len(vehicleList):
		number = int(input("\n\nEnter Vehicle Number: "))	
		vehicleData = Vehicle(vehicleType,number)
		import pdb;pdb.set_trace();
		floorObject.addVehicles(Vehicle(vehicleType,number))
		return vehicleData
	else:
		print "Enter the vehicle type correctly"

def displayVehicleData():
	# import pdb; pdb.set_trace()
	for vehicles in range(len(floorData)):	
		print "\n {}\t{} ".format(vehicles,str(parkingData.getAllData()[vehicles].getFloorData()).replace("{","").replace("}", ""))
		
def enterVehicleData():
	global numOfFloors,floorData,parkingData,floorObject
	print "\n<--- ENTER VEHICLE DATA --->"
	parkingData = Parking()
	for numOfFloors in range(2):
		vehicleDict = {}
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the Number of vehicles: "))
		totalvehicles = 0
		for vehicles in vehicleList:
			vehicleDict[vehicles] = int(input("\n\t {}: ".format(vehicles)))
			totalvehicles += vehicleDict[vehicles]		
		if totalvehicles == vehicleLimit:
			floorObject = Floor(vehicleDict)
			floorData.append(floorObject)
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break
		parkingData.addFloorData(floorObject)

def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Data\n5. Exit\n\n"))
	return option

def main():
	global numOfFloors
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			enterVehicleData()		
		elif option == 2:
			vehicledata = getVehicleData()	
			floorNum = searchForAvailableFloors() 
			parkVehicle(floorNum,vehicledata) if floorNum <= numOfFloors else "\nPARKING IS FULL IN FLOOR {}".format(floorNum)
		elif option == 3:
			unparkVehicle(vehicledata)
		elif option == 4:
			displayVehicleData()
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()