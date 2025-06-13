#!/bin/sh
export PATH="$HOME/.local/bin:$PATH"

poetry install
#source .venv/bin/activate
poetry env activate

if ! grep -q "$PATH" /home/user/.bashrc; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/user/.bashrc
fi

#poetry run python -u -m flask --app src/main run -p $PORT --debug
poetry run adk web --port $PORT --reload ./agents