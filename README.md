# c3d_2_sto
 c3d file converter for OpenSIMtk markers and forces

#Issues:

- The OpenSim C3DFileAdapter() only supports Type-2 (AMTI & Bertec) forceplates. If you have C3D files having other forceplate types, particularly Kistler forceplates, please consider donating these files to the OpenSim project (email: opensim@stanford.edu)
- If you have NaNs in your forces (.mot) file, the IDTool will generate all NaNs for the joint torques. The current workaround is to delete any time frames where there is an offending NaN. (forum post)

#Prerequisites:

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