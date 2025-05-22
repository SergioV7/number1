"""Entry point to run the main program from ``my_project``."""

import os
import sys

# Add my_project/src to the path so we can import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'my_project', 'src'))

from main import main

if __name__ == '__main__':
    main()
