from bs4 import BeautifulSoup
from urllib.request import urlopen

def write_to_csv(videos):
    
    print('writing...')
    outputfile = "videos.csv"
    csv = open(outputfile, "w")
        
    for video in videos:
        row = video['title'] + ', ' \
            + video['href'] + ', ' \
            + video['thumbnail'] + '\n'
        print(row)
        csv.write(row)
        
    csv.close()
    
    print('file closed')

if __name__ == "__main__":
    youtube_url = input('video url: ')
    #youtube_url = 'https://www.youtube.com/watch?v=0uUoqD8a0V4'
    page = urlopen(youtube_url).read()
    
    soup = BeautifulSoup(page, "lxml")
    recommended_videos = []
    
    for rec_video in soup.find_all("div", {"class":"content-wrapper"}):
        rec_video = BeautifulSoup(str(rec_video), "lxml")
        link = rec_video.find('a')
        href = link.get('href')
        title = link.get('title')
        thumbnail = href[9:] 
        recommended_videos.append({'title': title, 
                                    'href': 'https://www.youtube.com' + href,
                                    'thumbnail': 'https://i.ytimg.com/vi/' + thumbnail + '/hqdefault.jpg'})
    '''
    for video in recommended_videos:
        print(video, '\n')
    print(len(recommended_videos))
    '''
    write_to_csv(recommended_videos)
