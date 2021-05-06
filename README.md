# Cryptotracker
A performance tracker for crypto portfolio

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
performance = Performance(portfolio={'btc': 1.43,
                                     'eth': 33,
                                     'ada': 46000,
                                     'theta': 668,
                                     'dot': 31})
```

Make sure the data is available for your coins in csv format.
