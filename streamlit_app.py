import streamlit as st
from moviepy.editor import VideoFileClip
import yt_dlp
import os
st.title("youtube'dan gıf yapma aracı")
url=st.text_input("youtube linkini yapıştır")
with st.spinner("video indiriliyor..."):
     ydl_opts={'outtmpl':'input.mp4'}
import yt_dlp;yt_dlp.YoutubeDL().download(ydl_opts,[url])
