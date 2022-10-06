""" A collection of tools for the runner """

from typing import Optional
from pathlib import Path
import time

import typer
from rich.console import Console
from rich.table import Table
from rich.progress import track


running = typer.Typer()
console = Console()

APP_NAME = "MY cli app"

@running.command()
def pace(
    first: Optional[str] = typer.Argument(None, help="The first name of the person"),
    last: str = "",
    middle: str = "",
):
    """
    Callin you by your name, like you deserve

    options include --last name and --middle name
    """
    print(f"Hello {first} {middle} {last}")


@running.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Have a good night {name}, sir!")
    else:
        print(f"See ya {name}!")


def get_pace(distance, time):
    """Calculate the pace based on a distance and time"""
    return time / distance


def main(name: str):
    """Main function"""
    table = Table("First", "Last", "Email")
    table.add_row("ben", "davidson", "b@e.com")
    table.add_row("michelle", "davidson", "email@e.com")
    console.print(table)
    print(f"Hello {name}")

    total = 0
    for value in track(range(100), description= "Processing"):
        time.sleep(0.1)
        total = total + 1
    
        app_dir = typer.get_app_dir(APP_NAME)
    app_dir_path = Path(app_dir)
    app_dir_path.mkdir(parents=True, exist_ok=True)
    config_path: Path = Path(app_dir) / "config.json"
    if not config_path.is_file():
        config_path.write_text('{"version": "1.0.0"}')
    config_file_str = str(config_path)
    print("Opening config directory")
    typer.launch(config_file_str, locate=True)


if __name__ == "__main__":
    # typer.run(main)
    running()
