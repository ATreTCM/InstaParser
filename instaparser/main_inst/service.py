import time
import instaloader
import numpy as np
import re
import config

class InstagramRateController(instaloader.RateController):
    
    def sleep(self, secs):
        delay = np.random.randint(5,15)
        time.sleep(delay)
    
    def query_waittime(self, query_type, current_time, untracked_queries=False):
        return 5.0

insta = instaloader.Instaloader(rate_controller=lambda ctx: InstagramRateController(ctx))


USER = config.inst_login
PASSWORD = config.inst_pass


insta.login(USER, PASSWORD)

class MainInstParser:
    def __init__(self, search_data, insta) -> None:
        self.search_data = search_data
        self.insta = insta
        self.data = instaloader.TopSearchResults(self.insta.context, self.search_data)
        self.finish_data_list = []
        
    def followers_list(self, func):
        followers = []
        for fol in func:
            followers.append(fol.username)
        return followers
    
    def avatar_link(self, url):
        url_re = re.search('(\/)(\d+\S+\w+.jpg)',str(url))
        if url_re:
            return url_re.group(2)
        else:
            return ""
    
    def phone_in_bio(self, bio):
        phone = re.search('\+\d+\S+',str(bio))
        if phone:
            return phone.group(0)
        else:
            return ""
        
    def link_in_bio(self, bio):
        link = re.search('\S+\/\S+',str(bio))
        if link:
            return link.group(0)
        else:
            return ""
        
    def get_profiles_data(self):
        for profile in self.data.get_profiles():
            tags = []
            for index,post in enumerate(profile.get_posts()):
                if index<50:
                    get_tegs=post.caption_hashtags
                    tags.append(get_tegs)
                      
            info = {
                'url': f'https://www.instagram.com/{profile.username}/',
                'avatar_url': self.avatar_link(profile.get_profile_pic_url()),
                'name': profile.username,
                'full_name': profile.full_name,
                'bio': profile.biography,
                'tags': tags,
                'phone': self.phone_in_bio(profile.biography),
                'link': self.link_in_bio(profile.biography),
                'posts': profile.mediacount,
                'count_followers': profile.followers,
                'followers': self.followers_list(profile.get_followers()),
                'count_following': profile.followees,
                'folowing': self.followers_list(profile.get_followees()),
                'ig_id': profile.userid,
                }
            
            self.finish_data_list.append(info)
        
    def download_data(self):
        for profile in self.data.get_profiles():
            insta.download_profilepic(profile)
            for index,post in enumerate(profile.get_posts()):
                if index<50:
                    insta.download_post(post, target=profile.userid)
                   
