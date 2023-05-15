"""write new subtitle file"""
import srt


def make_subtitle(subs: list):
    """this function creates subtitles compose"""
    if len(subs) > 0:
        # make one list from sublists
        subtitles_list = [sub for sublist in subs for sub in sublist]
        subtitles = srt.compose(subtitles_list)
        sub_file = write_file(subtitles)

    return sub_file


def write_file(subs):
    """This function writes srt file"""
    with open("new.srt", "w", encoding="utf-8") as f:
        file = f.write(subs)

    return file
