import hashlib

def crack_password_sha256(hash, dictionary_file):
    """
    This function attempts to crack a given SHA-256 hashed password
    using a dictionary attack. It reads through each line of the
    provided dictionary file, hashes the word using SHA-256, and
    compares it to the provided hash.
    """
    with open(dictionary_file, 'r') as file:
        for line in file:
            word = line.strip()
            if hashlib.sha256(word.encode()).hexdigest() == hash:
                return word
    return None

if __name__ == "__main__":
    hashed_password = input("Enter the SHA-256 hashed password: ")
    dictionary = input("Enter the path to the dictionary file: ")

    result = crack_password_sha256(hashed_password, dictionary)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
