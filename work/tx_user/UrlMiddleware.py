
class url():
    def prosess_response(self,request,response):
        url_list=[
            '/user/register',
            '/user/register_handle',
            '/user/register_exist',
            '/user/login_handle',
            '/user/login',
            '/user/logout'
        ]
        if not request.is_ajax() and request.path not in url_list:
            request.set_cookie('red_url', request.get_full_path())
        return response




