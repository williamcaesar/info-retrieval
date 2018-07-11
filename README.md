# Information Retrieval - Probabilistic Model

OS dependencies
```
tesseract
```
Setup for pdftotext (https://github.com/jalan/pdftotext)

Debian derivates:

```
sudo apt-get update
sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev
```

Red hat derivates:

```
sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python-devel redhat-rpm-config
```

macOS:

```
brew install pkg-config poppler
```

Python dependencies
```
pipenv install
```
Configure mysql user

```
create database ri_vetorial;
create user 'admin'@'localhost' identified by 'password';
grant all privileges on ri_probabilistic.* to 'admin'@'localhost';
```

```
python3 manager.py makemigrations
python3 manager.py migrate
```