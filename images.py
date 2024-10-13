import os
import shutil

folder_to_zip = r'C:\Users\dadoo\OneDrive\Pictures\face_position'  
output_zip_path = r'C:\Users\dadoo\OneDrive\Pictures\face_position\\outputfolder1.zip'  

shutil.make_archive(output_zip_path.replace('.zip', ''), 'zip', folder_to_zip)

print(f"All files in {folder_to_zip} have been zipped into {output_zip_path}")
