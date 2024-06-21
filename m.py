import subprocess
import os

def setup_jupyter():
    # Generate Jupyter configuration if not already generated
    subprocess.run(['jupyter', 'notebook', '--generate-config', '--allow-root'])

    # Path to Jupyter configuration file
    config_file = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')

    # Configure JupyterLab options in the configuration file
    with open(config_file, 'a') as f:
        f.write("c.NotebookApp.token = ''\n")
        f.write("c.NotebookApp.allow_root = True\n")
        f.write("c.NotebookApp.ip = '0.0.0.0'\n")
        f.write("c.NotebookApp.port = 8888\n")

    # Start JupyterLab in the background
    subprocess.Popen(['nohup', 'jupyter', 'lab', '&'])

if __name__ == "__main__":
    setup_jupyter()
