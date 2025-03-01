# Custom Windows Python Terminal

A Python-based custom terminal that provides Linux-like functionality with an extensible module system. This terminal includes built-in commands and supports custom modules for extended functionality.

## Features

- Linux-like command prompt with username, hostname, and current directory
- Built-in commands: cd, pwd, ls, cat, touch, rm, cp, mv, history
- Module system for extending functionality
- Community based evolution

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Marin190/python-terminal
cd terminal
```

2. Run the terminal (No external dependencies needed):
```bash
python terminal.py
```

## Built-in Commands

- `cd [directory]` - Change directory
- `pwd` - Print working directory
- `ls` - List files and directories
- `cat <file>` - Display file contents
- `touch <file>` - Create new file or update timestamp
- `rm [-r] <file/directory>` - Remove files or directories
- `cp [-r] <source> <destination>` - Copy files or directories
- `mv <source> <destination>` - Move/rename files or directories
- `history [-c|-d <num>|<n>]` - View or manage command history
- `modules <reload|list>` - Manage terminal modules
- `clear` or `cls` - Clear the terminal screen
- `exit` or `quit` - Exit the terminal

## Creating Custom Modules

You can extend the terminal's functionality by creating custom modules. Modules should be placed in the `modules` directory.

### Module Structure

Create a new Python file in the `modules` directory and refer to the modules/module_example.py for the basic structure.

### Module Guidelines

1. **File Name**: The module file name will be the command name (e.g., `mymodule.py` creates the `mymodule` command)

2. **Required Function**: Each module must have a `run_command(args)` function
   - `args`: String containing everything after your command name
   - The function handles all the module's logic

3. **Error Handling**: Always include proper error handling and usage messages

4. **Dependencies**: If your module requires external packages:
   - Document them in your module's header
   - Add them to the project's requirements.txt
   - Handle import errors gracefully

5. **Documentation**: Include:
   - Module description
   - Usage instructions
   - Examples
   - Required arguments
   - Optional flags


### Testing Your Module

1. Place your module in the `modules` directory
2. Start the terminal
3. Use `modules reload` to load your new module
4. Test your command
5. Use `modules list` to verify it's loaded

## License

This project is licensed under the MIT License - see the LICENSE file for details. 