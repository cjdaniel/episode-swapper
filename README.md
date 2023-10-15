# Episode Swapper

Some TV rips have episodes interchanged. Use this script by modifying the
`episode_pairs` dictionary, then running it from each season directory that
needs to be modified.

For each pair, 'src' is the "wrong" episode, and 'dst' is the "right"
episode. You can use any unique string that is part of the filename, but you
should probably use the `S**E**` part. The rest of the file name will be
preserved as you have it on disk.

The included `episode_pairs` dict is what's needed to correct a popular
Stargate SG-1 rip with the torrent info hash:
`66cee6aca421c309dc9a7ef5de25a22b657cc06b`
(you will need to add spaces between the `S**` and `E**` if your media library hasn't renamed the files to a standard format)

## Testing
Also included are some test files, with filenames as cleaned up by Sonarr for the TV rip mentioned above. They are just short text files with their original filenames inside for verification. If you run this script against them, you should be able to see that the renaming matches the provided dict.

### Generating your own test files
Generate your own test files by doing the below:

List the season dir in your media library:
```
ls -N > episodes
```

Copy that `episodes` file into the testing season dir, then continue:

Create a test file for each episode, each containing `originally: $original_file_name`:
```
while read -r line ; do echo "originally: $line" > "$line" ; done < episodes
```

Now you will be able to verify that the script is going to do what you think it will, by running it against the test set, and checking the contents of the files to see what they were originally named.