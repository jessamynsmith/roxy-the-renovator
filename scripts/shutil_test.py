import os
import shutil
import sys
import tempfile
# import easygui
import platform

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


knOsVerison=platform.system()
                #knOsVerison=os.name
print(knOsVerison + 'knknknknknknknknknknknknknknknknknknknknknkn')
print('temp dir')
print(resource_path('/temp'))
if(knOsVerison=="Darwin"):
    iOSPath='/Users/jessamyn/Documents/shutil_test'
    # iOSPath='/Users/Shared/immersiveED'
    def copytree(src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)




    if os.path.exists(iOSPath):
        print("its already there!")
        shutil.rmtree(iOSPath)
        os.mkdir(iOSPath)
        knPath=os.path.exists(iOSPath)
        knSrc='/Users/Jessamyn/Documents/avatars'
        copytree(knSrc, iOSPath, symlinks=True)
        #knRmTree(knPath)
        #copytree(knSrc, iOSPath, symlinks=True)
        #easygui.msgbox("The immersiveED Software is already installed!", title="ed installed")
    else:
        print("its been made!")
        os.mkdir(iOSPath)
        knPath=os.path.exists(iOSPath)
        knSrc='/Users/Jessamyn/Documents/avatars'
        copytree(knSrc, iOSPath, symlinks=True)

    userhome = os.path.expanduser('~')
    print (userhome)
    # knScriptDicPath= userhome + '/Library/Preferences/Autodesk/maya/scripts'
    # knScriptSrc='/Users/Jessamyn/Documents/avatars'
    # copytree(knScriptSrc, knScriptDicPath, symlinks=True)

    # knShelfPath= userhome + '/Library/Preferences/Autodesk/maya/2016/prefs/shelves'
    # knShelfSrc='2016_MAC/immersiveED/icons'
    # copytree(knShelfSrc, knShelfPath, symlinks=True)


    knModDicPath= userhome + '/Library/Preferences/Autodesk/maya/2016/modules'
    if os.path.exists(knModDicPath):
        knModSrc='2016_MAC/immersiveED/modules'
        copytree(knModSrc, knModDicPath, symlinks=True)
        knModSrc='2016_MAC/immersiveED/modules'
        copytree(knModSrc, knModDicPath, symlinks=True)
        #easygui.msgbox("The immersiveED Software is done installing. Please open maya and look for the tab", title="ed installed done")
    else:
        os.mkdir(knModDicPath)
        knModSrc='2016_MAC/immersiveED/modules'
        copytree(knModSrc, knModDicPath, symlinks=True)
        knModSrc='2016_MAC/immersiveED/modules'
        copytree(knModSrc, knModDicPath, symlinks=True)
        #easygui.msgbox("The immersiveED Software is done installing. Please open maya and look for the tab", title="ed installed done")
    # easygui.msgbox("The immersiveED Software is done installing. Please open maya and look for the tab", title="ed installed done")






    '''
    os.mkdir(iOSPath)
    knPath=os.path.exists(iOSPath)
    knSrc='2016_MAC/immersiveED'
    copytree(knSrc, iOSPath, symlinks=True)


    knUserName=os.getenv('USERNAME')
    print (knUserName)
    '''
else:
    #pcside
    iOSPath='C:\\Users\\Public\\immersiveED\\'
    def copytree(src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)




    if os.path.exists(iOSPath):
        print("its already there!")
        shutil.rmtree(iOSPath)
        os.mkdir(iOSPath)
        knPath=os.path.exists(iOSPath)
        knSrc=resource_path('2016_MAC\\immersiveED')
        copytree(knSrc, iOSPath, symlinks=True)

        #knRmTree(knPath)
        #copytree(knSrc, iOSPath, symlinks=True)
        #easygui.msgbox("The immersiveED Software is already installed!", title="ed installed")
    else:
        print("its been made!")
        os.mkdir(iOSPath)
        knPath=os.path.exists(iOSPath)
        knSrc=resource_path('2016_MAC\\immersiveED')
        copytree(knSrc, iOSPath, symlinks=True)

    userhome = os.path.expanduser('~')

    knScriptDicPath= userhome + '\\Documents\\maya\\scripts'
    knScriptSrc=resource_path('2016_MAC\\immersiveED\\Scripts')
    copytree(knScriptSrc, knScriptDicPath, symlinks=True)
    knNum=str(2016)
    knShelfPath= userhome + "\\Documents\\maya\\2016\\prefs\\shelves\\"
    knShelfSrc=resource_path('2016_MAC\\immersiveED\\shelves')
    copytree(knShelfSrc, knShelfPath, symlinks=True)

    knIconPath= userhome + "\\Documents\\maya\\2016\\prefs\\icons\\"
    knIconSrc=resource_path('2016_MAC\\immersiveED\\icons')
    copytree(knIconSrc, knIconPath, symlinks=True)

    knModDicPath= userhome + "\\Documents\\maya\\2016\\modules"
    if os.path.exists(knModDicPath):
        knModSrc=resource_path('2016_MAC\\immersiveED\\modules')
        copytree(knModSrc, knModDicPath, symlinks=True)
        knModSrc=resource_path('2016_MAC\\immersiveED\\modules')
        copytree(knModSrc, knModDicPath, symlinks=True)
        #easygui.msgbox("The immersiveED Software is done installing. Please open maya and look for the tab", title="ed installed done")
    else:
        os.mkdir(knModDicPath)
        knModSrc=resource_path('2016_MAC\\immersiveED\\modules')
        copytree(knModSrc, knModDicPath, symlinks=True)
        knModSrc=resource_path('2016_MAC\\immersiveED\\modules')
        copytree(knModSrc, knModDicPath, symlinks=True)
        #easygui.msgbox("The immersiveED Software is done installing. Please open maya and look for the tab", title="ed installed done")
    # easygui.msgbox("The immersiveED Software is done installing. Please open maya and look for the tab", title="ed installed done")






    '''
    os.mkdir(iOSPath)
    knPath=os.path.exists(iOSPath)
    knSrc='2016_MAC/immersiveED'
    copytree(knSrc, iOSPath, symlinks=True)


    knUserName=os.getenv('USERNAME')
    print (knUserName)
    '''
