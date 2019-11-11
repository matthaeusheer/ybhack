#########################################################################################
#                                                                                       #
#   Common variables like the repo's root path or data dir path are defined in here     #
#   for convenient use within the ybhack repo, e.g.                                     #
#                                                                                       #
#   from ybhack.common import DATA_DIR_PATH                                             #
#                                                                                       #
#########################################################################################

import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_DIR_PATH = os.path.join(PROJECT_ROOT_PATH, 'data')
