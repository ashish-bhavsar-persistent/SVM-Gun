import os, os.path

DIR = 'features/train'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))