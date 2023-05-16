import srt
import asyncio

from google_translate import GoogleTranslate

from .sub import make_subtitle


async def translate_subtitle(file: str, target_l: str, bilingual: bool):
    """This function translates the srt file and returns the translated file."""
    subtitles = list(srt.parse(file))

    all_subs = []
    subtitles_length = len(subtitles)
    chunk = 200

    # split subtitles into sublists
    chunks = [subtitles[x : x + chunk] for x in range(0, subtitles_length, chunk)]

    for subtitles in chunks:
        subs = await asyncio.gather(
            *[translate(target_l, subtitle, bilingual) for subtitle in subtitles]
        )
        # make delay for limited requests
        if len(chunks) > 0:
            await asyncio.sleep(1)
        all_subs.append(subs)

    new_subtitles = make_subtitle(all_subs)

    return new_subtitles


async def translate(target_l, subtitle, bilingual):
    g_t = GoogleTranslate(target_l, subtitle.content)
    translated = await g_t.translate()

    if bilingual:
        new_content = f"{subtitle.content} \n {translated}"
    else:
        new_content = f"{translated}"
    # create subtitle
    sub = srt.Subtitle(
        subtitle.index, start=subtitle.start, end=subtitle.end, content=new_content
    )
    return sub
