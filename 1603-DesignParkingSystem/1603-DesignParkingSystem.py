class�ParkingSystem:

����def�__init__(self,�big:�int,�medium:�int,�small:�int):
��������self.parking�=�{1�:�big,�2�:�medium,�3�:�small}

����def�addCar(self,�carType:�int)�->�bool:


#�Your�ParkingSystem�object�will�be�instantiated�and�called�as�such:
#�obj�=�ParkingSystem(big,�medium,�small)

��������if�self.parking[carType]�>�0:�
������������self.parking[carType]�-=�1
������������return�True
��������return�False
������������
#�param_1�=�obj.addCar(carType)
[