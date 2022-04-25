# Unicode SSRF payload concealer

## Kudos
The scripts in this repo is a result of following 
https://www.rfk.id.au/blog/entry/security-bugs-ssrf-via-request-splitting/ guide for a CTF about HTTP request splitting (CVE-2018-12116).

## Main idea
The idea is to smuggle http request (inject it into another one) by passing it as another request's parameter, but hiding it from http module till the very end.

Converts plain payload to payload of non-ascii symbols,
which helps to jump over escape characters checks and
smuggle some requests.

## Example

raw payload in a form of:

```
x HTTP/1.1

POST /private_route HTTP/1.1


```

is converted to:
```
ݸܠ݈ݔݔݐܯܱܮܱ܊܊ݐݏݓݔܠܯݰݲݩݶݡݴݥݟݲݯݵݴݥܠ݈ݔݔݐܯܱܮܱ܊܊
```

## Result
After payload is smuggled as a parameter to the server,
Node < 8.x will not check for escape characters, and
convert the payload to latin1 before sending the request.

http module will think that it needs to send one more request
and will send it to the server from the same server.

To check how an old Node.js server handles this payload,
you can use the following js command:

Buffer.from(payload.toLowerCase(), 'latin1').toString()

## Why does it work?

https://xenome.io/http-request-smuggling-via-unicode-payloads/
