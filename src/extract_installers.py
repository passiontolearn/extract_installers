import sys
import os
import subprocess

srcPath = r'F:\\Installers\\Development\\'
destPath = r'F:\\Extracted_Installers\\'
SevenZip = r'C:\\Program Files\\7-Zip\\7z.exe'
def main():
    Check_Paths_Exist()
    for folderName, subfolders, filenames in os.walk(srcPath):
        # print('The current folder is ' + folderName)
        # for subfolder in subfolders:
        #     print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            third_folder_inDir = folderName.split(os.sep,4)[4]
            # print(third_folder_inDir, "\n")
            # print('FILE INSIDE ' + folderName + ': '+ filename)

            # NOTE: destPath + third_folder_inDir   is intentional here (!)
            #       otherwise os.path.join() will think a leading slash '/'  means "start at Root directory"
            full_destPath = os.path.join(destPath + third_folder_inDir, filename)
            print('Attempting extract of ' + filename + ' to: ' + full_destPath)
            full_srcPath = os.path.join(folderName, filename)
            exitcode = ExtractFile(full_srcPath, full_destPath)
            if exitcode == 0:
                print("SUCCESS")
            else:
                print("------------------")
                print("Failed to extract '{}' to '{}'".format(full_srcPath, full_destPath))
                print("------------------")

def ExtractFile(file_fullPath, destPath):
    # For 7z usage see: https://sevenzip.osdn.jp/chm/cmdline/switches/overwrite.htm
    result = subprocess.run([SevenZip, 'x', file_fullPath, '-o' + destPath, '-aoa'], stdout=subprocess.DEVNULL)
    return result.returncode

def Check_Paths_Exist():
    if not os.path.isfile(SevenZip):
        sys.exit("7z.exe does not exist at '{}' (!)".format(SevenZip))
    if not os.path.exists( os.path.normpath(srcPath) ):
            sys.exit("Please make sure source path '{}' exists (!)".format(srcPath))
    if not os.path.exists( os.path.normpath(destPath) ):
        sys.exit("Please make sure destination path '{}' exists (!)".format(destPath))

if __name__ == "__main__":
    main()
