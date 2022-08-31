---
date: '2019-01-23T00:00:00Z'
published: true
tags:
  - factorytech
  - python
  - barcodes
title: The Best Python Packages for Generating Barcodes
---

Barcodes are a cheap and ubiquitous way to add machine-readable information to an object. I think of barcodes as the real-world equivalent of browser cookies: For example, when you arrive at airport departures, the airline hands you a boarding pass with a barcode (the cookie). From that point onward you're asked to show your barcode at every interaction: at security, the duty-free shop, and the boarding gate. And just like the information stored in browser cookies, the information in barcodes isn't in plain sight but easily made visible.

While preparing a conference talk about barcodes, I spent three evenings researching Python packages for generating images of 1D and 2D barcodes. This review article is the result of that work.

_This article was last updated on January 23th, 2019._

## Summary: Recommendations

[**treepoem**](https://pypi.org/project/treepoem) is the most feature-rich Python package for rendering barcodes as images. It supports all common barcode symbologies as well as many obscure ones, is actively maintained, and is available under the MIT license. It's my recommendation for anyone who wants to work with many symbologies.

However, treepoem requires non-Python dependencies which might be difficult or impossible to install in some situations. If you cannot install treepoem's dependencies, or just don't want to, the next best general purpose option is [**python-barcode**](https://pypi.org/project/python-barcode), the most actively maintained fork of the dormant [pyBarcode](https://pypi.org/project/pyBarcode) package.

To generate barcodes of only a single symbology, I recommend these libraries: [segno](https://pypi.org/project/segno) for QR and MicroQR, [pdf417gen](https://pypi.org/project/pdf417gen) for PDF417, [pylibdmtx](https://pypi.org/project/pylibdmtx/) for Datamatrix, and [PubCode](https://pypi.org/project/PubCode) for Code 128.

## Overview Table

<style>
    .comparison-table th.comparison-table-symbology {
        white-space: nowrap;
    }

    .comparison-table th.comparison-table-symbology>a {
        transform: rotate(-90deg);
        display: block;
        position: absolute;
        width: 1em;
    }
</style>

<table class="comparison-table">
  <tr>
    <th>Package</th>
    <th>last updated</th>
    <th>License</th>
    <th style="white-space: nowrap;"><img style="width: 0.8em" alt="Octocat (Github logo)" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpFNTE3OEEyQTk5QTAxMUUyOUExNUJDMTA0NkE4OTA0RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFNTE3OEEyQjk5QTAxMUUyOUExNUJDMTA0NkE4OTA0RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkU1MTc4QTI4OTlBMDExRTI5QTE1QkMxMDQ2QTg5MDREIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkU1MTc4QTI5OTlBMDExRTI5QTE1QkMxMDQ2QTg5MDREIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+m4QGuQAAAyRJREFUeNrEl21ojWEYx895TDPbMNlBK46IUiNmPvHBSUjaqc0H8pF5+aDUKPEBqU2NhRQpX5Rv5jWlDIWlMCv7MMSWsWwmb3tpXub4XXWdPHvc9/Gc41nu+nedc7/8r/99PffLdYdDPsvkwsgkTBwsA/PADJCnzX2gHTwBt8Hl7p537/3whn04XoDZDcpBlk+9P8AFcAghzRkJwPF4zGGw0Y9QS0mAM2AnQj77FqCzrtcwB1Hk81SYojHK4DyGuQ6mhIIrBWB9Xm7ug/6B/nZrBHBegrkFxoVGpnwBMSLR9EcEcC4qb8pP14BWcBcUgewMnF3T34VqhWMFkThLJAalwnENOAKiHpJq1FZgI2AT6HZtuxZwR9GidSHtI30jOrbawxlVX78/AbNfhHlomEUJJI89O2MqeE79T8/nk8nMBm/dK576hZgmA3cp/R4l9/UeSxiHLVIlNm4nFfT0bxyuIj7LHRTKai+zdJobwMKzcZSJb0ePV5PKN+BqAAKE47UlMnERELMM3EdYP/yrd+XYb2mOiYBiQ8OQnoRBlXrl9JZix7D1pHTazu4MoyBcnYamqAjIMTR8G4FT8LuhLsexXYYjICBiqhQBvYb6fLZIJCjPypVvaOoVAW2WcasCnL2Nq82xHJNSqlCeFcDshaPK0twkAhosjZL31QYw+1rlMpWGMArl23SBsZZO58F2tlJXmjOXS+s4WGvpMiBJT/I2PInZ6lIs9/hBsNS1hS6BG0DSqmYEDRlCXQrmy50P1oDRKTSegmNbUsA0zDMwRhPJXeCE3vWLPQMvan6X8AgIa1vcR4AkGZkDR4ejJ1UHpsaVI0g2LInpOsNFUud1rhxSV+fzC9Woz2EZkWQuja7/B+jUrgtIMpy9YCW4n4K41YfzRneW5E1KJTe4B2Zq1Q5EHEtj4U3AfEzR5SVY4l7QYQPJdN2as7RKBF0BPZqqH4VgMAMBL8Byxr7y8zCZiDlnOcEKIPmUpgB5Z2ww5RdOiiRiNajUmWda5IG6WbhsyY2fx6m8gLcoJDJFkH219M3We1+cnda93pfycZpIJEL/s/wSYADmOAwAQgdpBAAAAABJRU5ErkJggg==" />★</th>
    <th>Python versions</th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/UPC-A">UPC-A</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/EAN-13">EAN-13</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/ISBN">ISBN</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/PZN">PZN</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/Interleaved-2-of-5">I. 2 of 5</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/Code-39">Code 39</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/Code-93">Code 93</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/Code-128">Code 128</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/GS1-DataMatrix">Datamatrix</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/PDF417">PDF417</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/QR-Code">QR</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/Micro-QR-Code">Micro QR</a></th>
    <th class="comparison-table-symbology"><a href="https://github.com/bwipp/postscriptbarcode/wiki/Aztec-Code">Aztec</a></th>
    <th>Output</th>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/treepoem">treepoem</a></td>
    <td>Aug 2018</td>
    <td>MIT</td>
    <td>28</td>
    <td>2, 3</td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td> ✓ </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/pyBarcode">pyBarcode</a></td>
    <td>Jul 2013</td>
    <td>MIT</td>
    <td>N/A</td>
    <td>2, (3)</td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>SVG, opt. Pillow</td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/python-barcode">python-barcode</a><br>
      <small>(fork of pyBarcode)</small>
    </td>
    <td>Jun 2018</td>
    <td>MIT</td>
    <td>47</td>
    <td>&gt;= 3.5</td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>SVG, opt. Pillow</td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/viivakoodi">viivakoodi</a><br>
      <small>(fork of pyBarcode)</small>
    </td>
    <td>Nov 2014</td>
    <td>MIT</td>
    <td>29</td>
    <td>2, 3</td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>SVG, opt. Pillow</td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/steenzout.barcode">steenzout.barcode</a><br>
      <small>(fork of viivakoodi)</small>
    </td>
    <td>Jan 2017</td>
    <td>MIT</td>
    <td>5</td>
    <td>2, 3</td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>SVG, opt. Pillow</td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/reBarcode">reBarcode</a><br>
      <small>(fork of viivakoodi)</small>
    </td>
    <td>Oct 2017</td>
    <td>MIT</td>
    <td>0</td>
    <td>2, 3</td>
    <td> ✓ </td><td> ✓ </td><td> ✓ </td><td> ✓ </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>SVG, opt. Pillow</td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/pyStrich">pyStrich</a><br>
      <small>(fork of huBarcode)</small>
    </td>
    <td>Jul 2016</td>
    <td>Apache</td>
    <td>N/A</td>
    <td>3</td>
    <td>   </td><td> ✓ </td><td>   </td><td>   </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td> ✓ </td><td>   </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/code128">code128</a></td>
    <td>Jan 2015</td>
    <td>LGPL</td>
    <td>N/A</td>
    <td>3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>SVG, opt. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/PubCode">PubCode</a></td>
    <td>Aug 2015</td>
    <td>MIT</td>
    <td>1</td>
    <td>2, (3)</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td> ✓ </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/candybar">candybar</a></td>
    <td>Aug 2016</td>
    <td>Apache</td>
    <td>2</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td><td> ✓ </td><td>   </td><td>   </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/pydmtx/">pydmtx (libdmtx)</a></td>
    <td>Feb 2015</td>
    <td>LGPL-2.1 </td>
    <td>N/A</td>
    <td>2</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td> ✓ </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/pylibdmtx/">pylibdmtx</a></td>
    <td>Jan 2017</td>
    <td>MIT</td>
    <td>21</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td> ✓ </td><td>   </td><td>   </td><td>   </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/pdf417gen">pdf417gen</a></td>
    <td>Nov 2018</td>
    <td>MIT</td>
    <td>22</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/pdf417">pdf417</a><br>
      <small>fork of pdf417gen</small>
    </td>
    <td>Nov 2018</td>
    <td>MIT</td>
    <td>0</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td> ✓ </td><td>   </td><td> ✓ </td>
    <td>   </td>
    <td>req. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/qrcode">qrcode</a></td>
    <td>Jan 2019</td>
    <td>BSD</td>
    <td>1,639</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td> ✓ </td><td>   </td>
    <td>   </td>
    <td>SVG, pypng, opt. Pillow</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/PyQRCode">PyQRCode</a></td>
    <td>Jun 2016</td>
    <td>BSD</td>
    <td>218</td>
    <td></td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td> ✓ </td><td>   </td>
    <td>   </td>
    <td>SVG, pypng</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/segno">segno</a></td>
    <td>Oct 2018</td>
    <td>BSD</td>
    <td>27</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td> ✓ </td><td> ✓ </td>
    <td>   </td>
    <td>see notes</td>
  </tr>
  <tr>
    <td><a href="https://pypi.python.org/pypi/qrcodegen/">qrcodegen</a></td>
    <td>Nov 2018</td>
    <td>MIT</td>
    <td>N/A</td>
    <td>2, 3</td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td>   </td><td>   </td>
    <td>   </td><td>   </td><td> ✓ </td><td>   </td>
    <td>   </td>
    <td>see notes</td>
  </tr>
</table>

## treepoem in detail

[treepoem](https://pypi.org/project/treepoem) stands out by the sheer number of supported symbologies and symbology variants. The way this feat is achieved, however, brings with it a few possible downsides.

The Python package treepoem is a wrapper around the Postscript program [BWIPP](https://bwipp.terryburton.co.uk). treepoem invokes Postscript [using `subprocess.Popen()`](https://github.com/adamchainz/treepoem/blob/master/treepoem/__init__.py#L80-L99) meaning that Postscript must already be installed and `subprocess` available. This may be a problem if you are trying to generate barcode images in a shared environment such as a notebook server, to name just one example. In addition, treepoem [requires](https://github.com/adamchainz/treepoem/blob/master/treepoem/__init__.py#L11) the [Pillow](https://pypi.org/project/Pillow/) package for producing image file formats (see the section "Image file format exporters" below for why this matters).

If you are not affected by any of these potential stumbling blocks, then treepoem is refreshingly easy to use.

To install:

```sh
pip install treepoem
```

To use as a command line tool:

```sh
treepoem --type code128 --output code128.png PyBay2018
```

Some barcode types have options for the generator. This example sets the `eclevel` flag to control the error correction level of the QR Code. To know which options are available for a barcode type, use the [BWIPP docs](https://github.com/bwipp/postscriptbarcode/wiki/QR-Code) as reference:

```sh
treepoem --type qrcode --output qr.gif \
    https://jonasneubert.com/talks/pybay2018.html \
    eclevel=Q
```

To use as a library, this is the same example as Python code:

```python
import treepoem

img = treepoem.generate_barcode(
    barcode_type='qrcode',
    data='https://jonasneubert.com/talks/pybay2018.html',
    options={"eclevel": "Q"}
)
img.convert('1').save('qr.gif')
```

![A selection of barcodes generated with treepoem, using symbologies from the common to the obscure. Columnwise starting in top left: UPC-A, Maxicode, Code 128, Royal Mail 4 State Customer Code, QR Code, Italian Pharmacode, Aztec Code.](/assets/2019-01-23-barcodes-generated-with-treepoem.png)

By the way, the name: barcode → bark ode → tree poem ([source](https://github.com/adamchainz/treepoem#whats-so-clever-about-the-name)).

## Criteria

Compared to web frameworks, data science tools, and the many other problem spaces addressed by open source Python packages, barcodes are only a small niche. However, barcode standards change at a glacial pace, resulting in an ecosystem where even packages that have not been maintained for a decade may enjoy active use. This section contains a few notes explaining the thought process by which I winnowed the list of several dozen options down to those listed in the comparison table and ultimately decided on my recommendations.

### Must Haves

To be included in the review, a package must meet these criteria:

- It is available on PyPI.
- `pip install [packagename]` succeeds without errors on my 5-year-old MacBook.

Of course, an implicit requirement is that I must be able to discover the package. My methods of searching were:

- Enter various barcode related terminology into the search box on [pypi.org](https://pypi.org).
- Search Stackoverflow for barcode related terminology.
- Look at the list of forks for repos associated with packages I had already found.
- Browse through the issue tracker of packages I had already found and follow links.

### Supported Symbologies

Most users will be looking to generate barcodes of a single symbology only, and the summary at the top includes recommendations for single-symbology packages. If you require a symbology for which no such dedicated package exists or if you need to support many symbologies, you will be looking for a general purpose package that supports many symbologies.

The comparison table includes both types of packages. In deciding which packages to recommend, I generally favored those supporting more symbologies or, for "single symbology" packages, those supporting more variants of a symbology.

The comparison table includes columns for 13 symbologies. This might seem unfair because those 13 are an arbitrarily chosen subset of the fifty or so barcode symbologies that have some common use case today. My time and the available space on the conference slide deck were the reasons for this limitation. (A snide aside: If all Readme files were up-to-date with the package functionality, adding columns for additional symbologies would have been a lot easier!) Hopefully, my choice presents a useful balance by including the union set of common and frequently supported symbologies.

A further complication was that some symbologies are subsets of other symbologies and, in some cases, I disagree with the way symbology support is described in the package documentation or readme file. For example, many packages advertise support for [ISSN](https://github.com/bwipp/postscriptbarcode/wiki/ISSN). I do not include ISSN because it is simply an EAN-13 barcode with the first three digits equal to "977". Similarly, the JAN (Japanese Article Number) symbology is sometimes listed separately but is actually identical to [EAN](https://github.com/bwipp/postscriptbarcode/wiki/EAN-13).

Note that I omit the short versions of UPC and EAN, for example [UPC-E](https://github.com/bwipp/postscriptbarcode/wiki/UPC-E) and [EAN-5](https://github.com/bwipp/postscriptbarcode/wiki/EAN-5), purely for space reasons. Most packages that support the long version also support the common short versions.

### Project Activity and Popularity

Most barcode symbologies have been set in stone for decades. In theory, software for generating them could be truly complete, with zero remaining feature requests or bug fixes. However, even if bug-free software existed, some maintenance would be necessary because the Python language has evolved over the years, and so has the ecosystem of available tools for writing image file formats which many barcode generating tools utilize.

The usual tradeoff between project completeness and project activity applies: The more comprehensive the functionality and the higher the quality, the lower the project activity needs to be for a package to likely be a good choice for many users. I tried to find a reasonable balance, but my judgment is subjective. Sadly, the majority of packages I reviewed meet neither the threshold for completeness nor the threshold for activity.

To judge the level of project activity I relied mainly on the date of the most recent project release. In addition, I looked at the number of Github stars, where available, as an indicator of how much secondary activity to expect. Only [qrcode](https://pypi.org/project/qrcode) benefited from this factor, but not enough to compensate for its lack of support for the Micro QR symbology in the head-to-head comparison with [segno](https://pypi.org/project/segno).

### Python 3 support

It's 2019, we are [less than one year](https://mail.python.org/pipermail/python-dev/2018-March/152348.html) away from Python 2 officially becoming obsolete, a big part of the Python ecosystem has [already abandoned it](https://python3statement.org).

All recommendations have explicit Python 3 support. By "explicit" I mean "not accidental": I looked for the "supported Python" package metadata, inclusion it in the test suite, or mentioning it in the Readme.

### Image file format exporters

The task of rendering a string of text into a barcode of a certain symbology consists of two steps: First, figure out what lines (or squares or circles or other geometric artifacts) represent the given text (or number or URL or other content). Second, exporting the lines in an image file format such as PNG, JPG, or SVG.

You'll find a Python package to generate each of the common image file formats, but many of them contain C code. The [Pillow](https://pypi.org/project/Pillow/) project is a bundle of many such packages and provide one consistent API for many image file formats, but can still prove [troublesome](https://stackoverflow.com/search?tab=newest&q=[python-imaging-library]%20install) to [install](https://Pillow.readthedocs.io/en/latest/installation.html).

Thanks to [wheels](https://pythonwheels.com) and [conda](https://conda.io), installing Python packages is less thorny than the war stories in 2013 StackOverflow results would make you think. Nonetheless, it remains a common stumbling block, especially for Windows users, which is why I consider a dependency on Pillow a downside in this review.

Ease of installation is a natural side effect of any Python package that is itself written in self-contained pure Python, i.e. without any embedded C code or external dependencies. The [pypng](https://pypi.org/project/pypng/) package is a pure Python implementation of the PNG file format. The SVG file format is an XML document type and therefore plain text and easily generated from pure Python.

A reasonable in-between solution is offered by several packages that support a limited set of formats in the default installation and expanded capabilities if Pillow happens to be independently installed.

The [segno](https://pypi.org/project/segno/) package for QR codes deserves a mention for supporting nine outputs formats without relying on any external dependency.

## Notes about the Contenders

For anyone still reading, this section contains a collection of marginally interesting notes I scribbled down while researching the packages covered in this review.

### pyBarcode and its forks

The genealogy of the [pyBarcode](https://pypi.org/project/pyBarcode/) family is a fascinating story for every code archeologist. For several years, pyBarcode was the only game in town for generating barcodes in Python and there was a steady trickle of features and version releases. When this stopped 2013, two forks gained some tractions by releasing their own version 0.8: [python-barcode](https://pypi.org/project/python-barcode/) and [viivakoodi](https://pypi.org/project/viivakoodi) ("barcode" in Finnish). The former has received a handful of bugfix and maintance releases including, most recently, "official" Python 3.7 support and is my second recommendation at the top of this article. viivakoodi fizzled out in 2014 and sparked further forks, none of which have recent updates. In addition to those that became PyPI packages, Github has tens of other forks, each with their own independent bug fixes. Oh open source.

PyPI historians will not want to miss a final (?) plot twist in 2017: Suddenly there was [a new pre-release](https://pypi.org/project/pyBarcode/0.8b1/) version of pyBarcode! Sadly, it has stayed a pre-release since then. As, sadly, usual for dormant open source code, the lack of activity does not deter people from filling [the issue tracker](https://bitbucket.org/whitie/python-barcode/issues) and demanding fixes and new features from the solo maintainer.

### code128, PubCode

Most small open source projects eventually go dormant, but some maintainers actively delete their work. This is what happened to code128. The latest version on PyPI is [0.3](https://pypi.org/project/code128/0.3/) from 2015. There are [indications](https://bitbucket.org/01100101/code128/issues/3/typeerror-encoding-is-an-invalid-keyword) that development continued after that date, but [the source code disappeared and remains gone](https://bitbucket.org/01100101/code128/issues/4/code-has-gone).

Based on features alone, I have a preference for code128 over PubCode due to Pillow being optional, but in absence of code or maintenance cannot recommend the package.

### qrcode, PyQRCode, qrcodegen, segno

[qrcode](https://pypi.org/project/qrcode) is the only package in the comparison table that can credibly claim to be "popular". 1,639 have "stared" the repository on Github and there is regular activity in the [issue tracker](https://github.com/lincolnloop/python-qrcode/issues). It probably helps that this package is maintained by [a company](https://github.com/lincolnloop) and not an individual's side project like most others in the comparison table. If your need happens to be for standard QR Codes, you should choose this package. However, it doesn't make the list of recommendations at the top of the article because [segno](https://pypi.org/project/segno) additionally supports Micro QR codes.

segno's documentation has [a much more detailed comparison of QR Code generators](https://segno.readthedocs.io/en/stable/comparison-qrcode-libs.html), including some in-the-weeds comparison criteria I don't fully understand.

### libdmtx, pydmtx, pylibdmtx

[pydmtx](https://pypi.org/project/pydmtx/) is part of the main [libdmtx codebase](https://github.com/dmtx/dmtx-wrappers/tree/master/python). The maintenance status of this project is unclear to me: There have been no updates since 2009 but recently the project has been migrated from [Sourceforge](https://sourceforge.net/projects/libdmtx/) to Github. [pylibdmtx](https://pypi.org/project/pylibdmtx/) updates pydmtx to support Python 3 and includes the dll in the Windows wheel but requires a separate install of libdmtx on all other platforms which is why it is my recommendation for generating Datamatrix codes.

## More about Barcodes

The content of this article was part of my talk "Zebras & Lasers" at PyBay 2018. [Slide deck and video from the talk are here](https://jonasneubert.com/talks/pybay2018).
