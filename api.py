from pytube import YouTube

class API:
    @staticmethod
    def download(url: str) -> str:
        yt = YouTube(url)

        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        streams.download()

        return streams.default_filename