from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, translate_to_english=False):
    try:
        api = YouTubeTranscriptApi()

        # Get all available transcripts
        transcript_list = api.list(video_id)

        # Step 1: Try manually created transcript
        try:
            transcript = transcript_list.find_manually_created_transcript(
                [t.language_code for t in transcript_list]
            )
        except:
            # Step 2: Fallback to auto-generated
            transcript = transcript_list.find_generated_transcript(
                [t.language_code for t in transcript_list]
            )

        # Step 3: Translate if needed
        if translate_to_english:
            transcript = transcript.translate('en')

        # Step 4: Fetch data
        data = transcript.fetch()

        # Step 5: Convert to text
        text = " ".join([item.text for item in data])

        return text

    except Exception as e:
        return f"Error fetching transcript: {str(e)}"