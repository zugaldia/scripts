#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Let's assume the following folder structure:

    ├── folder1
    └── folder2
        └── folder3

If your current path is `folder2`, and you want to create a symlink inside
`folder3`, that points at `folder1`, you need to do the following:

    folder2$ cd folder3; ln -s ../../folder1

This script lets you do the following:

    folder2$ python ln_plus.py --from folder3 --to ../folder1

We use this script in the Makefile, were sometimes we know the path relative
to the Makefile, but not once we've moved to the target folder.

'''

import os
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument('--from', required=True, type=unicode, help='the folder containing the symlink')
parser.add_argument('--to', required=True, type=unicode, help='the target of the symlink')
parser.add_argument('--name', type=unicode, help='the name of the created symlink', default='')
args = parser.parse_args()

# Get the args values
args_parsed = vars(args)
from_path = args_parsed.get('from')
to_path = args_parsed.get('to')
name = args_parsed.get('name')

# Ready
link_name = name or os.path.basename(os.path.normpath(to_path))
print 'Creating symlink to `%s` inside `%s` (name: `%s`)' % (to_path, from_path, link_name)
relative_path = os.path.relpath(to_path, from_path)
os.chdir(from_path)
os.symlink(relative_path, link_name)
