import os,sys

directory = ""
def matchName(name, dir_list):
    # make the name and list to lower then compare
    appName = []
    for in_dir_name in dir_list:
        temp_name = in_dir_name.split(".exe")[0]
        if temp_name.lower() in name.lower():
            appName.append(in_dir_name)
    if len(appName) > 1:
        return sizeFilter(appName)
    else:
        return appName[0]

def sizeFilter(name_list):
    # return the name with max size
    appNsize = ["", 0]
    for appName in name_list:
        temp_size = os.stat(directory + appName).st_size
        if appNsize[1] < temp_size:
            appNsize[0] = appName
            appNsize[1] = temp_size
    return appNsize[0]

def listTheDirectory():
    global directory
    all_files = os.listdir(directory)
    exe_list = []
    for fil in all_files:
        if os.path.isfile(directory + fil) and fil.find(".exe") > -1:
            #index_exe = fil.find(".exe")
            exe_list.append(fil)
    return exe_list

def openApplication(name, dir):
    global directory
    directory = dir
    dir_list = listTheDirectory()
    #print(dir_list)
    if len(dir_list) < 1:
        print("No executables found in directory.")
        sys.exit(-1)
    appName = matchName(name, dir_list)
    print("Opening ->",appName)
    os.system('"' + directory + appName + '"')
    #print("Application closed.")
