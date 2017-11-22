#------------------------------------------------------------------------------
# cuadruplo.py
# un objeto que guarda 5 valores
# 1- el indice del cuadruplo
# 2- la accion del cuadruplo
# 3- primer argumento
# 4- segundo argumento
# 5- tercer argumento
#------------------------------------------------------------------------------


class cuadruplo:
    def __init__(self, dir, accion, arg1, arg2, arg3):
        self.dir = dir
        self.accion = accion
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __str__(self):
        return str(self.dir) + "\t" + str(self.accion) + "\t" + str(self.arg1) + "\t" + str(self.arg2) + "\t" + str(self.arg3)
