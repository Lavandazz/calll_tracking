from pathlib import Path


class PathFolder:
    home = Path.cwd()
    images = (home / "app" / "images").absolute()
    env = home/".env"
