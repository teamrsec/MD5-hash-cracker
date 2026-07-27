import hashlib
import sys
import os

WORDLIST_FILE = "wordlist.txt"

def load_wordlist(filepath: str) -> list:
    """Load passwords from a text file (one per line)."""
    if not os.path.exists(filepath):
        print(f"[!] Wordlist file not found: {filepath}")
        sys.exit(1)
    
    words = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.strip()
            if word:                    # skip empty lines
                words.append(word)
    return words

def md5_hash(text: str) -> str:
    """Compute MD5 of a string and return lowercase hex digest."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def crack_md5(target_hash: str, wordlist: list):
    """
    Compare the target hash against MD5 of every word in the list.
    Returns the plaintext if found, otherwise None.
    """
    target_hash = target_hash.strip().lower()

    # Basic validation: MD5 is always 32 hex characters
    if len(target_hash) != 32 or not all(c in "0123456789abcdef" for c in target_hash):
        return "INVALID_HASH"

    for word in wordlist:
        if md5_hash(word) == target_hash:
            return word
    return None

def main():
    print("=" * 55)
    print("  Simple MD5 Dictionary Cracker")
    print("  (Wordlist loaded from external file)")
    print("=" * 55)

    # Load the wordlist once
    wordlist = load_wordlist(WORDLIST_FILE)
    print(f"[*] Loaded {len(wordlist)} words from {WORDLIST_FILE}")

    # Get the target hash
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("\nEnter MD5 hash: ").strip()

    if not target:
        print("No hash provided.")
        sys.exit(1)

    result = crack_md5(target, wordlist)

    print()
    if result == "INVALID_HASH":
        print("Invalid MD5 hash format. Expected 32 hexadecimal characters.")
    elif result is not None:
        print("[+] MATCH FOUND!")
        print(f"    Hash     : {target.lower()}")
        print(f"    Plaintext: {result}")
    else:
        print("No matching hash identified. Please try again.")
    print()

if __name__ == "__main__":
    main()