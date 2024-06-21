import subprocess
import os

# List of libraries to install
libraries_to_install = [
    'jupyterlab',
    # Add more libraries as needed, e.g., 'numpy', 'pandas', etc.
]

def install_libraries():
    installed_libraries = subprocess.run(['pip', 'freeze'], capture_output=True, text=True).stdout.split('\n')
    
    for lib in libraries_to_install:
        if any(lib in package for package in installed_libraries):
            print(f'{lib} is already installed. Skipping...')
        else:
            print(f'Installing {lib}...')
            subprocess.run(['pip', 'install', lib])

def configure_jupyter():
    try:
        from jupyter_core.paths import jupyter_config_dir
    except ModuleNotFoundError:
        print("Error: 'jupyter_core' module not found. Make sure Jupyter Lab is installed.")
        return
    
    # Get Jupyter config directory
    config_dir = jupyter_config_dir()
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    
    # Generate default config file
    default_config_file = os.path.join(config_dir, 'jupyter_notebook_config.py')
    if not os.path.exists(default_config_file):
        subprocess.run(['jupyter', 'notebook', '--generate-config', '--config', default_config_file])
    
    # Modify config file to allow no authentication and admin access
    with open(default_config_file, 'a') as f:
        f.write('\n')
        f.write('c.NotebookApp.token = ""\n')  # Disable token authentication
        f.write('c.NotebookApp.password = ""\n')  # Disable password authentication
        f.write('c.NotebookApp.allow_origin = "*"\n')  # Allow connections from anywhere
        f.write('c.NotebookApp.allow_root = True\n')  # Allow Jupyter to be run by root user

def start_jupyter_lab():
    subprocess.run(['jupyter', 'lab'])

if __name__ == "__main__":
    install_libraries()  # Install required libraries if not already installed
    configure_jupyter()  # Configure Jupyter Lab
    start_jupyter_lab()  # Start Jupyter Lab
