function Decoder(request) {

    var decoded = JSON.parse(request.body);
        
    var datacakeFields = []

    for (var key in decoded) {

        if (decoded.hasOwnProperty(key)) {           
            
            datacakeFields.push(
                {
                    device: decoded["serial"],
                    field: key.toUpperCase(), 
                    value: decoded[key]
                }
            )
        }
    }      

    return datacakeFields;    
       
}