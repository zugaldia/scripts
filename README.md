# Scripts

Miscellaneous scripts.

## Installation

This will create symlinks in `/usr/local/bin`:

```
$ make install
```

## ln_plus.py

Creates symbolic links in a simpler way. We use it in `Makefile`s,
were sometimes we know the path relative to the `Makefile`,
but not once we've moved to the target folder.

Usage:

```
$ ./ln_plus.py --help
usage: ln_plus.py [-h] --from FROM --to TO [--name NAME]

optional arguments:
  -h, --help   show this help message and exit
  --from FROM  the folder containing the symlink
  --to TO      the target of the symlink
  --name NAME  the name of the created symlink
```

For example, this creates a link to `ln_plus.py` into `/usr/local/bin` from this folder:

```
$ ./ln_plus.py --from /usr/local/bin --to ln_plus.py
```

## prepare_build.py

Helps you change the stage and build number in a file,
works well with text, Python, and JS files.

Usage:

```
$ ./prepare_build.py --help
usage: prepare_build.py [-h] --filename FILENAME [--stage STAGE]
                        [--increase-build INCREASE_BUILD]
                        [--var-build VAR_BUILD] [--var-stage VAR_STAGE]

Prepare the build.

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME   The name of the file to process, e.g.: config.py or
                        index.html (default: None)
  --stage STAGE         The stage, e.g.: DEVELOPMENT or PRODUCTION (default:
                        DEVELOPMENT)
  --increase-build INCREASE_BUILD
                        Whether to increase the build number or not, e.g: True
                        or False (default: False)
  --var-build VAR_BUILD
                        The variable holding the build value, e.g.:
                        PROJECT_BUILD (default: PROJECT_BUILD)
  --var-stage VAR_STAGE
                        The variable holding the stage value, e.g.:
                        PROJECT_STAGE (default: PROJECT_STAGE)
```

For example:

```
$ prepare_build.py --filename test/prepare_build.txt --stage=development
Updated (new PROJECT_STAGE = 'development')
File updated: test/prepare_build.txt
```

And:

```
$ prepare_build.py --filename test/prepare_build.txt --stage=production --increase-build=True
Updated (new PROJECT_BUILD = 42)
File updated: test/prepare_build.txt
```
