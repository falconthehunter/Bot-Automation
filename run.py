#!/usr/bin/env python3
import subprocess
import time
import os

# List of folders where bot.py is located
bot_dirs = [
    "/root/bytenova",
    "/root/coresky",
    "/root/gpu",
    "/root/polyflow",
    "/root/prior",
    "/root/xos"
]

RUN_SECONDS = 180  # 3 minutes (180 seconds)

for bot_dir in bot_dirs:
    bot_path = os.path.join(bot_dir, "bot.py")
    print(f"=== Starting bot in {bot_dir} ===")

    proc = subprocess.Popen(
        ["python3", bot_path],
        cwd=bot_dir,
        stdin=subprocess.PIPE,
        text=True
    )

    time.sleep(2)  # wait 2 seconds to ensure bot is ready
    proc.stdin.write("3\n")
    proc.stdin.flush()

    time.sleep(RUN_SECONDS)

    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()

    print(f"Bot in {bot_dir} stopped.\n")

print("All bots completed.")