import pytube

url=input("Enter video URL: ")
path="D:\june 2024 learnings"
pytube.YouTube(url).streams.get_highest_resolution().download(path)