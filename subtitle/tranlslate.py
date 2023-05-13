import srt
import asyncio

from google_translate import GoogleTranslate

async def translate_subtitle(file: str, target_l: str):
    """This function translates the srt file and returns the translated file."""
    subtitles = list(srt.parse(file))

    all_subs = []
    subtitles_length = len(subtitles)
    chunk = 200

    # split subtitles into sublists
    chunks = [subtitles[x:x+chunk] for x in range(0, subtitles_length, chunk)]

    for subtitles in chunks:
        subs = await asyncio.gather(*[translate(target_l, subtitle) for subtitle in subtitles])
        # make delay for limited requests
        if len(chunks) > 0:
            await asyncio.sleep(1)
        all_subs.append(subs)

    new_subtitles = srt.compose(all_subs[0])
    
    return new_subtitles



async def translate(target_l, subtitle):
    g_t = GoogleTranslate(target_l, subtitle.content)
    translated = await g_t.translate()
    new_content = f"{subtitle.content} \n {translated}"
    # create subtitle
    sub = srt.Subtitle(subtitle.index, start=subtitle.start, end=subtitle.end, content=new_content)
    return sub
    
