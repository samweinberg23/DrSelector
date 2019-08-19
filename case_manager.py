from doctor import Doctor
import heapq

class CaseManager:
	def __init__(self):
		self.casePair = {}
		self.typePicker = {}
	
	def addDoctor(self, val, name):
		self.typePicker[val] = self.typePicker.get(val, set()).add(Doctor(name))

	def removeCase(self, type, id):
		if id not in self.casePair:
			return
		doctor = self.casePair[id]
		filtered = fiter(lambda x : x.name == doctor, self.typePicker[type])
		if filtered:
			filtered[0].cases -= 1
		self.typePicker.add(filtered[0])
	
	def addCase(self, type, id):
		doctor = heapq.nsmallest(1, self.typePicker[type], key = lambda x : x.cases)[0]
		self.casePair[id] = doctor.name
		doctor.self.cases += 1
		self.typePicker[type].add(doctor)
