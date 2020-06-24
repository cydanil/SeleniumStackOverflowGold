# Selenium StackOverflow Gold

An easy way to get a gold badge on Stack Overflow.

It's possible to get a silver badge for 30 consecutive days of browsing the
website (enthusiast), and a gold one for 100 days (fanatic).

With cron, Selenium, and a sprinkle of Firefox, you can relax over the weekend.

set the EMAIL and PASSWORD environment variables, and call the script daily:

```bash
$ EMAIL=name@example.com PASSWORD=magics101 python gold_badge.py
```

To get the count, I've set the Fanatic badge to be tracked prior to launching
the script.
