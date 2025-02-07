#!/bin/sh
# Download ttyd if it is not already present
if [ ! -f ttyd ]; then
    echo "Downloading ttyd..."
    wget https://github.com/tsl0922/ttyd/releases/download/1.6.3/ttyd.x86_64-unknown-linux-gnu.tar.gz
    tar -xzvf ttyd.x86_64-unknown-linux-gnu.tar.gz ttyd && chmod +x ttyd
    rm ttyd.x86_64-unknown-linux-gnu.tar.gz
fi

# Start ttyd on the port provided by Render's $PORT (defaults to 7681 if not set)
./ttyd -p ${PORT:-7681} python main.py 