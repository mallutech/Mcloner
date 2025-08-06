import os
import requests

# Create folder structure if not exists
os.makedirs("checkpoints/converter", exist_ok=True)

# URL for downloading the real converter.pth file
url = "https://huggingface.co/myshell-ai/OpenVoice/resolve/main/checkpoints/converter/converter.pth"

# Local path to save the downloaded file
save_path = "checkpoints/converter/converter.pth"

# Download and save the file
print("🔁 Downloading converter.pth...")
response = requests.get(url, stream=True)
with open(save_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
print("✅ converter.pth downloaded successfully.")
