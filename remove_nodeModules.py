import os
import shutil

def has_child_directory(target, root_dir):
    try:
        for item in os.listdir(root_dir):
            full_path = os.path.join(root_dir, item)
            if os.path.isdir(full_path) and item == target:
                return True
    except PermissionError:
        print(f"Sem permissão para acessar: {root_dir}")
        return False
    return False

def main():
    base_dir = 'C:\\Users\\Talison'

    for item in os.listdir(base_dir):
        full_path = os.path.join(base_dir, item)
        if os.path.isdir(full_path) and has_child_directory('node_modules', full_path):
            # print(f"A pasta {item} dentro de {base_dir} contém um diretório 'node_modules'.")
            print('APAGANDO NODE_MODULES')  
            shutil.rmtree(full_path+'\\node_modules')

main()