import requests
import hashlib

url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'  # Replace with the actual URL
response = requests.get(url)

file_content = response.content

file_hash = hashlib.sha256(file_content).hexdigest()

# Save the hash to a file
with open('hash.txt', 'w') as hash_file:
    hash_file.write(file_hash)

# Save the file
with open('output_file.csv', 'wb') as f:
    f.write(file_content)

# Check if file_content is not empty
if file_content:
    print('File has been extracted successfully.')
else:
    print('Failed to extract the file.')



