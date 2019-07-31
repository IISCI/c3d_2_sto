"""
Issues:

- The OpenSim C3DFileAdapter() only supports Type-2 (AMTI & Bertec) forceplates. If you have C3D files having other forceplate types, particularly Kistler forceplates, please consider donating these files to the OpenSim project (email: opensim@stanford.edu)
- If you have NaNs in your forces (.mot) file, the IDTool will generate all NaNs for the joint torques. The current workaround is to delete any time frames where there is an offending NaN. (forum post)

Prerequisites:

Note on Python 2.7.x vs Python 3
The Python package that comes with the OpenSim GUI distribution will only work with Python 2.7.x. For Python 3, you must build the OpenSim API (opensim-core) from scratch and set the CMake variable OPENSIM_PYTHON_VERSION to 3.

Install Python setuptools, Numpy, SciPy separately or Anaconda package

Insert OpenSim into the System Path

Edit your Path environment variable to include <OPENSIM_INSTALL_DIRECTORY>\bin is in system variables Path, where OPENSIM_INSTALL_DIRECTORY is the directory where you installed the current version of OpenSim (e.g. C:\OpenSim 4.0). Delete any other OpenSim Path entries

Run the Setup File from Command Line

Open an Anaconda Command Prompt (type anaconda into the Windows Start menu). Navigate to the OpenSim Installation folder and find the subfolder sdk which contains the script setup.py.

cd C:\OpenSim 4.0\sdk\Python
Run the python script by typing:

python setup.py install
This will copy the required files and folders into the Anaconda directory.

Test Installation

Start the Spyder integrated development environment, installed by Anaconda, by typing spyder into the Windows Start menu. Run the following in the interpreter that appears within Spyder:

import opensim

If there is no error, then the installation worked.
"""

import os, unittest
import opensim as osim

#originally there were no osim class prefix (fixed)
#Signature: osim.C3DFileAdapter.readFile(fileName)
#Docstring:
#readFile(std::string const & fileName) -> StdMapStringAbstractDataTable
#removing second parameter (1) - fixed
tables = osim.C3DFileAdapter.readFile(os.path.join(test_dir, 'walking2.c3d'))
markers = tables['markers']
forces = tables['forces']
  
# Marker data read from C3D.
markers = tables['markers']
       
# Flatten marker data.
markersFlat = markers.flatten()

"""
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-45-c6e0720d2aee> in <module>()
     42 
     43 # Flatten marker data.
---> 44 markersFlat = markers.flatten()
     45 
     46 # Make sure flattenned marker data is writable/readable to/from file.

C:\ProgramData\Anaconda2\lib\site-packages\opensim-4.0-py2.7.egg\opensim\common.pyc in <lambda>(self, name)
  22211     __setattr__ = lambda self, name, value: _swig_setattr(self, AbstractDataTable, name, value)
  22212     __swig_getmethods__ = {}
> 22213     __getattr__ = lambda self, name: _swig_getattr(self, AbstractDataTable, name)
  22214 
  22215     def __init__(self, *args, **kwargs):

C:\ProgramData\Anaconda2\lib\site-packages\opensim-4.0-py2.7.egg\opensim\common.pyc in _swig_getattr(self, class_type, name)
     78     if method:
     79         return method(self)
---> 80     raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))
     81 
     82 

AttributeError: 'AbstractDataTable' object has no attribute 'flatten'
"""
       
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