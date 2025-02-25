import requests
import sys

site = "https://zaudiobooks.com/"

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



url = "https://files01.freeaudiobooks.top/audio/"

# Open file and read it
f = open("website.txt", "r")

# Skip Lines until we get to "tracks = ["
for line in f:
    if "tracks = [" in line:
        break
f.readline()
f.readline()
f.readline()
f.readline()

for line in f:
    if "name" in line:
        name = line.strip().replace('"', '').replace('\\', "").replace('name: ', "")[:-1] + ".mp3"
        print(f'Downloading {name}')

    if "chapter_link_dropbox" in line:
        url2 = line.strip().replace('"', '').replace('\\', "").replace("chapter_link_dropbox: ", "")[:-1]
        r = requests.get(url + url2)
        with open(name, 'wb') as outfile:
            outfile.write(r.content)
        print(f"Finished Downloading {name}")
    
    if "]," in line:
        print("-----Audiobook Download Complete-----")
        break

f.close()