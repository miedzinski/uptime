# worktime-logger #

Keep track of your daily worktime.

## Details ##

worktime-logger allows you to see how many hours did you work in any given date range.

For example, let's say I should work 6 hours per day and I'm curious how much time I've spent working this month.

    $ worktime show -s 01-11-2015 --hours=6
    ----------  -------
    2015-11-02  4:49:08
    2015-11-03  5:58:52
    2015-11-04  6:09:02
    2015-11-05  5:24:43
    2015-11-06  3:56:05
    ----------  -------
    Total: 1 day, 2:17:50 (expected 1 day, 6:00:00)

Whoops! Looks like I should work more.

## Installation ##

    $ pip install worktime-logger

or

    $ python setup.py install
    
## Usage ##

    $ worktime --help

Make sure you run `worktime save` everytime you shutdown.

This script takes assumption your uptime reflects your worktime.

## License ##

worktime-logger is availible under [The MIT License](https://opensource.org/licenses/MIT), see the `LICENSE` file for more information.
