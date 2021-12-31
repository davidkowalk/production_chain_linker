# Production Forrest

> This script is currently in alpha and I am working on the main branch. It is highly unstable and may be untested.

The Production-Forrest takes a json file describing linked nodes and will tell you, how scale your production chain.

The script has been written for a just-in-time production chain, specifically taylored for the video game "factorio".

A user can define a production chain via a json file. The item to be produced is specified on startup and in what amounts per unit of time during runtime.

## How to start Production-Forrest.

To run forrest you need to first install python3 on your system. Then download the repository from GitHub, go to the `/src/` folder and in your console or terminal run

```
python3 forrest.py <path to json file>
```

The python3 program alias may vary depending on your system:

```
python3 forrest.py <path to json file>
```
