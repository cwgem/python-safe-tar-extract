# python-safe-tar-extract

Some POC code for attempting to safely extract a tarfile with nasty symlink/directory traversal issues

## WARNING!!!

`testing.tar` is meant to test for safe extraction and purposely does nasty things that a normal tar archive shouldn't do. While the contents doesn't hit critical system files you shouldn't be trying to unpack it on a production system. I'm not held liable for what happens if you don't head this warning.

## Description

This project is a simple python file with some POC code to attempt to extract a tar file safely while trying to guard against the following:

* Absolute paths outside of the target directory
* Path traversal outside of the target directory
* Symlink targets outside of the target directory

For more insight on the potential security pitfalls of using vanilla tar extraction see:

https://gist.github.com/cwgem/204b233193b25e123422ed64142d8ff8

## Requirements

* Python 3.6+ (Python 3 especially for pathlib)

## Usage

Since this is a POC your current method of usage will simply be copy/paste of the code. Note that the code uses the defaults for `set_attrs` and `numeric_owner` so it will need to be modified to handle that.

If you just want to see it in action:

1. Clone this repo
2. Setup a virtualenv python 3.6 or have python 3.6 installed already
3. `python3.6 extract.py` in the source repository

If things go well the `test2.txt` file should be the only file extracted and:

```
../test.txt
../symlink
/tmp/test3.txt
```

should not exist.
