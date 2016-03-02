'''
删除指定的目录下面的所有文件和文件夹
'''
import os
import shutil
from ensurepip import __main__

def CleanDir(dir):
    if os.path.isdir(dir):
        print 'clean dir:\t' + dir
        paths = os.listdir(dir)
        for path in paths:
            filePath = os.path.join(dir, path)
            if os.path.isfile(filePath):
                try:
                    os.remove(filePath)
                except os.error:
                    autoRun.exception('remove %s error!' % filePath)
            elif os.path.isdir(filePath):
                if filePath[-4:].lower() == '.svn'.lower():
                    continue
                shutil.rmtree(filePath, True)

if __name__ == '__main__':
    #dir = r'E:\github\read_excel\b' + '\\'
    dir = r'E:\github\read_excel\a'  #加不加最后的\没区别
    CleanDir(dir)