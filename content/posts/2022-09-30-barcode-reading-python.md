---
title: "The Best Python Packages for Reading Barcodes"
slug: the-best-python-packages-for-reading-barcodes
date: "2022-09-30"
updated_date: "2023-06-15"
tags:
 - factorytech
 - python
 - barcodes
published: true
---

Three years ago I published a blog post on [how to _generate_ barcodes using Python]({{< ref "2019-01-23-barcode-generation-python" >}}). It's one of the most visited posts on the blog! Occasionally a reader emails to ask: "But what if I want to _read_/_decode_/_scan_[^1] a barcode, not write it?"

Here is the answer:

## Don't use Python for Barcode Decoding!

You really shouldn't be using pure Python to decode barcodes from images or videos or, worse, from camera streams.

For best performance[^2], use purpose-built barcode reader hardware whenever possible. These devices can optimize every step in the barcode decoding pipeline which starts with capturing photons of light and ends with bits of data. For example, a barcode reading device can use lenses and sensors that optimize for barcode contrast but don't yield realistic images. That's obviously not an option in a smartphone that must also work as a general-purpose camera.

Even if dedicated hardware is not an option, stay as low level as possible for as much of the barcode reading process as possible. If the barcode reading happens on a computing device that runs Python, this usually means using a compiled language for the heavy lifting.

You have considered every possible other option and still want to decode barcodes with Python? Then you are probably in the market for a Python package that wraps a barcode reading library written in another language.

## Recommended Package

