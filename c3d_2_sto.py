
tables = C3DFileAdapter.readFile(os.path.join(test_dir, 'walking2.c3d'), 1)
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
       
# Clean up.
os.remove(markersFilename)
os.remove(forcesFilename)