'''
This code will scrape the sidebar recommended videos from a saved youtube page.
You need to right click on the page you want to scrape and choose "save as..."

'''


from bs4 import BeautifulSoup
from render_page import Render

def write_to_csv(videos):
    
    outputfile = input("What do you want to call your data file?\n")
    print('Writing to "%s"...' % outputfile)
    csv = open(outputfile, "w")
        
    for video in videos:
        row = '"' + video['title'] + '", ' \
            + '"' + video['href'] + '", ' \
            + '"' + video['thumbnail'] + '"\n'
        csv.write(row)
        
    csv.close()
    
    print('Success!  File closed.')

if __name__ == "__main__":

    url = input("Enter the full path to your saved html file:\n")
    #url = "file:///home/jason/workspace/youtubescrape/TrewsYouTube.html"
    
    r = Render(url)
    page = r.frame.toHtml()
    
    soup = BeautifulSoup(page, "lxml")
 
    recommended_videos = []    
    
    for rec_video in soup.find_all("a", {"class":"yt-simple-endpoint style-scope ytd-compact-video-renderer"}):
        
        rec_video = BeautifulSoup(str(rec_video), "lxml")
        
        link = rec_video.find('a')
        href = link.get('href')
        
        span = rec_video.find('span')
        title = span.get('title')
    
        thumbnail = 'https://i.ytimg.com/vi/' + href[-11:] + '/hqdefault.jpg' 
        recommended_videos.append({'title': title, 
                                    'href': href,
                                    'thumbnail': thumbnail })
    
    #for video in recommended_videos:
    #    print(video, '\n')
    #print(len(recommended_videos))
    
    write_to_csv(recommended_videos)
