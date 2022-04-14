# Lambda HTTPGet Tor Demo
A quick and dirty demo on using AWS lambda to retrieve a file via an HTTP request via TOR

It will do a GET request to `http://ifconfig.me/all`, and save the output to `outputfile.ext`.

You MUST provide a statically linked Tor binary, and save it in the root as `tor`. I recommend you look at [tor-static](https://github.com/cretz/tor-static). Do not open an issue asking me to help you build a static `tor` binary.

You may want to look at [qrtt1's lambda-layer-tor](https://github.com/qrtt1/lambda-layer-tor) project

# Credits
This project borrows code from:

- https://github.com/Anorov/PySocks
- https://github.com/qrtt1/aws-lambda-tor
