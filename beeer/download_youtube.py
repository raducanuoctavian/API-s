import os
import youtube_dl
from flask import Flask, request, send_file

app = Flask(__name__)

# Set up the API route
@app.route("/download_video", methods=["GET"])
def download_video():
    # Get the URL of the YouTube video from the query string
    video_url = request.args.get("url")


    # Set the YouTube video download options
    ydl_opts = {
        "outtmpl": "/%(title)s.%(ext)s",
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4'
    }

    # Download the YouTube video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Get the filename of the downloaded video
    video_title = ydl.extract_info(video_url, download=False)["title"]
    video_filename = video_title + ".mp4"

    # Return the downloaded video as a response
    return send_file(video_filename,
                     as_attachment=True)

if __name__ == "__main__":
    app.run()