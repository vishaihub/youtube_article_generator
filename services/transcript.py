from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()

        if hasattr(api, "fetch"):
            transcript = api.fetch(video_id, languages=['en', 'hi'])
            text = " ".join([t.text for t in transcript])
        else:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi'])
            text = " ".join([t['text'] for t in transcript])

        return text

    except Exception as e:
        return f"Error fetching transcript: {str(e)}"
