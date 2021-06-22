import re 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

class GcodeReader:

    def __init__(self):
        self.filepath = '../Tablet_-graphic-_Holder__v1_GCODE.gcode'

        listX, listY, listZ = self.extract_XYZ()
        self.plot_XYZ_coordinates(listX, listY, listZ )

    def extract_XYZ(self):
        listX = []
        listY = []
        listZ = []
        valueZ = 0.0
        with open(self.filepath) as Gcode:
            for line in Gcode:
                line = line.strip()
                coordinatesX = re.findall(r'[X].?\d+.\d+|[X].?\d\d', line)
                coordinatesY = re.findall(r'[Y].?\d+.\d+|[Y].?\d\d', line)
                coordinatesZ = re.findall(r'[Z].?\d+.\d+|[Z].?\d\d', line)
                if coordinatesX:
                    valueX = "{}".format(coordinatesX[0])
                    listX.append(float(valueX[1:]))
                    listZ.append(float(valueZ))
                if coordinatesY:
                    valueY = "{}".format(coordinatesY[0])
                    listY.append(float(valueY[1:]))   
                if coordinatesZ:
                    valueZ = "{}".format(coordinatesZ[0])
                    valueZ = valueZ[1:]
        print(len(listX), len(listY), len(listZ))
        print(listY)
        return listX, listY, listZ

    def plot_XYZ_coordinates(self, listX, listY, listZ ):
        fig = plt.figure()
        ax = plt.axes(projection ='3d')
        ax.plot3D(np.array(listX), np.array(listY), np.array(listZ), 'blue')
        plt.show()
            

if __name__ == '__main__':
    GcodeReader()

    exit()

