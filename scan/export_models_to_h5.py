from ghost_scan.constants import dirpath

from .remove_background.model import getModel as getModel1
from .detect_pose.model import getModel as getModel2
from .finetune_positions.model import getModel as getModel3

model1 = getModel1('%s/scan/models/weights/remove_background/weights' % dirpath)
model1.save('%s/scan/models/h5/remove_background.h5' % dirpath)
model2 = getModel2('%s/scan/models/weights/detect_pose/weights' % dirpath)
model2.save('%s/scan/models/h5/detect_pose.h5' % dirpath)
model3 = getModel3('%s/scan/models/weights/finetune_positions/weights' % dirpath)
model3.save('%s/scan/models/h5/finetune_positions.h5' % dirpath)
