## Flatten JSON

#### _Сonsole utility to convert nested json files to flat._

----

### Installation
```shell
git clone https://github.com/margo-noise/flatten_json.git
cd flatten_json
poetry install
```
or install as python package
```shell
pip3 install --upgrade git+https://github.com/margo-noise/flatten_json
```
### Usage
1. From command line:
```commandline
usage: FlattenJSON [-h] [-d DELIMITER] [-r] filename outfile

positional arguments:
  filename                  Input json file 
  outfile                   Output json file

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter 
                        key separator (default='.')
  -r, --recursive       use recursive solution
```
