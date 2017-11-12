class cuadruplo:
    def __init__(self, dir, accion, arg1, arg2, arg3):
        self.dir = dir
        self.accion = accion
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __str__(self):
        return str(self.accion) + "\t" + str(self.arg1) + "\t" + str(self.arg2) + "\t" + str(self.arg3)
