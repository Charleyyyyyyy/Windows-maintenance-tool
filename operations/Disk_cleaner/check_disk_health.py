import subprocess
import os

def check_disk_health():
    
    # Checks the S.M.A.R.T. status of all connected drives using Windows WMI.
    # Returns a clear status for each drive found.
    
    print("[+] Checking storage drives health status (S.M.A.R.T.)...")
    
    try:
        # We run a native Windows WMIC command to get the status of the disks
        # 'diskdrive get status, caption' retrieves the drive model and its health
        result = subprocess.run(
            ["wmic", "diskdrive", "get", "status,caption"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # Split the output into lines and clean it up
        lines = [line.strip() for line in result.stdout.split('\n') if line.strip()]
        
        if len(lines) <= 1:
            print("[-] No drives detected or unable to read status.")
            return

        # The first line is the header (Caption / Status), so we skip it
        print(f"\n{'Drive Model':<40} | {'S.M.A.R.T. Status':<15}")
        print("-" * 60)
        
        for line in lines[1:]:
            # Windows outputs 'OK' if the drive is healthy
            if "OK" in line:
                print(f"{line:<51} [HEALTHY]")
            else:
                print(f"{line:<60} -> [WARNING / FAILURE]")
                
    except Exception as e:
        print(f"[-] Failed to retrieve disk health: {e}")
