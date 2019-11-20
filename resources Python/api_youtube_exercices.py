import requests, json

class youtube_api:
    api_key = "AIzaSyDkICKG01px6a_jFXU9X9HsDc5tvOMDmK0"
    http_header = {'accept-encoding':'gzip'}

    def __valid_request(self, response):
        if response.status_code == requests.codes.ok:
            return True
        else:
            response_json = response.json()
            print "Error : %s\n" % (response_json["error"]["message"])
            return False

    #def search_videos(self, vid):
    def search_videos(self, list_terms):
        params = {"key" : self.api_key, "part": "id",  "type": "video", "q": "|".join(list_terms), "maxResults": 1}
        resp = requests.get("https://www.googleapis.com/youtube/v3/search", params, headers=self.http_header)

        list_vid = []

        if self.__valid_request(resp):
            resp_js = resp.json()
            #print json.dumps(resp_js, indent=2, sort_keys=True)
            for item in resp_js["items"]:
                list_vid.append(item["id"]["videoId"])

        return list_vid

    def get_video_information(self, vid):
        params = {"key" : self.api_key, "part": "snippet,statistics,topicDetails", "id": vid}
        resp = requests.get("https://content.googleapis.com/youtube/v3/videos", params, headers=self.http_header)


        if self.__valid_request(resp):
            resp_js = resp.json()
            print json.dumps(resp_js, indent=2, sort_keys=True)

            for item in resp_js["items"]:
                return item["statistics"]
                #print json.dumps(resp_js[], indent=2, sort_keys=True)

    def get_most_similar(self, vid):
        params = {"key" : self.api_key, "part": "id", "type": "video", "order": "relevance", "relatedToVideoId": vid, "maxResults": 1}
        resp = requests.get("https://www.googleapis.com/youtube/v3/search", params, headers=self.http_header)

        if self.__valid_request(resp):
            resp_js = resp.json()
            print json.dumps(resp_js, indent=2, sort_keys=True)


ya = youtube_api()
#ya.search_videos("4Mn0-lfYAa4")
list_vid = ya.search_videos(["surf pacific ocean"])

list_link_vid = []

# for vid in list_vid:
#     list_link_vid.append("https://www.youtube.com/watch?v=" + vid)
#
# print list_link_vid
information_video = {}

for vid in list_vid:
    information_video[vid] = ya.get_video_information(vid)

for vid in list_vid:
    ya.get_most_similar(vid)
