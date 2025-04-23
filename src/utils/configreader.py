import os
import json
import sys

class ConfigReader:
    def load_config():
        try:
            with open('config/config.json', 'r') as f:
                config = json.load(f)
                work_dir = os.path.abspath(config['work_dir'])
                if not os.path.exists(work_dir):
                    os.makedirs(work_dir)
                return work_dir
        except Exception as e:
            print(f"Error loading config: {e}")
            sys.exit(1)
