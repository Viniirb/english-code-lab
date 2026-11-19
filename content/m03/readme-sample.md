# FastNote

FastNote is a small library for saving notes in a file. It is simple and fast.

## Install

Run `pip install fastnote`. FastNote needs Python 3.9 or newer.

## Quick start

```python
from fastnote import Notebook

book = Notebook("notes.json")
book.add("Buy milk")
print(book.search("milk"))
```

## Options

- `autosave` (default: true): save the file after every change. Set it to false to save only when you call `save()`.
- `max_notes` (default: 1000): the most notes one notebook can keep. FastNote raises an error if you add more.

## Limits

FastNote is not safe for many users at the same time. Do not open the same file from two programs.
The search is case sensitive in version 1.

## Contributing

Open an issue before you send a big change. Small fixes are welcome. Run `pytest` before you open a pull request.
