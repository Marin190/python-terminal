import os
from pathlib import Path

def run_command(args):
    if not args:
        print("Usage: touch <file>")
        return
    
    try:
        for file in args.split():
            Path(file).touch()
    except Exception as e:
        print(f"touch: {args}: {str(e)}") 