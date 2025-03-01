import os
import shutil

def run_command(args):
    if not args:
        print("Usage: mv <source> <destination>")
        return
    
    parts = args.split()
    if len(parts) < 2:
        print("Usage: mv <source> <destination>")
        return
        
    source = parts[0]
    dest = parts[1]
    
    try:
        shutil.move(source, dest)
    except Exception as e:
        print(f"mv: cannot move '{source}' to '{dest}': {str(e)}") 