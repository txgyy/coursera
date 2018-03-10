import os


for i in range(1, 9):
    os.chdir('week' + str(i))
    for file_dir in os.listdir('.'):
        os.chdir(file_dir)
        for name in os.listdir('.'):
            if name[-4:]=='.mp4':
                os.rename(name,'0'+name)
        os.chdir('..')
    os.chdir('..')

