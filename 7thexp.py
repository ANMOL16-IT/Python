import requests
import threading
import os
def download_file(url, filename):
    print(f"Starting Download: {filename}")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"Completed: {filename}")
# List of files to download
files = [
    ("https://example.com/file1.pdf", "file1.pdf"),
    ("https://example.com/file2.pdf", "file2.pdf"),
    ("https://example.com/file3.pdf", "file3.pdf"),
]
threads = []
for url, filename in files:
    thread = threading.Thread(
        target=download_file,
        args=(url, filename)
    )
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("\nAll downloads completed!")