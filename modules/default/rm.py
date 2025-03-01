import os
import shutil

def run_command(args):
    if not args:
        print("Usage: rm [-r] <file/directory>")
        return
    
    parts = args.split()
    recursive = False
    
    if parts[0] == "-r" or parts[0] == "-rf":
        recursive = True
        parts = parts[1:]
    
    if not parts:
        print("Usage: rm [-r] <file/directory>")
        return
        
    for path in parts:
        try:
            if os.path.isdir(path):
                if recursive:
                    shutil.rmtree(path)
                else:
                    print(f"rm: cannot remove '{path}': Is a directory")
            else:
                os.remove(path)
        except Exception as e:
            print(f"rm: cannot remove '{path}': {str(e)}") 