def run_command(args):
    if not args:
        print("Usage: cat <file>")
        return
    
    try:
        with open(args, 'r') as file:
            print(file.read(), end='\n')
    except Exception as e:
        print(f"cat: {args}: {str(e)}")