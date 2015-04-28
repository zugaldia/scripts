#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Prepare the build; do --help for more info, or try the test/prepare_build.txt file.
'''

import argparse
import re

# Templates
PATTERN_BUILD = '%s = (\d+)'  # E.g: PROJECT_BUILD = 3
PATTERN_BUILD_TARGET = '%s = %d'
PATTERN_STAGE = '%s = \'(\w+)\''  # E.g: PROJECT_STAGE = 'PRODUCTION'
PATTERN_STAGE_TARGET = '%s = \'%s\''

# Parser
parser = argparse.ArgumentParser(description='Prepare the build.')

# Arguments
parser.add_argument(
    '--filename', required=True, type=str,
    help='The name of the file to process, e.g.: config.py or index.html (default: %(default)s)')
parser.add_argument(
    '--stage', type=str, default='DEVELOPMENT',
    help='The stage, e.g.: DEVELOPMENT or PRODUCTION (default: %(default)s)')
parser.add_argument(
    '--increase-build', type=bool, default=False,
    help='Whether to increase the build number or not, e.g: True or False (default: %(default)s)')
parser.add_argument(
    '--var-build', type=str, default='PROJECT_BUILD',
    help='The variable holding the build value, e.g.: PROJECT_BUILD (default: %(default)s)')
parser.add_argument(
    '--var-stage', type=str, default='PROJECT_STAGE',
    help='The variable holding the stage value, e.g.: PROJECT_STAGE (default: %(default)s)')

# Parse arguments
args = parser.parse_args()


def get_value(var_pattern, content):
    # Extracts a value from a given pattern
    m = re.search(var_pattern, content)
    if not m:
        raise Exception('Could not find pattern: %s' % var_pattern)
    return m.group(1)


def set_value(var_pattern, target_pattern, content):
    # Replaces an old value with a new value, based on patterns
    new_content, total_count = re.subn(var_pattern, target_pattern, content)
    if total_count != 1:
        raise Exception('Too many matches found for %s (%d instead of 1)'
                        % (var_pattern, total_count))
    print 'Updated (new %s)' % target_pattern
    return new_content

# Parse file content
dirty = False
with open(args.filename, 'r') as f:
    filecontent = f.read()

# Process build number
build_pattern = PATTERN_BUILD % args.var_build
current_build = get_value(build_pattern, filecontent)
if args.increase_build:
    dirty = True
    new_build = int(current_build) + 1
    target_pattern = PATTERN_BUILD_TARGET % (args.var_build, new_build)
    filecontent = set_value(build_pattern, target_pattern, filecontent)

# Process stage
stage_pattern = PATTERN_STAGE % args.var_stage
current_stage = get_value(stage_pattern, filecontent)
if args.stage != current_stage:
    dirty = True
    target_pattern = PATTERN_STAGE_TARGET % (args.var_stage, args.stage)
    filecontent = set_value(stage_pattern, target_pattern, filecontent)

# Do we need to rewrite the file?
if dirty:
    with open(args.filename, 'w') as f:
        f.write(filecontent)
    print 'File updated: %s' % args.filename
else:
    print 'No need to update file: %s' % args.filename
