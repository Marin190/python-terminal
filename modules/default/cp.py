import os
import shutil

def run_command(args):
    if not args:
        print("Usage: cp [-r] <source> <destination>")
        return
    
    parts = args.split()
    recursive = False
    
    if parts[0] == "-r" or parts[0] == "-rf":
        recursive = True
        parts = parts[1:]
    
    if len(parts) < 2:
        print("Usage: cp [-r] <source> <destination>")
        return
        
    source = parts[0]
    dest = parts[1]
    
    try:
        if os.path.isdir(source):
            if recursive:
                shutil.copytree(source, dest)
            else:
                print(f"cp: {source} is a directory (not copied)")
        else:
            shutil.copy2(source, dest)
    except Exception as e:
        print(f"cp: {str(e)}") 