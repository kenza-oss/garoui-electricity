#!/usr/bin/env python3
"""
Script to compile .po files to .mo files using polib.
Runs as part of the build process on Render (no gettext needed).
"""
import os
import sys

try:
    import polib
except ImportError:
    print("Installing polib...")
    os.system(f"{sys.executable} -m pip install polib")
    import polib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')

compiled = 0
errors = 0

for lang in os.listdir(LOCALE_DIR):
    lc_messages = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES')
    if not os.path.isdir(lc_messages):
        continue
    po_file = os.path.join(lc_messages, 'django.po')
    mo_file = os.path.join(lc_messages, 'django.mo')
    if os.path.exists(po_file):
        try:
            po = polib.pofile(po_file)
            po.save_as_mofile(mo_file)
            print(f"✅  Compiled: {po_file} -> {mo_file}")
            compiled += 1
        except Exception as e:
            print(f"❌  Error compiling {po_file}: {e}")
            errors += 1

print(f"\nDone: {compiled} compiled, {errors} errors.")
if errors:
    sys.exit(1)
