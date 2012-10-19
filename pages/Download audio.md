title: Download audio
id: dlaudio
main_file: Download audio.py
status: undocumented
type: addon
status_color: red
status_text_color: white
abstract: Automatically download audio from Google TTS and Japanesepod
first_image: Downloaded audio.png
first_alt: Reviewing downloaded audio files.
extra_jq_script: audio_tips.js

Automatically download audio from Google TTS and Japanesepod.

This add-on adds three menu items, “Note audio”, “Side audio” and
“Manual audio”, that all try to download audio in slightly different
manners.

## Please be patient

While the add-on is pretty much finished, this manual page is
not. Please be patient.

## Fields
The download mechanism looks for audio fields to store the information
in, according to two rules:

* When there is a field called “<span class="qtbase
  ignorecase">Expression</span>”, “<span class="qtbase
  ignorecase">Front</span>”, or “<span class="qtbase
  ignorecase">Back</span>”, the add-on looks for a field called “<span
  class="qtbase ignorecase">Audio</span>” or “<span class="qtbase
  ignorecase">Sound</span>”.
* For other fields, the add-on looks for a second field with the same
  name with “Audio” or “Sound” added. Like this, one note can store
  different audio files for differnt fields. For example, a geography
  deck can have fields “Country” and “Capital”. When that note
  also has fields “Country Audio” and “Capital Audio”, the add-on can
  download pronunciation for these two fields separately.

### Japanesepod

reading instead of Expression

### Change

in `downloadaudio/download.py`

## Manual, note, side

Two of the three download modes, note and side mode, immediately
download the audio when triggered. The note mode checks all the fields
of the card.

### Manual



### Review

#### Japanesepod

Blacklist



## Language

There are up to four ways the download language is determined

* For manual downloads, the language code can be set in the dialog.
* The language code can be set as a tag on individual cards
* ... settings ...
* ... default ...

## Google TTS

Caveat emptor robot voice

## Japanesepod

Split kana kanji

## Private use

These audio files can be freely downloaded without registering or
agreeing to a license, they keep the copyright of those providing
them. While i see no problem with using them privately, re-publishing,
for example by uploading a shared deck to Ankiweb, is most likely
prohibited by those rights.

## Pysox and Pydub

Get them.

## Ideas for improvements
While this add-on works as it is, a few things would be nice.

 * Automatically edit the information before the request is sent. I use
   what i call “electric” cards for Japanese verbs, where the
   different forms are formed automatically. That means that the whole
   word doesn’t actually appear on the card. While it is no big
   problem to complete the word in the “Manual audio” dialog, the
   add-on could automatically add the 「る」 for 一段動詞.