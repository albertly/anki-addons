# -*- mode: python; coding: utf-8 -*-
#
# Copyright © 2012 Roland Sieker, ospalh@gmail.com
# Inspiration and source of the URL: Tymon Warecki
#
# License: AGNU GPL, version 3 or later; http://www.gnu.org/copyleft/agpl.html



'''
Download Japanese pronunciations from Japanesepod
'''


import urllib
import os

from aqt import mw
from anki.template import furigana

from process_audio import process_audio
from blacklist import get_hash
from exists import free_media_name


download_file_extension = u'.mp3'


url_jdict='http://assets.languagepod101.com/dictionary/japanese/audiomp3.php?'
# url_jdict='http://assets.languagepod101.com/dictionary/japanese/audioogg.php?'

# Code

def get_word_from_jpod(source):
    kanji, kana = get_kanji_kana(source)
    base_name = build_file_name(kanji, kana)
    get_url = build_query_url(kanji, kana)
    # This may throw an exception
    file_name, retrieve_header = urllib.urlretrieve(
        get_url, os.path.join(mw.col.media.dir(), base_name))
    try:
        file_hash = get_hash(file_name)
    except ValueError:
        os.remove(file_name)
        # Simpler to just raise again
        raise
    # for testing
    # try:
    file_name = process_audio(file_name)
    # except:
    #    pass
    return os.path.basename(file_name), file_hash


def build_query_url(kanji, kana):
        qdict = {}
        if kanji:
            qdict['kanji'] = kanji.encode('utf-8')
        if kana:
            qdict['kana'] = kana.encode('utf-8')
        return url_jdict + urllib.urlencode(qdict)


def build_file_name(kanji, kana):
    """Get a valid download file name."""
    base_name = kanji
    if kana:
        base_name += u'_' + kana
    # Use my function that takes different capitalization rules into
    # account. This may throw a ValueError.
    return free_media_name(base_name, download_file_extension)


def get_kanji_kana(source):
    """Split reading into kanji and kana."""
    kanji = furigana.kanji(source)
    kana = furigana.kana(source)
    #if kanji == kana:
    #    kana = u""
    if not kanji and not kana:
        raise ValueError('Nothing to download')
    return kanji, kana