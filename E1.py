import requests
video_id = "bw7bVpI5VcM"
api_key = "AIzaSyC6ZHngVmQRc6VdyF4cY0F-wL68X2uzZvk"
video_info_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
video_info_response = requests.get(video_info_url)
video_info_data = video_info_response.json()
print("\nVideo Information Data:\n")
video_info_data

comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()
print("\nComments Data in Video:\n")
comments_data

comments = [item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]for item in comments_data["items"]]
print("\nRAW Comments:\n")
comments