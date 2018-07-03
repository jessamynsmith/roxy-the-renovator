import sys, os
import shutil

sourcepath="D:\Data\MP-PO-to-QB\NEWXMLS"

for filename in os.listdir(sourcepath):
    current_file=os.path.join(sourcepath, filename)
    dst="D:\Data\MP-PO-to-QB\CONVERTED"
    shutil.move(current_file, dst)
