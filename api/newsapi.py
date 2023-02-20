import requests
import os

class news_api():
    def __init__(self):
        self.api ='pub_169289543874a9b46fae2bb5ce175f2858e64'


    def get_sports_new(self,category='sports',country='us'):
        title = []
        pub_date = []
        full_description = []
        creator = []
        top_10 = [0,1,2,3,5,6,7,8,9]

        try:
            re = requests.get('https://newsdata.io/api/1/news?apikey=' + self.api+ '&country=' + country + '&category=' + category + '&language=en&page=16766087997e6002b41d3c0eabf39000335af1a919')
            response = re.json()
            print(response['nextPage'])
            for i in range(10):
                
                
                if response['results'][i]['title']:

                    title.append(response['results'][i]['title'])
                else:
                    title.append('Information not aviable')
                

                if response['results'][i]['creator']:

                    creator.append(response['results'][i]['creator'])
                else:
                    creator.append('Information not aviable')

                if response['results'][i]['pubDate']:
                    pub_date.append(response['results'][i]['pubDate'])
                else:
                    pub_date.append('Information not aviable')
                
                if response['results'][i]['content']:

                    full_description.append(response['results'][i]['content'])
                else:
                    full_description.append('Information not aviable')

            return {title[i]: [creator[i],pub_date[i],full_description[i]] for i in range(len(title))}
        except Exception as e:
            raise e



    
    def get_detail(self,q):
        try:
            re = requests.get('https://newsdata.io/api/1/news?apikey='+ self.api+ '&qInTitle='+str(q))
            response = re.json()
            print(response)
            return response
            
        except Exception as e:
            raise(e)


    

    
