class car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color 
        self.company = company
        self.model = model
        self.speed_limit = speed_limit
    def start(self):
        print("Start")
    def stop(self):
        print("Stop")
    def accelerate(self):
        print("Accelerating..")
    def changeGear(self):
        print("Changing Gears")
audi = car("A6","Red","Audi","80")
print(audi.start)