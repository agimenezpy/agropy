# initialization
from six import print_
import sys
from os import path as pth, getcwd

work_dir = pth.dirname(getcwd())
root_dir = pth.dirname(work_dir)

print_('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([work_dir, root_dir + '/climatepy'])