#!/usr/bin/env node
 // Bot holding a single counter, allowing anyone to increment it and see its value.
// Usage: ./counter.js <auth token>

var botgram = require("..");
var bot = botgram(process.argv[2]);
const get = require('simple-get')
var url = "https://script.google.com/macros/s/AKfycbw-GBAvvLoquYfg_rwYa_OwNB6KP27Py14G0uFfWWB-2cYtt9iT/exec?id=1lk4oaTTfoI6QnayBSRiPtJYbAHxBENor3vrcndStsVY&sheet=sheet1"

bot.command("start", "help", function(msg, reply, next) {
    reply.text("KKQue Foreva!");
});

bot.command("mhs", function(msg, reply, next) {
    reply.text("Getting data...")
    var param = msg.args.raw
    get.concat(url, function(err, res, buffer) {
        if (err) throw err
        var response = JSON.parse(buffer.toString());
        var strResult = "Result:";
        if (response.data.length > 0) {
            var counter = 0;
            for (var i in response.data) {
                obj = response.data[i];
                if (param == "" || obj.Nama_.toLowerCase().indexOf(param.toLowerCase()) > -1) {
                    strResult += "\n- " + obj.NPM + ": " + obj.Nama_ + " (" + obj.Phone + ")";
                    counter++;
                }
            }

            if (counter == 0)
                strResult += "\nNo data contains word <i>'" + param + "'</i>"
        } else {
            strResult = "\nNo data found.";
        }
        reply.html(strResult)
    })
});