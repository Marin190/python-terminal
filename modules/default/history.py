import os
import json
from pathlib import Path

HISTORY_FILE = os.path.expanduser("~/.terminal_history")
MAX_HISTORY = 50

def load_history():
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
                return history[-MAX_HISTORY:] if len(history) > MAX_HISTORY else history
    except Exception:
        pass
    return []

def save_history(history):
    try:
        Path(HISTORY_FILE).parent.mkdir(parents=True, exist_ok=True)
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history[-MAX_HISTORY:] if len(history) > MAX_HISTORY else history, f)
    except Exception as e:
        print(f"Error saving history: {str(e)}")

def run_command(args):
    history = load_history()
    
    if not args:
        for i, cmd in enumerate(history, 1):
            print(f"{i:5d}  {cmd}")
        return
    
    parts = args.split()
    if parts[0] == "-c":
        save_history([])
        print("History cleared")
    elif parts[0] == "-d":
        try:
            if len(parts) < 2:
                print("Usage: history -d <number>")
                return
            index = int(parts[1]) - 1
            if 0 <= index < len(history):
                del history[index]
                save_history(history)
                print(f"Deleted history entry {index + 1}")
            else:
                print(f"Invalid history number: {parts[1]}")
        except ValueError:
            print(f"Invalid history number: {parts[1]}")
    elif parts[0].isdigit():
        n = int(parts[0])
        for i, cmd in enumerate(history[-n:], len(history) - n + 1):
            print(f"{i:5d}  {cmd}")
    else:
        print("Usage: history [-c] [-d num] [n]")
        print("  -c        clear the history list")
        print("  -d <n>    delete entry number n")
        print("  n         show last n entries") 