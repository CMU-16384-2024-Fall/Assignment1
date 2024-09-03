import zipfile
import os

def create_submission():
    with zipfile.ZipFile('handin.zip', 'w') as zf:
        # Adding forward_kinematics_RR.py from ex1 folder to the main folder of the zip
        zf.write(os.path.join('ex1', 'forward_kinematics_RR.py'), 'forward_kinematics_RR.py')
        
        # Adding workspace_analysis_PR.py from ex2 folder to the main folder of the zip
        zf.write(os.path.join('ex2', 'workspace_analysis_PR.py'), 'workspace_analysis_PR.py')
        
        # Adding the entire ex3 folder and its contents to the zip
        for root, dirs, files in os.walk('ex3'):
            for file in files:
                file_path = os.path.join(root, file)
                zf.write(file_path, os.path.relpath(file_path, os.path.join('ex3', '..')))
                
    print("Created submission archive: handin.zip")

if __name__ == "__main__":
    create_submission()