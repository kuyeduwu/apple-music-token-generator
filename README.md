# Apple music token generator

This is a script to generate the Apple Music token.

Before running this script, please follow [Apple's official guid](https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens) to create a MusicKit identifier and private key.

# Prerequisites

 - Python 3.7.1
 - pyjwt
 - cryptography

And the following information:
 - The key id you created in your apple developer account.
 - The team id of you apple developer account.
 - The `.p8` key file for the key

# Usage

```python
python generator.py -f mykey.p8 -k 1234567890 -t 1234567890 -e 10
```

# Details

Optional arguments:

    -h, --help      Show this help message and exit.
    -e, --expire    Expire after X days, default to 1 day.
Arguments:

    -f, --file      File name of the p8 key file downloaded from apple.
    -k, --key       The 10-character key id.
    -t, --team      Your apple developer account's team id.

You could run `python generator.py -h` to get the full help message.