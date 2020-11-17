from dao import VideoDao


def load_video():
    result = VideoDao.load_video()
    urls = {row[0]: row[1] for row in result}
    return urls
