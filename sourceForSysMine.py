import tkinter as tk
from tkinter import *
import os
import platform
import subprocess
import shutil

# gui

root = Tk()

root.mainloop()

# Detect OS
current_os = platform.system().lower()

# Windows-only console styling
if current_os == "windows":
    os.system("color 0A")
    os.system("title SystemInfo")

# ASCII Banner
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
"""

print(banner)

# Choose system info command based on OS
if current_os == "windows":
    cmd = ["systeminfo"]

elif current_os == "linux":
    # Prefer hostnamectl if available
    if shutil.which("hostnamectl"):
        cmd = ["hostnamectl"]
    else:
        cmd = ["uname", "-a"]

elif current_os == "darwin":  # macOS
    cmd = ["system_profiler", "SPSoftwareDataType"]

else:
    print("Unsupported OS. Cannot gather system info.")
    cmd = None

# Run the command
if cmd:
    try:
        subprocess.check_output(cmd)
    except Exception as e:
        print(f"Error running system info command: {e}")

# Pause equivalent
input("\nPress Enter to continue...")
