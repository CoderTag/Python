# find 5 oldest file in directory and subdiretory
import os
#from collections import defaultdict

# #From CMD line
# $ find . -printf '%T+ + %p\n' | sort | head -5
# 2003-06-19+12:05:04.0000000000 + ./.wine/drive_c/windows/syswow64/mspatcha.dll
# 2011-06-11+01:58:52.0000000000 + ./.wine/drive_c/windows/syswow64/msvcp100.dll
# 2011-06-11+01:58:52.0000000000 + ./.wine/drive_c/windows/syswow64/msvcr100.dll
# 2012-09-20+00:00:00.0000000000 + ./.local/share/Trash/files/OFL.txt
# 2012-09-20+00:00:00.0000000000 + ./.local/share/Trash/files/SourceCodePro-Black.ttf




p = '/home/kaushik'
#d = defaultdict(lambda: 'Nothing')
d = {}


def list_directory(p):
    try:
        for li in os.listdir(p):
            file = os.path.join(p, li)
            if os.path.isfile(file):
                create_time = os.path.getctime(file)
                d[create_time] = file
            else:
                if os.path.isdir(file):
                    list_directory(file)

    except (PermissionError, OSError) as e:
        return 1
    except Exception as e:
        print(e)


if os.path.isdir(p):
    list_directory(p)
    print(d)
