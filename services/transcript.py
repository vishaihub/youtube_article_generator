from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, translate_to_english=False):
    try:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, languages=['en', 'hi']
            )
        except:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)

        text = " ".join([t['text'] for t in transcript])
        return text

    except Exception as e:
        return f"Error fetching transcript: {str(e)}"
