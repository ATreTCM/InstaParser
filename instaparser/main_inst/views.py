from django.shortcuts import render
from django.views.generic import View

from .models import UserInfo, SearchData
from .service import MainInstParser, insta
       
class CreateInstaData(View):
    
    template_name = 'main_inst/index.html'
 
    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        users_value = request.POST.dict()
        data_base = UserInfo()
        search_data = SearchData()
        parse_data = MainInstParser(users_value['search'], insta)
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
            search_data.userInfo_set.add(data_base, bulk =False)
            
        if search_data['download'] == 'on':
            parse_data.download_data()
            
        return render(request, self.template_name)