**[zxing-cpp](https://pypi.org/project/zxing-cpp/) is the best Python package for reading barcodes. Here is why:**

1. It is straightforward to install, including on Windows. Most of the alternatives require separate install steps for their non-Python dependencies.
2. It wraps the C++ port of the zxing library. Of the three common "wrapped" libraries, zxing C++ supports the most barcode symbologies and reads more barcodes in my test images than the others.
3. Both the Python wrapper and the wrapped library are actively maintained as of September 2022.

## Runners Up

If you are specifically looking for a Python wrapper for zbar, then [**pyzbar**](https://pypi.org/project/pyzbar) is the most likely to work out-of-the-box for most users.

If you are looking for a wrapper for the original zxing, which is written in Java, use the [**zxing**](https://pypi.org/project/zxing) Python package. But be warned: It only reads one barcode per image.

Commercial barcode reading SDKs generally outperform open-source software. However, most products are geared towards mobile platforms, offering bindings for every mobile app development framework under the sun, but not Python. Two options with ready-to-use Python support are covered at the end of this post.

## Overview Tables

### Python wrapper packages

The following table compares Python packages that you may stumble across when searching PyPI for keywords related to barcode decoding.

Instead of repetitively listing the supported [barcode symbologies]({{< ref "2017-02-26-intro-to-barcode-readers" >}}#barcode-formats) of each library, the table shows which non-Python library each Python package wraps. You can look up the features of the wrapped libraries in the next table below.

<table class="comparison-table">
  <tr>
    <th>Package</th>
    <th>last updated</th>
    <th>License</th>
    <th><img style="width: 0.8em" alt="Octocat (Github logo)" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpFNTE3OEEyQTk5QTAxMUUyOUExNUJDMTA0NkE4OTA0RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFNTE3OEEyQjk5QTAxMUUyOUExNUJDMTA0NkE4OTA0RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkU1MTc4QTI4OTlBMDExRTI5QTE1QkMxMDQ2QTg5MDREIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkU1MTc4QTI5OTlBMDExRTI5QTE1QkMxMDQ2QTg5MDREIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+m4QGuQAAAyRJREFUeNrEl21ojWEYx895TDPbMNlBK46IUiNmPvHBSUjaqc0H8pF5+aDUKPEBqU2NhRQpX5Rv5jWlDIWlMCv7MMSWsWwmb3tpXub4XXWdPHvc9/Gc41nu+nedc7/8r/99PffLdYdDPsvkwsgkTBwsA/PADJCnzX2gHTwBt8Hl7p537/3whn04XoDZDcpBlk+9P8AFcAghzRkJwPF4zGGw0Y9QS0mAM2AnQj77FqCzrtcwB1Hk81SYojHK4DyGuQ6mhIIrBWB9Xm7ug/6B/nZrBHBegrkFxoVGpnwBMSLR9EcEcC4qb8pP14BWcBcUgewMnF3T34VqhWMFkThLJAalwnENOAKiHpJq1FZgI2AT6HZtuxZwR9GidSHtI30jOrbawxlVX78/AbNfhHlomEUJJI89O2MqeE79T8/nk8nMBm/dK576hZgmA3cp/R4l9/UeSxiHLVIlNm4nFfT0bxyuIj7LHRTKai+zdJobwMKzcZSJb0ePV5PKN+BqAAKE47UlMnERELMM3EdYP/yrd+XYb2mOiYBiQ8OQnoRBlXrl9JZix7D1pHTazu4MoyBcnYamqAjIMTR8G4FT8LuhLsexXYYjICBiqhQBvYb6fLZIJCjPypVvaOoVAW2WcasCnL2Nq82xHJNSqlCeFcDshaPK0twkAhosjZL31QYw+1rlMpWGMArl23SBsZZO58F2tlJXmjOXS+s4WGvpMiBJT/I2PInZ6lIs9/hBsNS1hS6BG0DSqmYEDRlCXQrmy50P1oDRKTSegmNbUsA0zDMwRhPJXeCE3vWLPQMvan6X8AgIa1vcR4AkGZkDR4ejJ1UHpsaVI0g2LInpOsNFUud1rhxSV+fzC9Woz2EZkWQuja7/B+jUrgtIMpy9YCW4n4K41YfzRneW5E1KJTe4B2Zq1Q5EHEtj4U3AfEzR5SVY4l7QYQPJdN2as7RKBF0BPZqqH4VgMAMBL8Byxr7y8zCZiDlnOcEKIPmUpgB5Z2ww5RdOiiRiNajUmWda5IG6WbhsyY2fx6m8gLcoJDJFkH219M3We1+cnda93pfycZpIJEL/s/wSYADmOAwAQgdpBAAAAABJRU5ErkJggg==" />★</th>
    <th>wraps what?</th>
    <th>input formats</th>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/pyzbar">pyzbar</a></td>
    <td>Mar 2022</td>
    <td>MIT</td>
    <td>523</td>
    <td>new zbar</td>
    <td>pillow, OpenCV, imageio, numpy ndarrays, raw bytes</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/zxing">zxing</a></td>
    <td>Nov 2021</td>
    <td>LGPLv3+</td>
    <td>88</td>
    <td>zxing</td>
    <td>pillow, file path</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/zbarlight">zbarlight</a></td>
    <td>Jan 2020</td>
    <td>BSD</td>
    <td>158</td>
    <td>new zbar</td>
    <td>pillow</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/fastzbarlight">fastzbarlight</a></td>
    <td>Dec 2016</td>
    <td>BSD</td>
    <td>—</td>
    <td>original zbar</td>
    <td>(fork of zbarlight with vendored original zbar)</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/pyzbar-x">pyzbar-x</a></td>
    <td>Oct 2020</td>
    <td>MIT</td>
    <td>9</td>
    <td>new zbar</td>
    <td>fork of pyzbar</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/zbar-py">zbar-py</a></td>
    <td>Dec 2016</td>
    <td>MIT</td>
    <td>81</td>
    <td>original zbar</td>
    <td>numpy array</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/libzbar-cffi">libzbar-cffi</a></td>
    <td>May 2016</td>
    <td>BSD</td>
    <td>13</td>
    <td>original zbar</td>
    <td>pillow, numpy arrays</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/zbar/">zbar</a></td>
    <td>Nov 2009</td>
    <td>LGPL 2.1</td>
    <td>—</td>
    <td>original zbar</td>
    <td>does not work with Python 3</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/libzbar-ctypes">libzbar-ctypes</a></td>
    <td>May 2017</td>
    <td>LGPL</td>
    <td>0</td>
    <td>original zbar</td>
    <td>pillow</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/pyzxing/">pyzxing</a></td>
    <td>Jan 2022</td>
    <td>MIT</td>
    <td>108</td>
    <td>zxing</td>
    <td>file path, numpy array</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/zxing-cpp/">zxing-cpp</a></td>
    <td>Jul 2022</td>
    <td>Apache 2.0</td>
    <td>(647)</td>
    <td>zxing C++</td>
    <td>pillow, OpenCV</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/zxinglight">zxinglight</a></td>
    <td>Mar 2019</td>
    <td>MIT</td>
    <td>8</td>
    <td>an unmaintained zxing C++ port</td>
    <td></td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/pylibdmtx">pylibdmtx</a></td>
    <td>Mar 2022</td>
    <td>MIT</td>
    <td>103</td>
    <td>libdmtx</td>
    <td>pillow, OpenCV, imageio, numpy ndarrays, raw bytes</td>
  </tr>

  <tr>
    <td><a href="https://pypi.org/project/dbr">dbr</a></td>
    <td>Aug 2022</td>
    <td>commercial</td>
    <td></td>
    <td>Dynamsoft</td>
    <td ></td>
  </tr>

</table>


### The wrapped libraries

<table class="comparison-table">
  <tr>
    <th></th>
    <th class="text-center"><div><span>zbar</span></div></th>
    <th class="text-center"><div><span>zxing</span></div></th>
    <th class="text-center"><div><span>zxing C++</span></div></th>
    <th class="text-center"><div><span>libdmtx</span></div></th>
  </tr>
  <tr>
    <td>Language</td>
    <td class="text-center">C</td>
    <td class="text-center">Java</td>
    <td class="text-center">C++</td>
    <td class="text-center">C</td>
  </tr>
  <tr>
    <td>License</td>
    <td class="text-center">LGPL 2.1</td>
    <td class="text-center">Apache 2.0</td>
    <td class="text-center">Apache 2.0</td>
    <td class="text-center">custom</td>
  </tr>

  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Codabar">Codabar</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Code-39">Code 39</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Code-93">Code 93</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Code-128">Code 128</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/GS1-DataBar-Omnidirectional">GSI Databar (RSS)</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Interleaved-2-of-5">Int. 2 of 5</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/UPC-A">UPC-A & E</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/EAN-13">EAN-8 & 13</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Aztec-Code">Aztec</a></td>
    <td class="text-center"></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/GS1-DataMatrix">Datamatrix</a></td>
    <td class="text-center"></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/MaxiCode">Maxicode</a></td>
    <td class="text-center"></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/PDF417">PDF417</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/QR-Code">QR</a></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/bwipp/postscriptbarcode/wiki/Micro-QR-Code">Micro QR</a></td>
    <td class="text-center"></td>
    <td class="text-center"></td>
    <td class="text-center"> ✓ </td>
    <td class="text-center"></td>
  </tr>

</table>

## More about zbar, zxing, and zxing C++

Python packages for reading barcodes are Python wrappers around non-Python barcode reading software. They differ in which non-Python software they wrap, how they do the wrapping, and the implications of those two choices for ease of installation.

The three general purpose open source libraries for which Python wrappers exist on PyPI are: zbar, zxing, and zxing C++. Libdmtx is a special purpose library for Datamatrix codes only.

### zbar

The name "zbar" is used for two-and-a-half different pieces of software:

* [The new zbar](https://github.com/mchehab/zbar/) is a software written in C with bindings for various languages. It is a maintained fork of the original zbar.
* [The original zbar](http://zbar.sourceforge.net/) was a software written in C with bindings for various languages. Its development stopped in 2012.
* The [zbar package on PyPI](https://pypi.org/project/zbar) contains the Python bindings of the original zbar. Its code is part of the original zbar code repo. The PyPI package received its last release in 2009. It has _not_ been updated to wrap the new zbar C library. [Bit rot](https://en.wikipedia.org/wiki/Software_rot) has taken its toll: In some quick testing, `pip install zbar` under Python 3.10 led to nothing but error messages. That's why the "zbar" PyPI package is not mentioned in the table above or elsewhere in this blog post.

Both original and new zbar are licensed under the LGPL version 2.1.

In lieu of up-to-date documentation, [this source code folder](https://github.com/mchehab/zbar/tree/master/zbar/decoder) served as my reference for compiling the list of supported symbologies (see table above). In addition to what's shown in the table, zbar also supports "SQ Code", [a strong contender for the title of "world's most obscure barcode symbology"](https://github.com/mchehab/zbar/discussions/232).

Of the zbar wrapper packages available on PyPI, [**pyzbar**](https://pypi.org/project/pyzbar) is the most likely to work out-of-the-box for most users. Like most other Python barcode reading packages it wraps the zbar C library, but sets itself apart by advertising (and delivering) ease of installation on Windows.  It is actively maintained by members of the [Natural History Museum in London](https://www.nhm.ac.uk). If you don't care about Windows support and instead want a 1-step install on Linux, consider [fastzbarlight](https://pypi.org/project/fastzbarlight) which bundles the original zbar but is unmaintained.

### zxing

First things first: It's pronounced "Zebra Crossing". In the USA (and probably other English-speaking countries) "Xing" is used in road markings and signs to mean "crossing". Elsewhere in the world, Xing is a [Linkedin competitor](https://www.xing.com).

Zxing is a Java library that was actively developed between 2008 and 2018. The project is hosted on [Github](https://github.com/zxing/zxing) and has been in [maintenance mode](https://github.com/zxing/zxing#project-in-maintenance-mode-only) since at least 2018. Despite the "maintenance mode" label, the repo is still quite active and the original maintainer remains involved. Zxing is licensed under the Apache 2.0 license.

[This documentation page](https://zxing.github.io/zxing/apidocs/com/google/zxing/BarcodeFormat.html) was my reference for the list of supported symbologies in the table above.

A big driver of Zxing's popularity is the Android app published by the project with its "100M+ downloads" [in the Google Play Store](https://play.google.com/store/apps/details?id=com.google.zxing.client.android). Also part of the project is the [zxing.org](https://zxing.org) website where you can upload an image and have Zxing read the barcode, and the [zxing.appspot.com](http://zxing.appspot.com) QR code generator website.

Besides the core library, the Android app, and the websites, the Zxing project also contained ports to other languages, an iOS app, and a C++ port.

The homonymous [**zxing**](https://pypi.org/project/zxing) PyPI package offers a Pythonic way of installing and calling it and is your least-bad bet if you must use the Java version for some reason. The package simply calls the JAR using Python's `subprocess.run()`. On my Mac, this results in an annoying Java popup every time a barcode gets read. I find it amusing that zxing's `decode()` method has a `try_harder` argument. Less amusing is the fact that the Python package returns at most one barcode per image ([the PR to fix that](https://github.com/dlenski/python-zxing/pull/13) has been in limbo).

[pyzxing](https://pypi.org/project/pyzxing/) is a separate development (not a fork) but has even fewer features: `try_harder` is missing! It downloads the zxing Java library at runtime from an unofficial source, and couldn't handle file names with spaces in my tests.

### zxing C++

The zxing code repo once contained a sub-directory with a C++ rewrite of the library which was deleted around 2018. The "zxing-cpp" project ~now maintains a fork of this C++ code in~[^3] picked up the idea and wrote a second C++ port [this Github repo](https://github.com/zxing-cpp/zxing-cpp). The official Python bindings for the ~fork~ project are in the [zxing-cpp PyPI package](https://pypi.org/project/zxing-cpp/). zxing-cpp is very actively maintained and exceeds its parent in performance and functionality. Just like its Java parent, zxing C++ is licensed under the Apache 2.0 license.

MicroQR is the one symbology supported by zxing C++ on top of the original zxing's.

There is only one PyPI package that wraps Zxing C++, and it is the main recommendation at the top of this blog post: [**zxing-cpp**](https://pypi.org/project/zxing-cpp/).

Note that there is [another Github repo named `zxing-cpp`](https://github.com/glassechidna/zxing-cpp) that is ~also~ a fork of the original Zxing C++ port. This project seems discontinued, with the last update in 2019. The PyPI package [zxinglight](https://pypi.org/project/zxinglight) is a Python wrapper for this discontinued other port.

### libdmtx

[libdmtx](https://github.com/dmtx/libdmtx) is a C library for reading and writing the Datamtrix barcode symbology only. It has existed since at least 2009, first hosted [on Sourceforge](https://sourceforge.net/projects/libdmtx/), then [confirmed as dormant by the creator](https://stackoverflow.com/a/15140460/997432), and now revived on Github. The repo appears actively maintained but without new feature development. It's licensed under the BSD license (with a custom addition, read the license file before use).

The PyPI package to use for calling libdmtx from Python is [pylibdmtx](https://pypi.org/project/pylibdmtx).

There's also a [.NET port of libdmtx](https://sourceforge.net/projects/datamatrixnet/) which you could probably import into your Python code with Python.NET (I didn't try this). The last activity in the .NET project was in 2017.


## zxing-cpp in detail

Let's take a closer look at [zxing-cpp](https://pypi.org/project/zxing-cpp/), the main recommendation from the top of the article.

Ease of installation is one of the reasons why I decided to recommend [zxing-cpp](https://pypi.org/project/zxing-cpp/). Because the project has wheels for all common platforms available, installation on Mac, Windows, and Ubuntu is just as simple:

```sh
pip install zxing-cpp
```

Most of the other PyPI packages I evaluated required downloading, building, and/or installing the wrapped library separately on at least some of these platforms.

If you have the image with the barcode as a [numpy array](https://numpy.org/doc/stable/reference/arrays.html), you are ready to go:

```python
import zxingcpp

results = zxingcpp.read_barcodes(my_numpy_array)
for r in results:
    print(f"Text:          '{r.text}'")
    print(f"Symbology:     {r.format.name}")
    print(f"Content Type:  {r.content_type.name}")
    print(f"Bounding Box:  {r.position}")
    print(f"Rotation:      {r.orientation}deg")
    print("---")
```

If your image is _not_ already in a numpy array, you have a few options for converting it into one. Each requires installing an additional Python package.

With [imageio](https://pypi.org/project/opencv-python/) (`pip install imageio` and `import imageio.v3`) reading an image from a file looks like this:

```python
import imageio.v3 as iio
img_iio = iio.imread("path/to/my/file.png")
results = zxingcpp.read_barcodes(img_iio)
```

Imageio can read images from many other sources than just local files, including webcam feeds and web URLs. See [the docs](https://imageio.readthedocs.io/en/stable/examples.html#read-from-fancy-sources) for details.

With [pillow](https://pypi.org/project/pillow/) (`pip install pillow` and `import PIL`) you can pass the `Image` object directly into zxingcpp:

```python
from PIL import Image
img_pil = Image.open("path/to/my/file.png")
results = zxingcpp.read_barcodes(img_pil)
```

With [OpenCV](https://pypi.org/project/opencv-python/) (`pip install opencv-python` and `import cv2`) it looks like this:

```python
import cv2
import numpy
img_cv = cv2.imread("path/to/my/file.png")
results = zxingcpp.read_barcodes(img_cv)
```

Matplotlib also works, although I'm not sure it ever makes sense to use it (you'd already know what's in the barcode):

```python
import matplotlib.pyplot as plt
import numpy
img_mpl = plt.imread("path/to/my/file.png")
np_arr = numpy.array(img_mpl)
results = zxingcpp.read_barcodes(np_arr)
```

In many real-world applications, barcode reading is only one step in a longer image processing pipeline, and you may already have one of these installed anyway. Otherwise, `imageio` is my preferred choice.

For my test image of a USPS shipping label, the output of the example above looks like this (irrespective of how I loaded the image):

```txt
Text:          '9114220300'
Symbology:     Code128
Content Type:  Text
Bounding Box:  642x1788 642x2215 558x2217 558x1792
Rotation:      90
---
Text:          '420941079205590121561713594424'
Symbology:     Code128
Content Type:  GS1
Bounding Box:  1067x2875 1067x4141 946x4149 946x2882
Rotation:      90
---
```

Both barcodes on the shipping label in my example image are linear Code-128 codes. Zxing correctly identifies the second one (the USPS tracking number) as following the [GS1-128 standard](https://en.wikipedia.org/wiki/GS1-128) while the first one is just simple text (a customer reference number printed onto the envelope by the sender).

The properties of the zxing-cpp result object are a bit difficult to find. I found them in [this C++ code file](https://github.com/zxing-cpp/zxing-cpp/blob/master/wrappers/python/zxing.cpp):

```
valid (bool): whether or not result is valid (i.e. a symbol was found)
text (str): text of the decoded symbol (see also TextMode parameter)
bytes (bytes): uninterpreted bytes of the decoded symbol
format (zxing.BarcodeFormat): decoded symbol format
symbology_identifier (str): decoded symbology identifier
content_type (zxing.ContentType): content type of symbol
position (zxing.Position): position of the decoded symbol
orientation (int): orientation (in degree) of the decoded symbol
```

## pyzbar in detail

[PyPI link](https://pypi.org/project/pyzbar) is listed as a runner-up for anyone who insists on (or has been told to) use zbar as the underlying (wrapped) library. zbar continues to be a popular topic [on Stackoverflow](https://stackoverflow.com/questions/tagged/zbar) and in others' blog posts, so I might as well write a brief section on how to best use it if you need to.

The installation process for pyzbar depends on your operating system:

* On **Windows**, all you need to do is `pip install pyzbar`. The Windows [wheels](https://realpython.com/python-wheels/) have a copy of zbar already installed. This makes sense, installing library dependencies on Windows is a major trip hazard.
* On **other platforms**, you are responsible for installing zbar yourself. For example, on macOS, you can use the brew package manager `brew install zbar`.

There's one big caveat on Windows. Straight from the Readme:

> [The new zbar project] does not produce Windows DLLs. The zbar DLLs that are included with the Windows Python wheels are built from the original project and so do not include support for decoding barcode orientation. If you see orientation=None then your system has an older release of zbar that does not support orientation.

In my testing on a Mac with Apple chipset I had to link the zbar library into a place where Python's [`ctypes.utils.find_library`](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries) can find it. For example `~/lib`:

```sh
$ mkdir ~/lib
$ ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
```

Once installed, usage is straightforward:

```python
from pyzbar.pyzbar import decode
from PIL import Image
img_pil = Image.open("path/to/my/file.png")
res = decode(img_pil)
print(res)
```

The `decode` function also accepts numpy arrays, so all the options shown above for zxing-cpp should also work here.

## Commercial Barcode Reading Libraries

No endorsement is implied. Do your own research!

I found two commercial (not free and not open source) barcode reading SDKs that advertise Python libraries as part of their offering.[^4]

### Dynamsoft Barcode Reader

[Dynamsoft Barcode Reader](https://www.dynamsoft.com/barcode-reader/overview/) publishes its Python package on PyPI: https://pypi.org/project/dbr/. No other installation steps are necessary, the PyPI package has wheels that contain the underlying non-Python library.

The [code examples in the Github repo](https://github.com/Dynamsoft/barcode-reader-python-samples#samples) contain a hard-coded license key included. Read the terms & conditions before using it: There are some limitations and the package will communicate with Dynamsoft servers. To get your own license key, sign up on the website and then request a 30-day trial license [on this slightly hidden](https://www.dynamsoft.com/customer/license/trialLicense) page in the Dynamsoft customer portal. It gets auto-approved immediately.

Using the library doesn't feel 100% Pythonic, but it gets the job done:

```python
from dbr import BarcodeReader, EnumErrorCode
reader = BarcodeReader()
results = reader.decode_file("path/to/my/file.png")
if results is None:
    print("No codes found")
else:
    for r in results:
        print(r.barcode_text)
```

In terms of barcodes found, Dynamsoft matches or exceeds all the open source options in all but one of my test images. The `result` objects also contain more information than either zbar or the zxings (see [the docs](https://www.dynamsoft.com/barcode-reader/docs/server/programming/python/api-reference/class/TextResult.html?ver=latest) for details).

In my opinion, Dynamsoft deserves high praise for how accessible their documentation and trial software is. Maintaining a PyPI package with ready-to-go example scripts puts them a few decades ahead of how their peers in the world of industrial B2B sales do it:

### Matrox Imaging Library

[Matrox Imaging Library](https://www.matrox.com/imaging/en/products/software/mil/) advertises Python bindings that work on Windows and Linux. The release notes of their latest version give a glimpse into what is supported:

> Makeover of CPython interface now with NumPy support

To get access to the free trial, you must fill out a form on the website that requires your phone number, email, street address, company name, and "Matrox Imaging Sales Representative / Authorized Integrator you are currently working with".

It took less than 24 hours for a voicemail to pop up on my phone from Matrox salesperson who "wanted to learn more about your intentions with the software" and noted that my phone number's area code doesn't match my address.

### Other Commercial Barcode Reading SDKs

I also checked the following other commercial barcode reading SDKs and did not find any Python-specific tooling for them:

* [Scandit Barcode Scanner SDK](https://www.scandit.com/products/barcode-scanner-sdk/) (some Python example code seems to have existed [in the past](https://stackoverflow.com/questions/60665224/scandit-python-code-15-your-app-id-does-not-match-the-license-keys-app-id#61222436))
* [Cognex Mobile Barcode SDK](https://www.cognex.com/products/barcode-readers/cognex-mobile-barcode-sdk) (previously known as [Manateeworks Barcode SDK](https://manateeworks.com/barcode-scanner-sdk))
* [VintaSoft Barcode .NET SDK](http://www.vintasoft.com/vsbarcode-dotnet-index.html)
* [Leadtools Barcode Pro Developer Toolkit](https://www.leadtools.com/sdk/barcode)
* [DTKSoft Barcode Recognition SDK](https://www.dtksoft.com/?p=barcodesdk)

## OpenMV

One more method for reading barcodes with Python needs to be mentioned: The Python-programmable [OpenMV camera](https://openmv.io) (tagline: Arduino of Machine Vision). OpenMV is a sub-$100 circuit board with an attached camera that comes with various machine vision algorithms embedded. One of these embedded algorithms is barcode detection. The board runs the MicroPython operating system and can therefore be programmed with [MicroPython](https://en.wikipedia.org/wiki/MicroPython).

A short (incomplete) code example to illustrate what this looks like:

```python
import sensor

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
# ... various sensor setup steps, see OpenMV docs

img = sensor.snapshot()
for code in img.find_barcodes():
  print(
    f"found barcode: {code.payload()}, "
    f"read quality: {code.quality()}, "
    f"symbology: {code.type()}"
  )
```

OpenMV brings this post full circle: Don't read barcodes in Python! While OpenMV is Python-programmable, the barcode detection is performed by the embedded code (which is not written in Python).

## The Methods Section

To be included in the comparison, a Python package must work with Python >3.7 and must be primarily a barcode reading tool. For example, a Django extension that happens to also read barcodes through some sub-dependency wouldn't make the cut.

Most importantly, for a package to be included I must have found it! My search terms for the PyPI search box were various combinations of "barcode", "qr", "zbar", "zxing", and symbology names like "code 128", "datamatrix", and so on. Beyond PyPI, I also did some general online searching for combinations of these search terms with "python". If you know of a package or library that I missed, please send me a message so that I can update the post with it.

The list of commercial barcode reading libraries is a mix of names I remember from past projects and trade show visits, supplemented with a quick web search. If your company sells a barcode reading library that I failed to mention, drop me a message and I'll gladly add a link to the post. Judging by what comes through my email inbox, all the marketing savvy companies will do this anyway...

Any statements about read success rates in the text are based on an unscientific experiment: First, I randomly copied 22 images from the "barcode photos" folder on my computer. Then I ran one PyPI package representing each of the underlying software libraries on them. The table below shows the raw data of barcodes found per image file for each library. For the original Zxing I couldn't get a read count because it only returns the first barcode it finds in an image.

```txt
columns:
1. filename
2. fastzbarlight read count
3. pyzbar read count
4. zxing successful read y/n
5. zxing-cpp read count
6. Dynamsoft read count

data:
shippinglabel-01.jpg    3 3 y 2 4
shippinglabel-02.jpg    0 0 n 0 3
shippinglabel-03.jpg    2 2 y 2 2
shippinglabel-04.jpg    1 1 n 0 1
shippinglabel-05.jpg    0 0 y 1 1
shippinglabel-06.jpg    0 0 n 1 1
shippinglabel-07.jpg    2 2 y 2 3
shippinglabel-08.jpg    0 0 n 0 1
shippinglabel-09.jpg    0 0 n 0 0
shippinglabel-10.jpg    1 1 n 0 2
shippinglabel-11.jpg    0 0 n 0 4
boardingpass-1.jpg      0 0 n 0 1
boardingpass-2.jpg      1 1 y 1 1
boardingpass-3.jpg      2 2 y 5 3
boardingpass-4.jpg      0 0 n 1 1
catfood.jpg             0 0 n 2 4
datamatrix1.png         0 0 y 1 1
datamatrix2.png         0 0 y 1 1
ean13.png               1 1 y 1 1
luggagetag.jpg          1 1 n 3 4
pdf417.png              0 0 y 1 1
tshirt.jpg              0 0 n 1 1
two_qr_codes.png        2 2 y 2 2
```

Initially, I was planning to share the images and show which library found which barcode. But then I realized that the boarding passes and shipping labels in my photo set may reveal personal data. Maybe a more rigorous and less privacy-violating comparison will be the subject of a future blog post.

## More about Barcodes

The content of this article is an updated version of a section of my talk "Zebras & Lasers" at PyBay 2018. The[The slide deck and video from the talk are here](https://jonasneubert.com/talks/pybay2018).

{{< related_posts tag="barcodes" >}}


[^1]: The verbs "read", "decode", and "scan" are often used synonymously for "barcode". When precise terminology matters, there are subtle differences between them: _Reading_ covers finding a barcode and decoding it. _Decoding_ is to convert an already located (and aligned and cropped) barcode into its corresponding value (usually a string or a number or URL). Arguably, you can't find a barcode without also decoding it, how else are you going to know that what you found actually is a barcode? _Scanning_ is a specific method for reading that involves a device that captures an image line by line, usually a laser. My post [Intro to Barcode Readers]({{< ref "2017-02-26-intro-to-barcode-readers.md" >}}) goes into more detail on how barcodes work.
[^2]: Performance metrics for barcode reading are about read success rate and read speed. Success rate covers how stretched, misaligned, partially covered, faded, and otherwise damaged a barcode can be to still be read. Speed measures the time between data acquisition of the raw pixels and a decoded value being returned.
[^3]: Thank you to [axxel](https://github.com/axxel) for [sending corrections](https://github.com/jonemo/blog.jonasneubert.com/commit/6814c5ec594975c7f2fb458a18b087359ff64e44#r118205554) about the zxing-cpp project. The post was updated to incorporate these on 2023-06-15.
[^4]: Both happen to be headquartered in Canada: Dynamsoft is in Vancouver and Matrox in Montreal. Matrox is now owned by [Zebra Technologies](https://en.wikipedia.org/wiki/Zebra_Technologies).
