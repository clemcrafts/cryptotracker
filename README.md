# Cryptotracker
A performance tracker for crypto portfolios

![alt tag](https://i.postimg.cc/g0RMZbmg/Screenshot-2021-05-06-at-20-03-12.png)

## Install

```
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
```

## Launch
```
python performance.py
```

## Adapt for your portfolio

Adapt for your need in `performance.py`:

```
    launch(
        portfolio={'btc': 0.01,
                   'bnb': 1,
                   'ada': 10})
```

Make sure the data is available for your coins in csv format.
