################################################################################
# SETUP CYTHON
################################################################################

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("supercell_cython.pyx", annotate = True))

################################################################################
# END
################################################################################
