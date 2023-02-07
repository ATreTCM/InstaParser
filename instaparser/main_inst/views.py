from django.shortcuts import render
from django.views.generic import View

from models import UserInfo
from service import MainInstParser, insta

class Create_insta_data(View):
    
    template_name = 'main_inst/index.html'
    context = {}
    
    def post(self, request):
        users_value = request.POST
        data_base = UserInfo()
        parse_data = MainInstParser(users_value, insta)
        parse_data.get_profiles_data()
        for data in parse_data.finish_data_list:
            data_base.url = data['url']
            data_base.avatar_url = data['avatar_url']
            data_base.name = data['name']
            data_base.full_name = data['full_name']
            data_base.bio = data['bio']
            data_base.tags = data['tags']
            data_base.phone = data['phone']
            data_base.link = data['link']
            data_base.posts = data['posts']
            data_base.count_followers = data['count_followers']
            data_base.followers = data['followers']
            data_base.count_following = data['count_following']
            data_base.folowing = data['following']
            data_base.user_id = data['ig_id']
            data_base.save()