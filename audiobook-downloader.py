import requests
import sys

site = "https://naudios.com/"

# Process the command line
if len(sys.argv) != 2:
    print('Usage: python', sys.argv[0], f'<{site}your-book-here>')
    sys.exit()
if site not in sys.argv[1] or len(site) >= len(sys.argv[1]):
    print(f'Please provide a {site} link')
    sys.exit()

# Get Website Source Code
website = sys.argv[1]
r = requests.get(website).text

with open("website.txt", "w", encoding="utf-8") as f:
    f.write(r)

f = open("website.txt", "r", encoding="utf-8")

# Skip lines until we get to links to mp3
for line in f:
    if "track-item active" in line:
        break
f.readline()

print("-----Audiobook Download Starting-----")
for line in f:
    # Link to audio file
    src = line.strip().replace("data-src=", '').replace('"', '').replace('>', '').replace("amp;", '')
    f.readline()

    # Name of file
    name = f.readline().strip().replace("</div>", '').replace("â€“", '-').replace(' ', '') + ".mp3"

    if "Footer" in name:
        print("-----Audiobook Download Complete-----")
        break

    # Download file
    print(f"Downloading {name}")
    audio = requests.get(src)
    with open(name, 'wb') as outfile:
        outfile.write(audio.content)
    print(" Download Finished")

    # Skip empty and /div lines
    f.readline()
    f.readline()
    f.readline()

    

f.close()