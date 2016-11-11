# qtor
**Q**uick Transla**tor** - simple translation command.

Translation from English to Japanese and from Japanese to English is possible.

# Usage
1. Get [Microsoft DataMarket](https://datamarket.azure.com/home/) Account
1. Register application to [Applications](https://datamarket.azure.com/developer/applications) in order to get secret key
1. Write your **client_id** and **client_secret** to `config.json`
1. If you haven't installed **requests** yet, `pip install requests`
1. `./qtor.py "text you want to translate"`

# Example
```console
$ ./qtor.py 機能
Features
$ ./qtor.py Features
機能
```

# Author
KAGE

# License
MIT License
