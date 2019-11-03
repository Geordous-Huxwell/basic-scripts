from TV import TV

testTV = TV(80, "1080p", "Samsung", "tv", ["HDMI 1", "HDMI 2", "Component"], "Optical Audio", False, "HDMI 1", 0.5, 0.5)

print(getattr(testTV, "make"))
setattr(testTV, "make", "LG")
print(getattr(testTV, "make"))


print(getattr(testTV, "isOn"))
testTV.togglePower("isOn")
print(getattr(testTV, "isOn"))