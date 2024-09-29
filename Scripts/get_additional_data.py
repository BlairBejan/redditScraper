from dbfunctions import get_posts
from utils import read_config, get_soup


config = read_config()

user_url = config['user_url']
headers = config['headers']

#soup = get_soup()
    
def parseposts():
    posts = get_posts()
    for post in posts:
        comments_url = post.get('comments_url')
        print(comments_url)
        soup = get_soup(comments_url, headers)
        comments = soup.find_all('div', class_='entry unvoted')
        for comment in comments:
                comment_div = comment.find('div', class_='md')
                
        



parseposts()
