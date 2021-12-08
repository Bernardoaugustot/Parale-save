import os
import shutil

root_src_dir = R'C:\Program Files (x86)\Steam\userdata\846537895\262060'
root_dst_dir = R'C:\Users\berna\Desktop\Darkest dungeon save\Save_1'

for src_dir, dirs, files in os.walk(root_src_dir): 
    # dirpath, dirnames, filenames /// caminho do diretorio,  nome do diretorio, nome do arquivo
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir) #Cria o diterotio
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        #shutil.move(src_file, dst_dir) # move esta redirecionando
        shutil.copy(src_file, dst_dir)