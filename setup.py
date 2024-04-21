import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as rq:
    install_requires = rq.read()

setuptools.setup(
    name = "Shopping24",
    version = "1.0.0",
    description = "This a python shopping app for handling apparel merch",
    author = "Saint-Inc",
    author_email = "supremecrow999@gmail.com",
    maintainer = "Crazypapi6",
    maintainer_email = "supremecrow999@gmail.com",
    download_url = "https://github.com/Crazypapi6/weldings-hol",
    packages = setuptools.find_packages(
"C:\Users\crow\weldings hol\.venv\Lib\site-packages"
    ),
    classifiers =[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows, Linux-subsystem",
    ],
    keywords = ["python", "streamlit", "shopping", "online-payment", "login", "sqlite3", "Shop management"],
    include_package_data = True,
    python_requires=">=3.9"
) 
