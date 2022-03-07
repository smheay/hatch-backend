import random
from model_json import model


class test_model():
    def __init__():
        pass

    def test_ping_request():

        mylist = model.ping_request()

        success_check = {"success" : "true" }
        
        assert mylist == success_check, "Page is not runnig."

        return 




    def test_get_posts_api():

        tagArr = ['history' , 'tech', 'design', 'culture', None]
        sortBy_list = ['id' , 'reads', 'likes', 'popularity']
        direction_list = ['asc' , 'desc']

        #sortBy = random.choices(sortBy_list, weights = [1, 1, 1, 1, 10], k = random(0,4))
        #sortBy = random.choices(sortBy_list, weights = [1, 1, 1, 1, 10], k = 1)
        #direction = random.choices(direction_list, weights = [1, 1, 10], k = 1)



        mylist = model.get_posts_api( None,None,None)
        return_check = {"error": "Tags parameter is required"}
        assert mylist == return_check, "Tag no args feature is not working"


        mylist = model.get_posts_api( tagArr[3],None,None)
        return_check = list(mylist.keys())
        assert return_check[0] == 'posts', "Tag with args feature is not working"


        mylist = model.get_posts_api( 'history,tech,design' ,None,None)
        return_check = list(mylist.keys())
        assert return_check[0] == 'posts', "Tag with multi args feature is not working"



        for item in direction_list:
            mylist = model.get_posts_api( tagArr[2], None, item)
            return_check = list(mylist.keys())
            assert return_check[0] == 'posts', "direction_list with args feature is not working"
        
        for item in sortBy_list:
            mylist = model.get_posts_api( tagArr[2], item, None)
            return_check = list(mylist.keys())
            assert return_check[0] == 'posts', "direction_list with args feature is not working"

        return 