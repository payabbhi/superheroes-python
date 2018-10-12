# Superheroes - A tutorial to enable Payments acceptance via Payabbhi Python library

Superheroes Store allows purchase of a superhero, to run errands for you, by paying a random amount between ₹1 to ₹5.

The `Payments Acceptance workflow` is implemented as described in the Payabbhi [Integration Guide](https://payabbhi.com/docs/integration) using (Payabbhi Python Library)[https://github.com/payabbhi/payabbhi-python]

This tutorial demonstrates integration with `Payabbhi Checkout` using both [dropin](https://payabbhi.com/docs/checkout/#drop-in-checkout) and [custom](https://payabbhi.com/docs/checkout/#custom-checkout) modes.

The Superheroes tutorial is designed to take you to full implementation in four graded steps:

- Step 1 : Basic implementation of `Payments Acceptance workflow`
- Step 2 : Add `Payment Response Handling`
- Step 3 : Add `Exception Handling`
- Step 4 : Reorganize and Refactor to bring everything together

## Getting started

* Clone the Superheroes repository
* Install the [Payabbhi Python library](https://github.com/payabbhi/payabbhi-python)
* Sign up for a `Payabbhi account` and download `API Keys`
* Setup the local env for running Superheroes

### Clone the Superheroes repository

```
 $ git clone https://github.com/payabbhi/superheroes-python.git
```

### Install the Payabbhi Python Client library

To run any of the steps, you will first need to install the [Payabbhi Python library](https://github.com/payabbhi/payabbhi-python). To do so follow the [installation steps](https://github.com/payabbhi/payabbhi-python/blob/master/README.md).

### Sign up for a Payabbhi account and download API Keys

Next, sign up for a [Payabbhi Account](https://payabbhi.com/docs/account) and download the [API keys](https://payabbhi.com/docs/account/#api-keys) from the [Portal](https://payabbhi.com/portal).

As you go through the tutorial, you will need to replace every instance of `<ACCESS-ID>` and `<SECRET-KEY>` with your actual keys. You would typically want to use your `test mode API` keys for this tutorial.

### Setup the web root directory

We have used [Flask](http://flask.pocoo.org/docs/0.12/) to set up the python web server. For the purposes of this tutorial, the `public` folder (included in the git repo) is assumed to be the web root directory. You'll need to configure your web server accordingly, or clone the repo in the right directory to ensure that.

For each step in the tutorial, first copy the templates folder and script(s) to be executed to the `public` folder.

#### Running superheroes tutorial

```
$ python public/superheroes.py

```

Then hit the root url i.e. http://127.0.0.1:5000/ in your browser.
