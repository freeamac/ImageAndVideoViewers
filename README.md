# Image And Video Viewers

A set of viewers, one for jpeg images and the other for mp4 video files. Each viewer runs off custom defition files constructed in XML.

# ImageViewer
View images based on a custom formatted XML description file

## XML Document Type Definition
This is the Document Type Definition required in the xml file driving the ImageViewer:

```
<!-- DTD for an image slide show -->
<!ELEMENT slideshow (title, copyright?, picture+)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT copyright (#PCDATA)>
<!ELEMENT picture (image, caption, date, location, asa?, roll_num?, roll_max?)>
<!ELEMENT image (#PCDATA)>
<!ELEMENT caption (#PCDATA)>
<!ELEMENT date (#PCDATA)>
<!ELEMENT location (#PCDATA)>
<!ELEMENT asa (#PCDATA)>
<!ELEMENT roll_num (#PCDATA)>
<!ELEMENT roll_max (#PCDATA)>
```

## Key Bindings
In the automated slideshow mode, the following key bindings are available:

| Key Binding | Action |
|---|---|
| \<Esc\> | Exit Slideshow |

In manual display mode, the following key bindings are available:

| Key Binding | Action |
|---|---|
| \<Left\> | Go To Previous Image |
| \<Right\> | Go To Next Image |
| \<Escape\> | Go To First Image |

## Execution

To directly execute via python:

```
$ python3 image_viewer.py
```

## Creating Standalone Executable

Use [PyInstaller](https://pyinstaller.org/en/stable/) as follows in Powershell to create a standalone Windows executable:

```
$ pyinstaller ImageViewer.spec
```

and the standalone executable will be found in the *dist* folder. 

Or download the [current Windows version](https://github.com/freeamac/ImageAndVideoViewers/releases/tag/V1.0-windows)

# Video Viewer

## XML Document Type Definition
This is the Document Type Definition required in the xml file driving the VideoViewer:

```
<!-- DTD for an video show -->
<!ELEMENT videos (title, copyright?, video+)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT copyright (#PCDATA)>
<!ELEMENT video (caption, source, date?, location?)>
<!ELEMENT caption (#PCDATA)>
<!ELEMENT source (#PCDATA)>
<!ELEMENT date (#PCDATA)>
<!ELEMENT location (#PCDATA)>
```

## Key Bindings

The following key bindings are available:

| Key Binding | Action |
|---|---|
| \<Left\> | Go To Previous Video |
| \<Right\> | Go To Next Video |
| \<Escape\> | Go To First Video |

## Execution

<details>

<summary><b>Old information on using cv2 library which did not allow audio with the video</b></summary>

Video replay is dependent on the [opencv library](https://github.com/opencv/opencv). This can be a tricky piece of software to install correctly. On Ubuntu, the following
packages needed to be installed:

```
 $ apt-get install pkg-config
 $ apt-get install -y libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev
```

Even if the above are installed, opencv is picky about the format of the mp4 file. You may need to convert the mp4 file to a format it can process using `ffmeg` as follows:

```
$ apt install ffmpeg
$ ffmpeg -i <input>.mp4 -vf "colorspace=bt709:iall=bt2020:fast=1,format=yuv420p" -c:v libx264 -crf 18 <output>.mp4
```

You will need to do the above if you see errors like the following when processing the video:

```
[swscaler @ 0x40d5f980] Unsupported input (Operation not supported): fmt:yuv420p csp:bt2020c prim:bt2020 trc:unknown -> fmt:bgr24 csp:gbr prim:unknown trc:unknown
```
</details>

### Requirements

The video playing with audio requires the [FFpyPlayer library](https://pypi.org/project/ffpyplayer/). This was used after attempting to use opencv which did not contain support for playing to audio with the video display. Audio now works although it may not match the video frame rate exactly.

See the details section on opencv above if you need to install the FFmpeg library.

Once the requirements are installed, to execute via python:

```
$ python3 video_viewer.py
```

## Creating Standalone Executable

Due to the requirements to run video on differing platforms, no standalone executable is available.
