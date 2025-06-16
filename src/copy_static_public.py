import os
import shutil
path = '/home/bkeller/Static_Site_Generator/public'
static_path = '/home/bkeller/Static_Site_Generator/static'

def public_clearing_house(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        shutil.rmtree(path)
        os.mkdir(path)

def copy_paste(static_path, path):
    for item in os.listdir(static_path):
        item_path = os.path.join(static_path, item)
        pub_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, pub_path)
            print(f'{pub_path}')
        elif os.path.isdir(item_path):
            os.mkdir(pub_path)
            copy_paste(item_path, pub_path)
            print(f'{pub_path}')

public_clearing_house(path)
copy_paste(static_path, path)