"""
Script to move image files.
"""

import shutil
import os


for i in range(1, 11):
    cmdname = f"manim -s -r 500,281 step{i}.py"
    os.system(cmdname)
    srcname = f"media/images/step{i}/Step{i}_ManimCE_v0.16.0.post0.png"
    dstname = f"../../images/two_pointer/step{i}.png"
    shutil.copyfile(srcname, dstname)
