class Circulo:
    def __init__(self, cx, cy, radio):
        self.cx = cx
        self.cy = cy
        self.radio = radio

    def getCx(self):
        return self.cx
    
    def getCy(self):
        return self.cy
    
    def getRadio(self):
        return self.radio
    
    def setCx(self, cx):
        if cx is None or cx is not isinstance(int):
            cx = 0
        else:
            self.cx = cx

    def setCy(self, cy):
        if cy is None or cy is not isinstance(int):
            cy = 0
        else:
            self.cy = cy

    def setRadio(self, radio):
        if radio is None or radio is not isinstance(float):
            radio = 1.0
        else:
            self.radio = radio

    #Devuelve una representacion textual del objeto
    def toString(self):
        return "(", self.cx, " ", self.getCy(), " ", self.getRadio(), ")"
    

c1 = Circulo(2, 2, 2.0)
print("c1:", c1.toString())