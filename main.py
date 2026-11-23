"""Entry program for the Write Your Agent's Tinder Bio bounty.

Copies the one-line bio held in this repository to the output path
the harness expects. Deterministic: it copies the same bytes every run
and performs no network access. The copy is verified by comparing file
sizes so a truncated write is never mistaken for a finished entry.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT, exist_ok=True)
dest = os.path.join(OUT, "entry.txt")
shutil.copyfile(SRC, dest)
assert os.path.getsize(dest) == os.path.getsize(SRC), "truncated copy"
print("wrote entry.txt")
