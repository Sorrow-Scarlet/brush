"""Entry Point"""

import designer

from . import main

if __name__ == "__main__":
    app = main.App(title=f"Magic Brush v{designer.__version__}")
    app.center()
    app.mainloop()
