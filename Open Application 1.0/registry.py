import os, winreg

# List of keys where the applications could be located
sub_key = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall", r"SOFTWARE\Microsoft"]

application_names = []
application_dirs = []

def addName(key): # Find the actual name of the application
    application_name = ""
    try:
        application_name, reg_type = winreg.QueryValueEx(key, "DisplayName")
        
        return [True, application_name]
    except:
        pass
    return [False]
    

def addDir(key): # Find the directory of the application
    dir_list = ["InstallLocation", "DisplayIcon", "UninstallString"]
    try:
        dir_name, reg_type = winreg.QueryValueEx(key, dir_list[0])
        if dir_name.find('"') > -1:
            dir_name = dir_name.replace('"', "")
    except Exception as e:
        #print(e)
        try:
            
            dir_name, reg_type = winreg.QueryValueEx(key, dir_list[1])
            if dir_name.find('"') > -1:
                dir_name = dir_name.replace('"',"")
            index = 0
            i = 0
            temp_dir = dir_name
            while temp_dir.find("\\") > -1:
                index = temp_dir.find("\\")
                temp_dir = temp_dir[index + 1:]
                i += index + 1
            dir_name = dir_name[:i]
            
        except Exception as e:
            #print(e)
            try:
                
                dir_name, reg_type = winreg.QueryValueEx(key, dir_list[2])
                if dir_name.find('"') > -1:
                    dir_name = dir_name.replace('"', "")
                index = 0
                i = 0
                temp_dir = dir_name
                while temp_dir.find("\\") > -1:
                    index = temp_dir.find("\\")
                    temp_dir = temp_dir[index + 1:]
                    i += index + 1
                dir_name = dir_name[:i]
                
            except Exception as e:
                #print(e)
                dir_name = ""
    
    if len(dir_name) > 0:
        return [True, dir_name]
    return [False]
                


def getAllAplications():
    for sub_ in sub_key:
        # Get the Key
        print("KEY: {}".format(sub_))
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_, 0, winreg.KEY_READ)
        # Read the sub keys
        index = 0
        while True:
            try:
                name = winreg.EnumKey(registry_key, index)
                #print(name)
                new_path = sub_ + '\\' + name
                new_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, new_path, 0, winreg.KEY_READ)
                
                hasName = addName(new_key)
                if hasName[0]:
                    hasDir = addDir(new_key)
                    if hasDir[0]:
                        application_names.append(hasName[1])
                        application_dirs.append(hasDir[1] if hasDir[1][-1] == "\\" else hasDir[1] + "\\")
                        

            except Exception as e:
                #print(e)
                break
            index += 1

def giveAllData():
    try:
        getAllAplications()
        if len(application_dirs) == len(application_names) and len(application_dirs) > 0:
            return (application_names, application_dirs)
        else:
            print("Unordered OR Unable to locate the applications")
    except:
        print("Unable to fetch the applications list")
    

if __name__ == '__main__':
    getAllAplications()
    if len(application_dirs) == len(application_names) and len(application_dirs) > 0:
        print("============== Applications =============")
        for index in range(len(application_names)):
            print(application_names[index], application_dirs[index])
            pass
    else:
        print("Unordered OR Unable to locate the applications")