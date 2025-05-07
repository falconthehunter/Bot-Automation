
# Bot Automation Script

This project contains a Python script to manage multiple bots running in different directories. The script launches each bot, sends an input command, runs them for a specified duration, and then terminates them.

## Prerequisites

Ensure the following are installed on your system:

- Python 3.x
- Necessary dependencies for each bot (if any)

### Install Python 3

You can install Python 3 by following the instructions on the [official Python website](https://www.python.org/downloads/).

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. Ensure that each bot script (e.g., bot.py) is located in one of the directories listed in the bot_dirs list.


3. Run the bot automation script:
```bash
python3 run.py
```
The script will:

Start each bot in the specified directories.

Wait for 2 seconds to ensure the bot is ready.

Send an input command (currently set to 3\n) to each bot.

Keep each bot running for a specified duration (default is 3 minutes).

Terminate the bot and clean up.




Configuration

You can easily customize the following parameters in the script:

1. Bot Directories

The bot_dirs list contains the paths to the directories where the bot.py files are located. You can modify this list to reflect the correct paths to your bots.
```bash
bot_dirs = [
    "/path/to/bot1",
    "/path/to/bot2",
    "/path/to/bot3"
]
```
Simply replace "/path/to/bot1", "/path/to/bot2", etc., with the correct paths where your bot scripts are stored.

2. Running Duration

The duration each bot will run is controlled by the RUN_SECONDS variable. By default, it is set to 180 seconds (3 minutes). You can adjust this value to your desired duration in seconds.
```bash
RUN_SECONDS = 180  # Default is 3 minutes
```
To run the bots for a different duration, change RUN_SECONDS to the number of seconds you want.

3. Input Command

The script sends an input command to each bot after a brief delay. Currently, it sends the input 3\n, which is defined in the following lines:
```bash
proc.stdin.write("3\n")
```
If your bots require a different input command, simply change "3\n" to the desired command.
```bash
proc.stdin.write("your-command\n")
```
License

This project is licensed under the MIT License - see the LICENSE file for details.
