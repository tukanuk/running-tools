""" A collection of tools for the runner """

from typing import Optional
from pathlib import Path
import time
from xml.dom import minicompat

import typer
from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel


running = typer.Typer()
console = Console()

APP_NAME = "MY cli app"


@running.command()
def pace(
    distance: str = typer.Argument(..., help="The distance in meters"),
    time: str = typer.Argument(..., help="The time in mm:ss"),
):
    """
    The most basic pace calculator

    options include --distance in meters and --time in mm:ss
    """
    minutes = int((time.split(":")[0]))
    seconds = int((time.split(":")[1]))
    time_in_seconds = int(minutes * 60 + seconds)

    print(f"time in seconds {time_in_seconds}")

    seconds_per_km = int(time_in_seconds / (int(distance) / 1000))

    minutes = int(seconds_per_km / 60)
    seconds = seconds_per_km - minutes * 60

    print(
        Panel.fit(
            f"Running [yellow]{distance}[/yellow] meters in [purple]{time}[/purple] gives you a pace of [green bold]{minutes}:{seconds:02}[/green bold] /km"
        )
    )


@running.command()
def goodbye(name: str, formal: bool = False):git 
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
    for value in track(range(100), description="Processing"):
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
