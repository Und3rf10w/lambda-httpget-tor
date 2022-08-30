# Lambda HTTPGet Tor Demo
A quick and dirty demo on using AWS lambda to retrieve a file via an HTTP request via TOR

By default, it will do a GET request to `http://ipinfo.io`, with an empty user agent. The lambda can take two arguments, `user_agent`, the user agent the the GET request is going to use, and `url`, the url that a GET request will be issued to.

The raw body of the request will then be returned.

You MUST provide a statically linked Tor binary, and save it in the root as `tor`. I recommend you look at [tor-static](https://github.com/cretz/tor-static), or look at [this guide](https://github.com/jhswartz/static-builds/blob/master/tor.md) to build your own. Do not open an issue asking me to help you build a static `tor` binary.

Some time will be taken for the lambda function to establish the tor circut and issue the actual request.

You may want to look at [qrtt1's lambda-layer-tor](https://github.com/qrtt1/lambda-layer-tor) project

# Usage
- Package repo as a zip.
- Upload from `.zip file` in lambda function editor.
- Adjust function timeout to be at least `1m`. `2m` is recommended. 
- Add a function url.
- Request your function url, adding the `url` and `user_agent` parameters

Example:
```
GET https://eQuuefakelambdaurlhivohz8yee6dae.lambda-url.us-east-1.on.aws?url={url_you_want_to_request}&user_agent={user_agent_you_want_to_request_as}
```

- Wait for a response from the lambda function

# Credits
This project borrows code from:

- https://github.com/Anorov/PySocks
- https://github.com/qrtt1/aws-lambda-tor
