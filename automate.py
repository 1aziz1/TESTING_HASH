import requests
import hashlib
import os

url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
file_path = 'output_file.csv'
hash_file_path = 'hash.txt'

# Step 1: Download the File and Save a Hash
response = requests.get(url)
new_file_content = response.content

# Compute the hash of the file content
new_file_hash = hashlib.sha256(new_file_content).hexdigest()

# Save the hash to a file
with open(hash_file_path, 'w') as hash_file:
    hash_file.write(new_file_hash)

# Save the file
with open(file_path, 'wb') as f:
    f.write(new_file_content)

# Step 2: Check if the File has Changed
if os.path.exists(hash_file_path):
    # Compare the new hash with the saved hash
    with open(hash_file_path, 'r') as hash_file:
        saved_hash = hash_file.read()

    if new_file_hash != saved_hash:
        # The file has changed; download the updated version
        with open(file_path, 'wb') as f:
            f.write(new_file_content)

        # Save the new hash
        with open(hash_file_path, 'w') as hash_file:
            hash_file.write(new_file_hash)
        print("File has changed. Updated version downloaded.")
    else:
        print("The file has not changed.")
else:
    print("No previous hash found. Initial download completed.")
