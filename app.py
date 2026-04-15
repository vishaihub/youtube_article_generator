import streamlit as st
from utils.helpers import extract_video_id
from services.transcript import get_transcript
from services.llm_service import generate_article
from services.pdf_service import create_pdf

st.set_page_config(page_title="YouTube Insight Generator")

st.title("🎥 YouTube → Insightful Article Generator")

url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Article"):
    if not url:
        st.warning("Please enter a valid URL")
    else:
        with st.spinner("Processing..."):

            video_id = extract_video_id(url)

            transcript = get_transcript(video_id)

            if "Error" in transcript:
                st.error(transcript)
            else:
                article = generate_article(transcript)

                pdf_path = create_pdf(article)
                with open(pdf_path, "rb") as file:
                    st.download_button(
                        label="📥 Download PDF",
                            data=file,
                            file_name="youtube_article.pdf",
                            mime="application/pdf"
                )
                st.subheader("📄 Generated Article")
                st.write(article)

                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📥 Download PDF",
                        data=f,
                        file_name="article.pdf"
                    )