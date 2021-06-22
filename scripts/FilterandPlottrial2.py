import re 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

class GcodeReader:

    def __init__(self):
        self.filepath = '../tool-path.gcode'
        self.listX = []
        self.listY = []
        self.listZ = []
        self.Z_updated = False
        self.extract_XYZ()
        

    def extract_XYZ(self):
        with open(self.filepath) as gcode:
            for line in gcode:
                line = line.strip()
                coordX = re.findall(r'[X].?\d+.\d+|[X].?\d\d', line)
                coordY = re.findall(r'[Y].?\d+.\d+|[Y].?\d\d', line)
                coordZ = re.findall(r'[Z].?\d+.\d+|[Z].?\d\d', line)
                if coordX:
                    valueX = "{}".format(coordX[0])
                    self.listX.append(float(valueX[1:]))
                    ## add value for Z
                    if coordZ:
                        valueZ = "{}".format(coordZ[0])
                        valueZ = valueZ[1:]
                        self.Z_updated = True
                    elif self.Z_updated: 
                        valueZ = valueZ
                    else: 
                        valueZ = 0.0
                    self.listZ.append(float(valueZ))
                if coordY:
                    valueY = "{}".format(coordY[0])
                    self.listY.append(float(valueY[1:]))

                
                    
        print(np.array(self.listX))
        self.plot_XYZ_coordinates()
  

    def plot_XYZ_coordinates(self):
        fig = plt.figure()
        ax = plt.axes(projection ='3d')
        ax.plot3D(np.array(self.listX), np.array(self.listY), np.array(self.listZ), 'green')
        plt.show()
            

if __name__ == '__main__':
    
    GcodeReader()

    exit()


# with open(self.filepath) as gcode:
#             for line in gcode:
#                 line = line.strip()
#                 coord = re.findall(r'[XYZ].?\d+.\d+', line)
#                 if coord: 
#                     valueX = "{}".format(coord[0]) 
#                     print("VALUE of X is ", valueX[:])
#                 if coord: 
#                     valueY = "{}".format(coord[1]) 
#                     print("VALUE of Y is ", valueY[:])
#                 # if coord: 
#                 #     valueZ = "{}".format(coord[2]) 
#                 #     print("VALUE of Z is ", valueZ[:])