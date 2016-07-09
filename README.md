# uptime #

Keep track of your daily uptimes.

## Details ##

This script allows you to see for how many hours
your computer was up in any given date range.

Personally, I'm using this to track time spent in office.
For example, let's say I should work 6 hours per day and
I'm curious how much time I've spent working this month.

    $ uptime show -s 2015-11 --hours=6
    2015-11-02  4:49:08
    2015-11-03  5:58:52
    2015-11-04  6:09:02
    2015-11-05  5:24:43
    2015-11-06  3:56:05
    total 1 day, 2:17:50
    expected 1 day, 6:00:00

Whoops! Looks like I should work more.

## Installation ##

Simply clone this repo. No external dependencies.
    
## Usage ##

    $ uptime --help

Make sure you run `uptime save` everytime you shutdown.

## License ##

uptime is availible under
[The MIT License](https://opensource.org/licenses/MIT),
see the `LICENSE` file for more information.
