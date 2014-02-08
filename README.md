# Twords

This is a Words With Friends (and related) cheater app. I've been using it with new(ish) programmers to explore programming concepts.

Currently, this version is a web app running under [Flask](http://flask.pocoo.org) with the following API:

```host:5000/matches/<tiles>```

Find words that can be made from the letters in the string ```tiles```.

```host:5000/matches/<tiles>/<required>```

Find words that can be made from the combined letters in ```tiles``` and ```required``` but only return words that include the letters in ```required``` exactly (in the same order).
