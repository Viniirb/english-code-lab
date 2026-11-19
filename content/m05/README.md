# Module 05: Names and comments in English (code)

Real projects are written in English: names, comments, error messages. Translate the old Portuguese file.

1. Read `content/m05/legacy/pedidos.py`.
2. Create `work/m05/orders.py` with the same behavior but **English names, comments, docstrings and messages**.
   The tests in `content/m05/test_orders.py` define the new names (read them first!). Data keys change too (`price`, `quantity`).
3. Keep or write English comments/docstrings (at least 12 words in total). Good names say WHAT, not HOW.
4. Run `python scripts/validate_module.py 05`.

The validator runs the tests and rejects any leftover Portuguese word or accented letter.
