function Decoder(request) {

    var decoded = JSON.parse(request.body);

    var serial = decoded.serial;

    return [
        {
            device: serial,
            field: "LEVEL",
            value: decoded.level
        }
    ]
       
}