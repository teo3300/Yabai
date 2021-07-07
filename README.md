# Yabai!
## Ed ecco ancora, un' altra reinvenzione di bad apple

What happens when you try to mix up spaghetti code with very little knowledge of whatever you are doing and a popular japanese song from 1998?
An uninviting multiethnic dish.

Too lazy to add some example sorry

## 00.0 Get the video
Our journey begins (with a candy raver) finding some sort of video file from the magic Internet (better if black and white, and I mean ONLY black and white, no grayscale, cause I'm lazy and not able to implement a better method to compress the video, shut up, I'm not some [smartass guy](https://github.com/PeterLemon/GBA/tree/master/Video/Touhou-BadApple!) I don't wanna reinvent LZW, p.s. GUESS WHAT)

## 01.0 Export video frames
Thank you VLC!
So I did't have to manually screenshot around 6k (6575) frames

## 02.0 Decrease bithdepth and framerate
During the process I discovered I'm dumb but not enough to need to reduce the framerate (sorta)

## 03.0 BAE
~~Binary alternation~~ Bad apple encoding: you know, if the only colors you see ar Black and White either you are colorblind or you are me when I'm lazy (if everything is just black you are probably blind, period).
Aaaand... that's how not to reinvent run-length encoding, I do know... BUT I DIDN'T.

## 03.5 BAE Render
Just testing frame rendering on my PC before yeeting everyting in a GBA program

## 04.0 BAE Join
Combine all compressed frames in a single big file of around 3MB (I also made a larger file, a little bigger, that is a C array of the data... did I already mention that I've no idea of what I'm doing?)

## 05.0 Finally some real code
Fuck you python
