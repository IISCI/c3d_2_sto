#added import of neccessary classes statements
import os
import opensim as osim

#FIX! Originally there were no osim class prefix
#FIX! Change fileRead() from paerent class FileAdapter to read() from C3DFileAdpter class

tables = osim.C3DFileAdapter().read(os.path.join(test_dir, 'walking5.c3d'), 0)
markers = tables['markers']
forces = tables['forces']
  
# Marker data read from C3D.
markers = tables['markers']
       
# Flatten marker data.
markersFlat = markers.flatten()
       
# Make sure flattenned marker data is writable/readable to/from file.

markersFilename = 'markers.sto'
stoAdapter = osim.STOFileAdapter()
stoAdapter.write(markersFlat, markersFilename)
markersDouble = stoAdapter.read(markersFilename)
       
# Forces data read from C3d.
forces = tables['forces']
fpCalMats = forces.getTableMetaDataVectorMatrix("CalibrationMatrices")
fpCorners = forces.getTableMetaDataVectorMatrix("Corners")
fpOrigins = forces.getTableMetaDataVectorMatrix("Origins")
       
# Flatten forces data.
forcesFlat = forces.flatten()
       
# Make sure flattenned forces data is writable/readable to/from file.
forcesFilename = 'forces.sto'
stoAdapter.write(forcesFlat, forcesFilename)
forcesDouble = stoAdapter.read(forcesFilename)
       
# Clean up if necessary - uncomment two rows below or leave it commented to preserve data files
# os.remove(markersFilename)
# os.remove(forcesFilename)