const get = require('simple-get')
var url = "https://script.google.com/macros/s/AKfycbw-GBAvvLoquYfg_rwYa_OwNB6KP27Py14G0uFfWWB-2cYtt9iT/exec?id=1lk4oaTTfoI6QnayBSRiPtJYbAHxBENor3vrcndStsVY&sheet=sheet1"

get.concat(url, function(err, res, buffer) {
    if (err) throw err
    var response = JSON.parse(buffer.toString());
    var strResult = "Result:";
    for (var i in response.data) {
        obj = response.data[i];
        strResult += "\n- " + obj.NPM + ": " + obj.Nama_;
    }
    console.log(strResult)
})