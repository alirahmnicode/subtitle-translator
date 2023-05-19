"""write new subtitle file"""
import os

import srt


def make_subtitle(subs: list, files_path, file_name):
    """this function creates subtitles compose"""
    if len(subs) > 0:
        # make one list from sublists
        subtitles_list = [sub for sublist in subs for sub in sublist]
        subtitles = srt.compose(subtitles_list)
        sub_file = write_file(subtitles, files_path, file_name)

    return sub_file


def write_file(subs, files_path, file_name):
    """This function writes srt file"""
    with open(os.path.join(files_path, file_name), "w", encoding="utf-8") as f:
        file = f.write(subs)

    return file
