# importing os module  
import os 
import sys
# importing shutil module  
import shutil 
  
# path 
path = 'E:/my course/python course/automation-scripts/test_dir'

# List files and directories 
# in '/home/User/Documents'
directories = {
    'doc': '/doc',
    'videos': '/videos',
    'compressed': '/compressed-files',
    'programs': '/programs',
    'others': '/others',
    'code': '/code',
    'images': '/images'
    }
if (len(sys.argv) > 1):
    path = sys.argv[1]
print("you are about to copy files from: \n{}".format(path))
x = input('press y if to confirm: ')

if (x == 'y'):
    try:
        for i in os.listdir(path):
        # check if .pdf or .epub or .txt , .docx, .ppt file put it in docs_dir
            if (i.lower().endswith(('.txt', '.pdf', '.epub', '.ppt'))):
                if (not os.path.exists(path+directories['doc'])):
                    os.makedirs(path+directories['doc'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['doc'],i))

            elif (i.lower().endswith(('.mp4', '.mkv', '.mp3'))):
                if (not os.path.exists(path+directories['videos'])):
                    os.makedirs(path+directories['videos'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['videos'],i))

            elif (i.lower().endswith(('.zip', '.rar'))):
                if (not os.path.exists(path+directories['compressed'])):
                    os.makedirs(path+directories['compressed'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['compressed'],i))

            elif (i.lower().endswith(('.jar', '.exe', '.dll'))):
                if (not os.path.exists(path+directories['programs'])):
                    os.makedirs(path+directories['programs'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['programs'],i))

            elif (i.lower().endswith(('.jpg', '.jpeg', '.png','bmp'))):
                if (not os.path.exists(path+directories['images'])):
                    os.makedirs(path+directories['images'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['images'],i))

            elif (i.lower().endswith(('.html', '.cpp', '.h','.py'))):
                if (not os.path.exists(path+directories['code'])):
                    os.makedirs(path+directories['code'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['code'],i))

            elif (os.path.isfile("{}/{}".format(path, i))):
                if (not os.path.exists(path+directories['others'])):
                    os.makedirs(path+directories['others'])
                shutil.move("{}/{}".format(path, i), "{}{}/{}".format(path,directories['others'],i))
        print("sucessfully organized")
    except FileNotFoundError as err:
        print(err)
    except KeyError as err:
        print(err)
else:
    print("please press y you pressed {}".format(x))

