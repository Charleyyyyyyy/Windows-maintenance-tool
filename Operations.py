
# import 
import os
import shutil

# this fonction clean the temp_dir
def clean_Temp_dir_files():
    temp_dir = os.environ.get('TEMP')
    if not temp_dir or not os.path.exists(temp_dir):
        print("[-] Temporary directory not found")
        return
    
    print(f"[+] Starting cleanup in: {temp_dir}")

    deleted_files_count = 0
    bytes_saved = 0
for root, dirs, files in os.walk(temp_dir, topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        try:
            file_size = os.path.getsize(file_path)
            os.remove(file_path)

            bytes_saved += file_size
            deleted_files_count += 1
        except Exception:
            continue

    for name in dirs:
        dir_path = os.path.join(root, name)
        try:
            os.rmdir(dir_path)
        except Exception:
            continue
Mb_saved = bytes_saved / (1024 * 1024)
print("--- Cleanup Finished ---")
print(f"Files deleted: {deleted_files_count}")
print(f"Mb saved: {Mb_saved:.2f} Mb")

if __name__== "__main__":
    clean_Temp_dir_files