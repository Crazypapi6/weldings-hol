## shopping24: using python by Saint Inc.

This product is strictly for admin production use and can only be sold by Authorised masters
[developer]

# Prerequisites

This app has a set of prerequisites that must be met for it to work

1. Having an online video service like youtube to pull urls from
2. Having a photography team that will be incharge of product images
3. A fully intergrated account from paypal, buymeacoffee, patreon, twitter, pintrest, whatsapp, email:
* These will be responsible for handling third party requests
4. A dedicated shop manager with basic computing skills
5. A full products list that we will then insert to the products.db

# Installation

- Install the required libraries using pip

```shell
$ pip install -r requirements.txt
```

- Or Activate the venv using powershell or cmd prompt(windows)

* powershell eg
```sh
$ .venv/Scipts.Activate.ps1 -Verbose
```

* cmd prompt eg
```sh
$ .venv/Scipts.Activate.bat
```

- Activating the app using(Linux)

* Ubuntu eg
```sh
```

## Running the app

```shell
$ python -m streamlit run shop.py
```

# Developer Notes

- **This app uses**

1. **Git:** controls the apps source code, it works hand and glove with github
2. **Github:** Tracks and keep records of the app in all angles
3. **Streamlit:** creates the gui and is responsible for all the availabe features on the app
4. **Html:**  it is widely used in this app to create non existant features on streamlit
5. **TailwindCSS:** which creates the styles for the html components
6. **Pandas:** stores all the arguments of the app
7. **Numpy:** handle math related operations in the app
8. **Openai:** handles the AI function and stracture of the app
9. **paypal/paynow/buymeacoffee/patreon:**
10. **sqlite3:** creates and manages this apps database
11. **Authenticor:** to authenticate users and log them in the app respectively

# Authors
Head to this account if you have a question or a comment or to become a patreon
- [@Saint-Inc][developer]

# Important to note

- If you wish to add or edit dependancies
Images are in the ```products``` folder
Videos are in the ```videos``` folder
Pages are found the ```pages``` folder
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

* You can edit the config settings in a hidden folder ```.streamlit``` then open the ```config.toml``` file, all app secrets are in the ```secrets.toml`` folder and can be accessed by using the [st.secrets] cmd 

# version

- Streamlit, version 1.30.0
- Python 3.12.1
- shop -v 2.0.0

# license and software/owner notes
===

* [Apache licence](https://)
* [MIT license](https://)
[developer]: https://github.com/Crazypapi6
* This software is owned and developed by [Saint Inc.](https://supremecrow999@gmail.com)

===