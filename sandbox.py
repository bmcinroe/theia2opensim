from theia2opensim.utilities import C3D
import ezc3d
import opensim as osim

data_path = '/home/ben/theia2opensim/data/trial1/pose_0.c3d'

c3d = C3D(data_path)

x = c3d.get_data('rotations')

print(x.shape)

breakpoint()



table = c3d.get_positions_table()

print(table.getColumnLabels())


model = osim.Model('unscaled_generic.osim')
model.initSystem()

