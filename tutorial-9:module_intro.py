# while importing module python looks for sys.path. If module define there it import from there
import sys
print(sys.path)

# if module is there in other path we can add that path in sys.path before importing it e.g
# sys.path.append('/usr/home')
# If there are too many other directory like this .. code might get clutter with hard coded path
# other way to include path in 'PYTHONPATH' variable in .bash_profile
# export PYTHONPATH="/usr/home"

import antigravity



