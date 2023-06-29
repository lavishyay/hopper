import os
from configparser import ConfigParser
from sys import exit

configname = "weirdconfignamesoidontoverwritesomethingimportant.ini"
config = ConfigParser()
category = {}

if os.path.isfile(configname):
    config.read(configname)
    for i in config["Folders"]:
        extentions  = config["Folders"][i].split(',')
        category[i] = extentions
else:
    with open(configname, 'w') as f:
        pass
    config.read(configname)
    config.add_section("Folders")
    config.set("Folders", "Videos", "mp4,mkv,mov,wmv,avi,flv,f4v,swf")
    config.set("Folders", "Audios", "mp3,aac,flac,alac,wav,aiff,dsd,pcm")
    config.set("Folders", "Documents", "pdf,docx,doc,xls,xlsx,txt,ppt,pptx,odp")
    config.set("Folders", "Installers", "exe,msi,iso")
    config.set("Folders", "Pictures", "png,jpeg,gif,tiff,psd,raw,webp,svg,tiff,tif")
    config.set("Folders", "Zips", "zip,rar,7z,pkg")
    with open(configname, 'w') as configfile:    # save
        config.write(configfile)       
    input("Config file created, press ENTER to exit and customize the config. . .")
    exit()

class File():
    def __init__(self, dest):
        self.dest = dest
        self.name = self.dest.split("\\")[-1]
        self.category = {}
        if '.' in self.name:
            self.exten = self.name.split('.')[-1]
        else:
            self.exten = "folder"

    def addCategory(self,name,extentions):
        self.category[name] = extentions

    def categorize(self):
        if self.exten != "folder":
            for i in self.category:
                if self.exten in self.category[i]:
                    self.cat = i
                    break
                else:
                    self.cat = "other"
        else:
            self.cat = "folder"
    def move(self):
        if self.exten != "folder":
            self.path = '{0}{1}\{2}'.format(
                "\\".join(self.dest.split("\\")[:-1]) + "\\",
                self.cat,
                self.name
            )
            if os.path.isdir("\\".join(self.path.split("\\")[:-1])):
                while True:
                    try:
                        os.rename(self.dest, self.path)
                        break
                    except Exception as e:
                        a = str(e).split("]")[0]
                        if a == "[WinError 32":
                            pass
                        elif a == "[WinError 183":
                            count = 1
                            while True:
                                temp = self.name.split(".")
                                temp[0] = ''.join(temp[:-1])
                                new_name = temp[0] + f" ({count})." + temp[-1]
                                self.path = '{0}{1}\{2}'.format(
                                "\\".join(self.dest.split("\\")[:-1]) + "\\",
                                self.cat,
                                new_name
                                )
                                try:
                                    os.rename(self.dest, self.path)
                                    break
                                except:
                                    count += 1
                        else:
                            print(f"error -> {e}")
                            break
            else:
                while True:
                    os.mkdir("\\".join(self.path.split("\\")[:-1]))
                    try:
                        os.rename(self.dest, self.path)
                        break
                    except Exception as e:
                        a = str(e).split("]")[0]
                        if a == "[WinError 32":
                            pass
                        elif a == "[WinError 183":
                            count = 1
                            while True:
                                temp = self.name.split(".")
                                temp[0] = ''.join(temp[:-1])
                                new_name = temp[0] + f" ({count})." + temp[-1]
                                self.path = '{0}{1}\{2}'.format(
                                "\\".join(self.dest.split("\\")[:-1]) + "\\",
                                self.cat,
                                new_name
                                )
                                try:
                                    os.rename(self.dest, self.path)
                                except:
                                    count += 1
                        else:
                            print(f"error -> {e}")
                            break

if __name__ == "__main__":
    pass