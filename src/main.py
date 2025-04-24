import os
import json
import sys
from utils import FileOperations, DirectoryOperations, Navigation, ConfigReader

class FileManager:
    def __init__(self):
        work_dir = ConfigReader.load_config()
        self.work_dir = work_dir
        self.curr_dir = work_dir
        self.file_ops = FileOperations(self)
        self.dir_ops = DirectoryOperations(self)
        self.navigation = Navigation(self)
        
        self.commands = {
            'help': self.show_help,
            'exit': self.exit,
            'ls': self.navigation.list_dir,
            'cd': self.navigation.change_dir,
            'mkdir': self.dir_ops.create_dir,
            'rmdir': self.dir_ops.remove_dir,
            'touch': self.file_ops.create_file,
            'read': self.file_ops.read_file,
            'write': self.file_ops.write_file,
            'rm': self.file_ops.remove_file,
            'cp': self.file_ops.copy_file,
            'mv': self.file_ops.move_file,
            'rename': self.file_ops.rename_file
        }

    def show_help(self):
        print("Available commands:")
        print("  help      - Show this help")
        print("  exit      - Exit file manager")
        print("  ls        - List directory contents")
        print("  cd <dir>  - Change directory")
        print("  mkdir <dir> - Create directory")
        print("  rmdir <dir> - Remove directory")
        print("  touch <file> - Create file")
        print("  read <file> - Read file")
        print("  write <file> <text> - Write to file")
        print("  rm <file>   - Remove file")
        print("  cp <src> <dest> - Copy file")
        print("  mv <src> <dest> - Move file")
        print("  rename <old> <new> - Rename file")

    def exit(self):
        print("See ya!")
        sys.exit(0)

    def run(self):
        print(f"File Manager. Working directory: {self.work_dir}")
        print("Type 'help' for list of commands")
        
        while True:
            try:
                current_dir = os.path.relpath(self.curr_dir, self.work_dir)
                if current_dir == '.':
                    current_dir = '/'
                else:
                    current_dir = '/' + current_dir
                
                cmd = input(f"{current_dir}> ").strip().split()
                if not cmd:
                    continue
                
                command = cmd[0].lower()
                args = cmd[1:]
                
                if command in self.commands:
                    self.commands[command](*args)
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    manager = FileManager()
    manager.run()