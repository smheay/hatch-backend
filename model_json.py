from Model import Model

import json
import requests
#import multiprocessing 

class model(Model):
    def __init__(self):
        #save for later uses 
        self.json_entries = dict()


    def get_request(tag):
        """
        Takes incoming tag and fetches the API for the appropriate tag
        """
        res = requests.get(f'https://api.hatchways.io/assessment/blog/posts/?tag={tag}')
        response = json.loads(res.text)
     
        return response



    def ping_request():
        """
        Takes incoming ping request and returns success if app is running
        """
        response = {"success" : "true" }

        return response
 
        


    def get_posts_api(tagArr, sortBy, direction):
        """
        tagArr: String science,tech
        sortBy: String (optional) 
            id , reads, likes, popularity
        direction: String (optional)
            desc, asc

        Takes in args and responds with errors or  with dictionary filled with 
        requested information. 

        Includes multiple tags 
        """

        ##check for errors
        if tagArr == None:
            response = {"error": "Tags parameter is required"}
            return response


        sortBy_list = ['id' , 'reads', 'likes', 'popularity']
        if sortBy != None  and  sortBy not in sortBy_list:
            response = {"error": "sortBy parameter is invalid"}
            return response


        direction_list = ['asc' , 'desc']
        if direction != None  and  direction not in direction_list:
            response = {"error": "direction parameter is invalid"}
            return response
        

        ## Sort the tags into a list
        tag_list = tagArr.split(",")
        response = {}


        # Add to the responce with all tags
        for item in tag_list:
            response.update(model.get_request(item))
            

        #remove all duplicates
        #Combine all the results from the API requests above and remove all the repeated posts (try to be efficient when doing this)
        result = {}
        
        for key,value in response.items():
            if value not in result.values():
                result[key] = value


        #Save a value for order
        sortVal = False

        if direction != None:
            if direction == 'desc':
                sortVal = True 

        sort_orders = result["posts"]

        if sortBy != None:
            #Sort the list of dictionaries 
            sort_orders= sorted(sort_orders, key = lambda i: i[sortBy], reverse=sortVal)
            dictReturn = {"posts": sort_orders}
            return dictReturn
    
        

        sort_orders = sorted(sort_orders, key = lambda i: i['id'], reverse=sortVal)
        #Add back to json format return
        dictReturn = {"posts": sort_orders}
        return dictReturn

        
        """
        numProc = multiprocessing.cpu_count()
        p = multiprocessing.Pool(numProc)

        ##add if time left 

        p.close()
        p.join()
        """

        
