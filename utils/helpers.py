def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1]
    return url.split("/")[-1]