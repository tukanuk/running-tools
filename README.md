# Running Tools

A collection of tools for runners.

```
Usage: running_tools [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                  │
│ --show-completion             Show completion for the current shell, to copy it or       │
│                               customize the installation.                                │
│ --help                        Show this message and exit.                                │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────╮
│ goodbye                                                                                  │
│ pace                The most basic pace calculator                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
```


## Pace Tool

Usage: running_tools pace [OPTIONS] DISTANCE TIME

 The most basic pace calculator
 options include --distance in meters and --time in mm:ss

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────╮
│ *    distance      TEXT  The distance in meters [default: None] [required]               │
│ *    time          TEXT  The time in mm:ss [default: None] [required]                    │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
