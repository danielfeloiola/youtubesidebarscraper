from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == "__main__":
    #watch_id = input('video watch id: ')
    youtube_url = 'https://www.youtube.com/watch?v=0uUoqD8a0V4'
    page = urlopen(youtube_url).read()
    
    soup = BeautifulSoup(page, "lxml")
    recommended_videos = []
    
    for rec_video in soup.find_all("div", {"class":"content-wrapper"}):
        recommended_videos.append(BeautifulSoup(str(rec_video)))
        
    print(recommended_videos)
    print(len(recommended_videos))
    
