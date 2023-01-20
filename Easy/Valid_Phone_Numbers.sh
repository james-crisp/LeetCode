# Read from the file file.txt and output all valid phone numbers to stdout.
# James Crisp

input="file.txt"
while IFS= read -r line; do
    echo "$line"
done < file.txt