import os
import subprocess
import importlib.util
import getpass

MODULES_DIR = "modules"
DEFAULT_MODULES_DIR = os.path.join(MODULES_DIR, "default")

def load_modules():
    modules = {}
    
    for directory in [MODULES_DIR, DEFAULT_MODULES_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    for directory in [MODULES_DIR, DEFAULT_MODULES_DIR]:
        for filename in os.listdir(directory):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module_path = os.path.join(directory, filename)
                
                try:
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    if hasattr(module, "run_command"):
                        modules[module_name] = module.run_command
                except Exception as e:
                    print(f"Error loading module {module_name}: {str(e)}")
    
    return modules

def get_prompt():
    username = getpass.getuser()
    hostname = os.environ.get('COMPUTERNAME', 'localhost')
    cwd = os.getcwd()
    home = os.path.expanduser("~")
    if cwd.startswith(home):
        cwd = "~" + cwd[len(home):]
    return f"\033[32m{username}@{hostname}\033[0m:\033[34m{cwd}\033[0m$ "

def execute_command(command, modules):
    from modules.default.history import load_history, save_history
    
    parts = command.strip().split()
    if not parts:
        return
    
    history = load_history()
    
    if parts[0] == "cd":
        try:
            if len(parts) > 1:
                path = os.path.expanduser(parts[1])
                os.chdir(path)
            else:
                os.chdir(os.path.expanduser("~"))
        except Exception as e:
            print(f"cd: {str(e)}")
        return

    if parts[0] == "pwd":
        print(os.getcwd())
        return
    
    if parts[0] == "modules":
        if len(parts) > 1:
            if parts[1] == "reload":
                global loaded_modules
                loaded_modules = load_modules()
                print("Modules reloaded.")
                return
            elif parts[1] == "list":
                print("Loaded modules:", ", ".join(modules.keys()) if modules else "No modules loaded.")
                return
        print("Usage: modules <reload|list>")
        return
    
    if parts[0] in modules:
        modules[parts[0]](" ".join(parts[1:]))
    else:
        if parts[0] in ["clear", "cls"]:
            os.system("cls" if os.name == "nt" else "clear")
        else:
            try:
                subprocess.run(command, shell=True)
            except Exception as e:
                print(f"Error executing command: {e}")
    
    if not history or history[-1] != command:
        history.append(command)
        save_history(history)

def main():
    global loaded_modules
    loaded_modules = load_modules()
    print("Custom Linux-like Terminal - Type 'exit' to quit")
    
    while True:
        try:
            command = input(get_prompt())
            if command.lower() in ["exit", "quit"]:
                break
            execute_command(command, loaded_modules)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
    
if __name__ == "__main__":
    main()
