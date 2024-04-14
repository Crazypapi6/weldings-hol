# shop: example using python by Saint Inc.

For world wide free usage

# Prerequisites

This app has a set of prerequisites that must be met for it to work

1. Having an online video service like youtube to pull urls from
2. Having the same method for images if not have a local folder like how it is in the example
3. A fully intergrated account from paypal, buymeacoffee, patreon, twitter, github, pintrest, whatsapp
4. A formsubmit.co ready account for requests

# Installation

1. Install the required libraries using pip

```shell
$ pip install -r requirements.txt
```

2. Or Activate the venv using powershell or cmd prompt(windows)

powershell

```sh
$ .venv/Scipts.Activate.ps1 -Verbose
```

cmd prompt
```sh
$ .venv/Scipts.Activate.bat
```

## Running the app

```shell
$ python -m streamlit run shop.py
```

# Developer Notes

This app uses 
1. Git: controls the apps source code, it works hand and glove with github
2. Github: Tracks and keep records of the app in all angles
3. Streamlit: creates the gui and is responsible for all the availabe features on the app
4. Html: it is widely used in this app to create non existant features on streamlit
5. TailwindCSS: which creates the styles for the html components
6. Pandas: stores all the arguments of the app
7. Numpy: handle math related operations in the app
8. Openai: handles the AI function and stracture of the app
9. paypal/paynow/buymeacoffee:
10. sqlite3: creates and manages this apps database
11. materiallogin from strealit components v1: which uses javascript to create frontend dev of the login function

# Authors
Head to this account if you have a question or a comment or to become a patreon
- [@Saint-Inc](https://github.com/Crazypapi6)

# Important to note
- If you wish to add or edit dependancies
Images are in the ```images``` folder
Videos are in the ```videos``` folder
pages are found the ```pages``` folder
The templates can be found in the ```template``` folder

- This app was made with delicacy to reduce data repatition
Dictionaries and key word names are defined as 
```python
company_name = """..."""
dict = {...}
list = [...]
```
- If you wish to change the theme or original font go to the ```template``` folder and edit the ```style.css``` file

* You can change the 
```css
*{
    font-family: 'Times New Roman', Times, serif;
}
```

* The theme is in a hidden folder ```.streamlit``` then open the ```config.toml``` file, all app secrets are in this folder and can be accessed by using the [st.secrets] cmd 

# version

- Streamlit, version 1.30.0
- Python 3.12.1
- shop -v 1.0.0

# license
===

* [Apache licence](https://)

===

* [python license]()

A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see https://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see https://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see https://opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
releases have also been GPL-compatible; the table below summarizes
the various releases.

    Release         Derived     Year        Owner       GPL-
                    from                                compatible? (1)

    0.9.0 thru 1.2              1991-1995   CWI         yes
    1.3 thru 1.5.2  1.2         1995-1999   CNRI        yes
    1.6             1.5.2       2000        CNRI        no
    2.0             1.6         2000        BeOpen.com  no
    1.6.1           1.6         2001        CNRI        yes (2)
    2.1             2.0+1.6.1   2001        PSF         no
    2.0.1           2.0+1.6.1   2001        PSF         yes
    2.1.1           2.1+2.0.1   2001        PSF         yes
    2.1.2           2.1.1       2002        PSF         yes
    2.1.3           2.1.2       2002        PSF         yes
    2.2 and above   2.1.1       2001-now    PSF         yes

Footnotes:

(1) GPL-compatible doesn't mean that we're distributing Python under
    the GPL.  All Python licenses, unlike the GPL, let you distribute
    a modified version without making your changes open source
