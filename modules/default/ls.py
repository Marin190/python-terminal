import os
from datetime import datetime
import stat

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}TB"

def format_time(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%b %d %H:%M")

def get_file_permissions(path):
    st = os.stat(path)
    mode = st.st_mode
    perms = ""
    perms += "d" if stat.S_ISDIR(mode) else "-"
    perms += "r" if mode & stat.S_IRUSR else "-"
    perms += "w" if mode & stat.S_IWUSR else "-"
    perms += "x" if mode & stat.S_IXUSR else "-"
    perms += "r" if mode & stat.S_IRGRP else "-"
    perms += "w" if mode & stat.S_IWGRP else "-"
    perms += "x" if mode & stat.S_IXGRP else "-"
    perms += "r" if mode & stat.S_IROTH else "-"
    perms += "w" if mode & stat.S_IWOTH else "-"
    perms += "x" if mode & stat.S_IXOTH else "-"
    return perms

def run_command(args):
    path = "." if not args else args.split()[0]
    try:
        entries = os.listdir(path)
        for entry in sorted(entries):
            full_path = os.path.join(path, entry)
            stats = os.stat(full_path)
            perms = get_file_permissions(full_path)
            size = format_size(stats.st_size)
            mtime = format_time(stats.st_mtime)
            
            if os.path.isdir(full_path):
                entry += "/"
            
            print(f"{perms} {size:>8} {mtime} {entry}")
    except Exception as e:
        print(f"ls: cannot access '{path}': {str(e)}") 