import os
import platform
import subprocess
import time
import shutil

# -----------------------------
#  COLOR (Windows only)
# -----------------------------
if os.name == "nt":
    os.system("color 0A")  # Green text
    os.system("title SysMine")

# -----------------------------
#  ASCII BANNER
# -----------------------------
banner = r"""
                                                                                                  
      *******                                   *****   **    **                                  
    *       ***                              ******  ***** *****     *                            
   *         **                             **   *  *  ***** *****  ***                           
   **        *                             *    *  *   * **  * **    *                            
   ***          **   ****         ****        *  *    *     *                                    
  ** ***         **    ***  *    * **** *    ** **    *     *     ***     ***  ****       ***    
 *** ***       **     ****    **  ****     ** **    *     *      ***     **** **** *   * ***   
   *** ***     **      **    ****          ** **    *     *       **      **   ****   *   ***  
     *** ***   **      **      ***         ** **    *     *       **      **    **   **    *** 
       ** ***  **      **        ***       ** **    *     **      **      **    **   ********  
       ** **  **      **          ***     *  **    *     **      **      **    **   *******   
         * *   **      **     ****  **        *     *      **     **      **    **   **        
 ***        *     *********    * **** *     ****      *      **     **      **    **   ****    * 
*  *********        **** ***      ****     *  *****           **    *** *   ***   ***   *******  
*     *****                ***             *     **                   ***     ***   ***   *****   
                    *****   ***            *                                                      
 **               ********  **              **                                                    
                 *      ****                                                                                                                                                                                                                                                                           
                                                           SystemInfoGatherer   
                                                         (Now with network info!)
"""

print(banner)
print()

# -----------------------------
#  FUNCTION TO RUN COMMANDS
# -----------------------------
def run_command(cmd):
    try:
        result = subprocess.run(
            cmd, shell=True, text=True, capture_output=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"[ERROR] {e}")

# -----------------------------
#  OS-SPECIFIC COMMANDS
# -----------------------------
system = platform.system()

print("Gathering system information...\n")

if system == "Windows":
    run_command("systeminfo")
else:
    # Linux / macOS
    if shutil.which("neofetch"):
        run_command("neofetch")
    else:
        run_command("uname -a")

input("\nPress Enter to continue...")

print("\nloading...")
time.sleep(3)

print("\nGathering network information...\n")

if system == "Windows":
    run_command("ipconfig /all")
else:
    # Linux/macOS
    if shutil.which("ifconfig"):
        run_command("ifconfig -a")
    else:
        run_command("ip addr show")

input("\nPress Enter to exit...")
