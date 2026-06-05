import subprocess
import os
import ctypes

def optimize_drives():
    """
    Launches Windows Drive Optimization (Defrag/TRIM) in the background.
    Requires Administrator privileges.
    """
    print("[+] Initializing drive optimization in the background...")

    # Security: Check if the script is running with Administrator privileges
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("[-] ERROR: This operation requires Administrator privileges.")
        print("[!] Please restart VS Code or your terminal as an Administrator.")
        return

    try:
        print("[~] Optimizing drive C: (this may take a few moments)...")
        print("[~] The script is running in the background, please wait.")

        # /O = Automatically selects the proper optimization (Defrag for HDD, TRIM for SSD)
        # /V = Verbose mode (displays complete text report at the end)
        result = subprocess.run(
            ["defrag", "C:", "/O", "/V"],
            capture_output=True,
            text=True,
            check=True
        )

        print("\n================ DRIVE OPTIMIZATION REPORT ================")
        print(result.stdout)
        print("===========================================================")
        print("[+] Drive optimization completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"[-] Error during drive optimization: {e}")
        if e.output:
            print(f"Details: {e.output}")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")