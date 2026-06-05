import os
import shutil

def clean_browser_cache():
    
    # Cleans Google Chrome and Microsoft Edge cache and junk files from AppData.
    #Calculates and displays the total disk space saved.
    
    print("[+] Initializing browser cache cleanup...")
    
    local_appdata = os.environ.get('LOCALAPPDATA')
    if not local_appdata:
        print("[-] Could not locate Local AppData directory.")
        return

    paths_to_clean = {
        "Google Chrome Cache": os.path.join(local_appdata, r"Google\Chrome\User Data\Default\Cache\Cache_Data"),
        "Google Chrome Crash Reports": os.path.join(local_appdata, r"Google\Chrome\User Data\Crashpad\reports"),
        "Microsoft Edge Cache": os.path.join(local_appdata, r"Microsoft\Edge\User Data\Default\Cache\Cache_Data"),
        "Microsoft Edge Crash Reports": os.path.join(local_appdata, r"Microsoft\Edge\User Data\Crashpad\reports")
    }

    cleaned_folders = 0
    failed_folders = 0
    total_bytes_saved = 0

    for name, path in paths_to_clean.items():
        if os.path.exists(path):
            print(f"[~] Cleaning {name}...")
            try:
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    try:
                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            total_bytes_saved += os.path.getsize(item_path)
                            os.unlink(item_path)
                        elif os.path.isdir(item_path):
                            for root, dirs, files in os.walk(item_path):
                                for f in files:
                                    f_path = os.path.join(root, f)
                                    try:
                                        total_bytes_saved += os.path.getsize(f_path)
                                    except os.error:
                                        continue
                            shutil.rmtree(item_path)
                    except Exception:
                        continue
                        
                print(f"[+] Successfully cleaned {name}!")
                cleaned_folders += 1
            except Exception:
                print(f"[!] Partial or failed cleanup for {name} (Browser might be open).")
                failed_folders += 1
        else:
            print(f"[~] {name} directory not found (Skipping).")

    megabytes_saved = round(total_bytes_saved / (1024 * 1024), 2)
    print(f"\n[+] Browser cleanup finished: {cleaned_folders} cleaned, {failed_folders} skipped/failed.")
    print(f"Total space saved: {megabytes_saved} MB")
clean_browser_cache()