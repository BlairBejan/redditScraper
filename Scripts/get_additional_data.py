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
        if comments:
            for comment in comments:
                    comment_text_div = comment.find('div', class_='md')
                    if comment_text_div:
                        comment_text = comment_text_div.text
                        comment_author = comment.find('a', class_='author').text
                        comment_id = comment.find('form')['id'].split('_')[-1]
                        print(comment_text)
                        print (comment_id)
                        print(parent_id)
        
'''
ok for next time i look at this, none of this is really correct or how i want to do this, the way reddit presents the comments in the html is a little strange
the comments will fall under a div like this, this div will group the intirety of 1 comment chain, wether it be one or many we can probebly use this id to group comments
<div class=" thing id-t1_lpglrqx noncollapsed   comment " id="thing_t1_lpglrqx" onclick="click_thing(this)" data-fullname="t1_lpglrqx" data-type="comment" data-gildings="0" data-subreddit="uspolitics" data-subreddit-prefixed="r/uspolitics" data-subreddit-fullname="t5_2qwlq" data-subreddit-type="public" data-author="_gnarlythotep_" data-author-fullname="t2_14un23" data-replies="0" data-permalink="/r/uspolitics/comments/1fryotn/biden_says_harris_handled_everything_from_foreign/lpglrqx/"><p class="parent"><a name="lpglrqx"></a></p><div class="midcol unvoted"><div class="arrow up login-required access-required" data-event-action="upvote" role="button" aria-label="upvote" tabindex="0"></div><div class="arrow down login-required access-required" data-event-action="downvote" role="button" aria-label="downvote" tabindex="0"></div></div><div class="entry unvoted"><p class="tagline"><a href="javascript:void(0)" class="expand" onclick="return togglecomment(this)">[–]</a><a href="https://old.reddit.com/user/_gnarlythotep_" class="author may-blank id-t2_14un23">_gnarlythotep_</a><span class="userattrs"></span> <span class="score dislikes" title="1">1 point</span><span class="score unvoted" title="2">2 points</span><span class="score likes" title="3">3 points</span> <time title="Sun Sep 29 07:33:14 2024 UTC" datetime="2024-09-29T07:33:14+00:00" class="live-timestamp">an hour ago</time>&nbsp;<a href="javascript:void(0)" class="numchildren" onclick="return togglecomment(this)">(0 children)</a></p><form action="#" class="usertext warn-on-unload" onsubmit="return post_form(this, 'editusertext')" id="form-t1_lpglrqxvfm"><input type="hidden" name="thing_id" value="t1_lpglrqx"><div class="usertext-body may-blank-within md-container "><div class="md"><p>Yeah, no shit. VP didn't make the decisions, but it's still a major voice in the room on pretty much every single thing that the oval office does.</p>
</div>
</div></form><ul class="flat-list buttons"><li class="first"><a href="https://old.reddit.com/r/uspolitics/comments/1fryotn/biden_says_harris_handled_everything_from_foreign/lpglrqx/" data-event-action="permalink" class="bylink" rel="nofollow">permalink</a></li><li><a href="javascript:void(0)" data-comment="/r/uspolitics/comments/1fryotn/biden_says_harris_handled_everything_from_foreign/lpglrqx/" data-media="www.redditmedia.com" data-link="/r/uspolitics/comments/1fryotn/biden_says_harris_handled_everything_from_foreign/" data-root="true" data-title="Biden says Harris handled 'everything from foreign policy to domestic policy' under his administration" class="embed-comment">embed</a></li><li class="comment-save-button save-button login-required"><a href="javascript:void(0)">save</a></li><li class="report-button login-required"><a href="javascript:void(0)" class="reportbtn access-required" data-event-action="report">report</a></li><li class="reply-button login-required"><a class="access-required" href="javascript:void(0)" data-event-action="comment" onclick="return reply(this)">reply</a></li></ul><div class="reportform report-t1_lpglrqx"></div></div><div class="child"></div><div class="clearleft"></div></div>
there will be the id for the first comment that is is the entry unvoted div tag also stored in a p "parent" tag
then in this structure there is a child div that will wrap the other comments, but then it continues down with the same parent, child structure.
we are going to have to build our loop not to parse through just all comments but to traverse this html strucure, then we should be able to save, all of the comments,
and maybe an array or something, of all of the parent ids leading up to that comment
'''



parseposts()
