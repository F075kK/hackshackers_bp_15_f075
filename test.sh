#!/usr/bin/env bash
python 2.py 1>/dev/null 2> 222
python -m csvbar < 222 | tee results.txt

