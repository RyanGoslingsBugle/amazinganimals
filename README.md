# amazinganimals
Basic autonomous script coded in Python to generate new tweets and follow back followers for the [amazinganimals](https://twitter.com/endangeredbot) Twitter bot.

Generates a single image and link, checks new followers and follows any not currently being followed with a welcome message every time it executes, so hook it up to a crontab and go wild.

##Authentication

Requires Twitter API access to function correctly, therefore you'll need the OAuth key and token for the desired account. Insert them into the OAUTH_TOKEN and OAUTH_SECRET variables.

You'll also need to set up a new application with read/write access to your account in order to post tweets. You can do that at [apps.twitter.com](http://apps.twitter.com). Once you've done that, insert the values into the APP_KEY and APP_SECRET variables.

##Tweets with images

Currently uses the deprecated POST statuses/update_with_media API method as [described here](https://dev.twitter.com/rest/reference/post/statuses/update_with_media).

Twitter now want you to upload media first before creating the status update separately, which I'll probably implement at a later point. Or you could help me out :)
