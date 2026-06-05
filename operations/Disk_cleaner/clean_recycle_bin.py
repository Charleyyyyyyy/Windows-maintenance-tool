# imports
import ctypes

def clean_recycle_bin():

    # Empties the Windows Recycle Bin using the native Shell32 API.
    # Bypasses confirmation dialogs and progress UI for a silent cleanup.

    print("[+] Emptying the Windows Recycle Bin...")
    
    # Windows constants to configure the cleanup behavior
    # 7 combined flags: No confirmation, no progress UI, no sound
    SHERB_NOCONFIRMATION = 0x00000001
    SHERB_NOPROGRESSUI   = 0x00000002
    SHERB_NOSOUND        = 0x00000004
    flags = SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND

    try:
        # Call the native Windows Shell function
        # First parameter (None) targets the default root recycle bin
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, flags)
        
        # In Windows API, 0 indicates a successful execution
        if result == 0:
            print("[+] Recycle Bin emptied successfully!")
        elif result == -2147418113:
            print("[~] Recycle Bin is already empty.")
        else:
            print(f"[-] Windows returned an error code: {result}")
            
    except Exception as e:
        print(f"[-] Failed to empty Recycle Bin: {e}")