import subprocess
import os

def setup_jupyter():
    # Check if Jupyter is installed
    try:
        subprocess.run(['jupyter', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print("Error: Jupyter is not installed or cannot be found.")
        print("Install Jupyter using 'pip install jupyterlab' or 'conda install -c conda-forge jupyterlab'")
        return

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
