import os

def create_folder_structure(name):
    
    base_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'IA folders', name)

    
    folders = [
        os.path.join(base_dir, 'configs'),
        os.path.join(base_dir, 'resourcepack', name, 'models', name),
        os.path.join(base_dir, 'resourcepack', name, 'textures', name)
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create YAML files
    with open(os.path.join(base_dir, 'configs', f'{name}.yml'), 'w') as f:
        pass 

    with open(os.path.join(base_dir, 'configs', 'categories.yml'), 'w') as f:
        pass  

    
    print(f'Folder structure for "{name}" created successfully in "finals" directory.')

def main():
    
    name = input("Enter the name to create folder structure: ")

    
    create_folder_structure(name)

if __name__ == "__main__":
    main()
