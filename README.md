# MD5 Dictionary Hash Cracker (Python)

A small Python tool I built to learn and demonstrate how dictionary attacks work against MD5 hashes.

Cryptographic hashes like MD5 are one-way. You can’t reverse them, so the only practical way to recover a password is to take a list of possible words, hash each one, and compare the results to the target hash. That’s exactly what this script does.

## What it does

- Loads candidate passwords from a separate `wordlist.txt` file
- Computes real MD5 hashes using Python’s `hashlib` (not fake or pre-stored values)
- Checks the target hash against every word in the list
- Returns the plaintext if a match is found, or tells you nothing matched

## Files

- `md5_cracker.py` – the main script
- `wordlist.txt` – one password candidate per line
- `README.md` – this file

## How to use it

Put both files in the same folder, then run:

```bash
python3 md5_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99
```

Or just run it without arguments and paste the hash when asked.

If it finds a match you’ll see the plaintext. If not, it prints:

`No matching hash identified. Please try again.`

## Custom wordlist

Just edit `wordlist.txt` and put one word per line. You can later swap it for a bigger list like rockyou if you want.

## Quick test hashes

| Password     | MD5 Hash                             |
|--------------|--------------------------------------|
| password     | 5f4dcc3b5aa765d61d8327deb882cf99     |
| 123456       | e10adc3949ba59abbe56e057f20f883e     |
| admin        | 21232f297a57a5a743894a0e4a801fc3     |
| contraseña   | 4c882dcb24bcb1bc225391a602feca7c     |
| пароль       | e242f36f4f95f12966da8fa2efd59992     |

## Notes

This is for learning, CTFs, and testing systems you own or have permission to test. Don’t use it on anything else.

MD5 itself is broken and should never be used for real password storage. Modern systems use slow, salted algorithms like bcrypt or Argon2.

## License

Copyright (c) 2026 Teamr Yheys /teamrsec  
Released for educational purposes. Feel free to use and modify.
```
