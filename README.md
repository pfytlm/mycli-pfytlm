# mycli-pfytlm

A tiny, zero-dependency CLI for managing personal todos / habits from the terminal.

## Features

- Add items with an optional priority (`high` / `mid` / `low`)
- List all items, mark them done, or delete them
- Data is stored as plain JSON under `~/.mycli/todos.json` — easy to back up or inspect
- Zero runtime dependencies. A single `pip install` gives you a global `mycli` command

## Installation

Requires Python 3.9 or newer.

```bash
pip install mycli-pfytlm
```

Or, if you prefer `uv`:

```bash
uv tool install mycli-pfytlm
```

After installation, a `mycli` command is available globally on your `PATH`.

## Usage

```bash
# Add a todo (priority defaults to mid)
mycli add "write weekly report" --priority high
mycli add "go for a 10-minute walk" --priority low

# List all todos
mycli list

# Mark item #1 done
mycli done 1

# Delete item #2
mycli delete 2
```

Data lives at `~/.mycli/todos.json` (override with the `MYCLI_DATA_DIR` environment variable).

## Development

```bash
# Clone and do an editable install
git clone https://github.com/your-name/mycli.git
cd mycli
uv venv
source .venv/bin/activate
uv pip install -e .

# Build distributable packages
uv build
# -> dist/mycli-pfytlm-0.1.0-py3-none-any.whl
#    dist/mycli-pfytlm-0.1.0.tar.gz
```

## License

MIT — see [LICENSE](LICENSE).
