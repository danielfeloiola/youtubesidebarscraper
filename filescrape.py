'''
This code will scrape the sidebar recommended videos from a saved
youtube page.  You will need to right click on the page you want to
scrape and choose "save as..." (take note of the full path name to
your file - you will need to enter it when you run the program).

The page is rendered via the Render Class from render_page.py.  
Video link, title, and thumbnail link will be output to a file
in csv format.
'''


from bs4 import BeautifulSoup
from render_page import Render

def write_to_csv(videos):
    ''' Write data to csv formatted file'''    
    
    outputfile = input("What do you want to call your data file?\n")
    print('Writing to "%s"...' % outputfile)
    csv = open(outputfile, "w")
        
    for video in videos:
        try:     
            row = '"' + video['title'] + '", ' \
                + '"' + video['href'] + '", ' \
                + '"' + video['thumbnail'] + '"\n'
            csv.write(row)
        except:
            print("invalid record")
    csv.close()
    
    print('Success!  File closed.')


if __name__ == "__main__":
    
    # Your html filename should be in a format similar to:
    # file:///home/jason/workspace/youtubescrape/TrewsYouTube.html
    url = input("Enter the full path to your saved html file:\n")
    
    result = Render(url)
    page = result.frame.toHtml()
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
    print("Found", len(recommended_videos), "videos.")
    
    write_to_csv(recommended_videos)
