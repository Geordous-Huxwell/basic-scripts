class TV():
	'''
	Author:
	Mod Date:
	Abstract:
	'''

	def __init__(self, size, res, make, model, inputOptions, output, isOn, currentInput, currentBrightness, currentVolume):
		self.size = size
		self.res = res
		self.make = make
		self.model = model
		self.inputOptions = inputOptions
		self.isOn = isOn
		self.output = output
		self.currentInput = currentInput
		self.currentBrightness = currentBrightness
		self.currentVolume = currentVolume


	def togglePower(self, isOn):
		if self.isOn == False:
			self.isOn = True
		else:
			self.isOn = False

	def changeInput(self, newInput):
		self.currentInput = newInput

	def adjustBrightness(self, newBrightness):
		self.currentBrightness = newBrightness

	def adjustVolume(self, newVolume):
		self.currentVolume = newVolume


	
