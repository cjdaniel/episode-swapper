#!/usr/bin/env python3
# Episode Swapper
#
# Some TV rips have episodes interchanged. Use this script by modifying the
# `episode_pairs` dictionary, then running it from each season directory that
# needs to be modified.
#
# For each pair, 'src' is the "wrong" episode, and 'dst' is the "right"
# episode. You can use any unique string that is part of the filename, but you
# should probably use the S**E** part. The rest of the file name will be
# preserved as you have it on disk.
#
# The included `episode_pairs` dict is what's needed to correct a popular
# Stargate SG-1 rip with the torrent info hash:
# 66cee6aca421c309dc9a7ef5de25a22b657cc06b
# (you will need to add spaces between the S** and E** if your media library
# hasn't renamed the files to a standard format)

# Change the pairs in this structure
episode_pairs = [
{ 'src': "S01E07", 'dst': "S01E09" },
{ 'src': "S01E08", 'dst': "S01E07" },
{ 'src': "S01E09", 'dst': "S01E10" },
{ 'src': "S01E10", 'dst': "S01E11" },
{ 'src': "S01E11", 'dst': "S01E12" },
{ 'src': "S01E12", 'dst': "S01E13" },
{ 'src': "S01E13", 'dst': "S01E08" },
{ 'src': "S01E15", 'dst': "S01E16" },
{ 'src': "S01E16", 'dst': "S01E15" },
{ 'src': "S01E18", 'dst': "S01E19" },
{ 'src': "S01E19", 'dst': "S01E18" },
{ 'src': "S02E15", 'dst': "S02E16" },
{ 'src': "S02E16", 'dst': "S02E15" },
{ 'src': "S02E17", 'dst': "S02E18" },
{ 'src': "S02E18", 'dst': "S02E17" },
]

### DON'T CHANGE ANYTHING BELOW THIS LINE ###
import os
import glob
import sys

if not sys.version_info[0] >= 3 or not sys.version_info[1] >= 9:
    print("this script requires Python 3.9 or later")
    exit(1)


def find_file(filename_fragment):
    files = glob.glob(f"*{filename_fragment}*")
    if len(files) == 1:
        print(f"found matching file: {files}")
        return(files[0])
    elif len(files) > 1:
        print(f"found multiple matching files for '*{filename_fragment}*'")
        print(f"matching files: {files}")
        return
    elif len(files) == 0:
        print(f"found no matching files for '*{filename_fragment}*'")
        return

# mkdir a temp dir
tmpdir = '.tmp'
if not os.path.isdir(tmpdir):
    os.mkdir(tmpdir)

# look for the actual files -- if they exist in pwd, make a hard link with the new name in the temp dir
for pair in episode_pairs:
    print(f"was given {pair['src']} to be renamed to {pair['dst']}")

    src_file = find_file(pair['src'])
    dst_file = f"{tmpdir}/{find_file(pair['dst'])}"

    if not src_file or not dst_file:
        print(f"not doing anything for pair {pair}")
        continue

    print(f"hard linking {src_file} to {dst_file}")
    os.link(src_file, dst_file)

    print()

# mv all files from temp dir back to pwd
for file in glob.glob(f"{tmpdir}/*"):
    newfile = file.removeprefix(f"{tmpdir}/")
    print(f"moving {file} to {newfile}")
    
    try:
        os.rename(file, newfile)
    except OSError:
        os.replace(file, newfile)

# cleanup
os.rmdir(tmpdir)