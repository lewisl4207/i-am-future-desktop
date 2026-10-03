"""I Am Future Desktop — A local helper for I Am Future rooftop folders, craft benches, and city photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='i_am_future_desktop',
        description='A local helper for I Am Future rooftop folders, craft benches, and city photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('I Am Future Desktop')
    print('Keep the rooftop on disk before a craft update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
