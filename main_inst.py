"""Пользователи у которых в название или в профайле есть: los angeles Photographer

Количество пользователей: 200 шт популярных (имеется ввиду у кого больше всего подписчиков)"""

import time
import instaloader
import numpy as np
import re
import csv

class InstagramRateController(instaloader.RateController):
    
    def sleep(self, secs):
        delay = np.random.randint(5,15)
        time.sleep(delay)
    
    def query_waittime(self, query_type, current_time, untracked_queries=False):
        return 5.0

insta = instaloader.Instaloader(rate_controller=lambda ctx: InstagramRateController(ctx))


USER = 'tretiakov306'
PASSWORD = 'fkbcf2018'


insta.login(USER, PASSWORD)
   


search_data = [
    'los angeles videographer',
    'LA videographer',
    'California videographer',
    'California photographer',
    'los angeles photographer',
    'LA photographer',
    'Фотограф Лос-Анджелес',
]

data_list = []
data_id = []

def fol_list(func):
    followers=[]
    for fol in func:
            followers.append(fol.username)
    return followers
            
def avatar_link(url):
    url_re = re.search('(\/)(\d+\S+\w+.jpg)',str(url))
    if url_re:
        return url_re.group(2)
    else:
        return ""

def phone_in_bio(bio):
    phone = re.search('\+\d+\S+',str(bio))
    if phone:
        return phone.group(0)
    else:
        return ""
        
def link_in_bio(bio):
    link = re.search('\S+\/\S+',str(bio))
    if link:
      return link.group(0)
    else:
      return ""
      
def get_profiles_data(insta, search):
    
    print('start')
    id_list = []
    with open('users.txt') as user_id_done:
        for id_done in user_id_done:
          id_list.append(id_done.strip())
    data = instaloader.TopSearchResults(insta.context, search)
    number = 1
    for profile in data.get_profiles():
        if str(profile.userid) not in id_list:
            tags = []
            insta.download_profilepic(profile)
            for index,post in enumerate(profile.get_posts()):
                if index<50:
        
                    insta.download_post(post, target=profile.userid)
                        
                    get_tegs=post.caption_hashtags
                    tags.append(get_tegs)
                      
            info = {
                '#': number,
                'url': f'https://www.instagram.com/{profile.username}/',
                'avatar_url': avatar_link(profile.get_profile_pic_url()),
                'name': profile.username,
                'full_name': profile.full_name,
                'bio': profile.biography,
                'tegs': tags,
                'phone': phone_in_bio(profile.biography),
                'link': link_in_bio(profile.biography),
                'posts': profile.mediacount,
                'count_followers': profile.followers,
                'followers': fol_list(profile.get_followers()),
                'count_following': profile.followees,
                'folowing': fol_list(profile.get_followees()),
                'ig_id': profile.userid,
                }
            
                
            number += 1
            
            data_list.append(info)
            with open('data.txt','w') as user_data:
                user_data.write(str(data_list))
            print(f'{profile.username} done')
            data_id.append(str(profile.userid))
            with open('users_id.txt', 'w') as users_done:
                users_done.write(str(data_id))

def main():        
    for search in search_data:
        get_profiles_data(insta, search)
    print('Finish')
    
    with open(f"instagram.cvs", "w") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                '№',
                'url пользователя',
                'Аватарка (сохранить в папку пользователя)',
                'Логин',
                'Фио',
                'Подпись',
                'Теги (Все теги из 50 постов)',
                'Телефон (если есть продублировать в новое поле)',
                'Cсылка (если есть продублировать в новое поле)',
                'Поличество постов',
                'Количество Читачів',
                'Списко пользователей - Читачів',
                'Количество Стежить',
                'Списко пользователей - Стежать',
                'Название папки где сохранены, из 50 постов все фото',
            )
        )

    for data in set(data_list):
        with open(f"instagram.cvs", "a") as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    data["#"],
                    data["url"],
                    data["avatar_url"],
                    data["name"],
                    data["full_name"],
                    data["bio"],
                    data["tegs"],
                    data["phone"],
                    data["link"],
                    data["posts"],
                    data["count_followers"],
                    data["followers"],
                    data["count_following"],
                    data["folowing"],
                    data["ig_id"],
                )
            )
    print('csv done')
    
    
        
if __name__ == '__main__':
    main()