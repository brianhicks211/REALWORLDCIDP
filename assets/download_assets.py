import urllib.request
import os

# Create the assets folder if it doesn't exist
os.makedirs('assets', exist_ok=True)

# List of media files to download
assets = {
    'marcus.jpg': 'https://images.unsplash.com/photo-1581056771107-24ca5f033842?auto=format&fit=crop&q=80&w=800',
    'sarah.jpg': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&q=80&w=800',
    'david.jpg': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&q=80&w=800',
    'elena.jpg': 'https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&q=80&w=800',
    'julian.jpg': 'https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&q=80&w=800',
    'maya.jpg': 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&q=80&w=800',
    'liam.jpg': 'https://images.unsplash.com/photo-1506869640319-41a49dc8c50e?auto=format&fit=crop&q=80&w=800',
    'clinical_video.mp4': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4' # Safe HD clinical placeholder
}

for filename, url in assets.items():
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, f"assets/{filename}")

print("All assets successfully downloaded for offline use!")