#!/usr/bin/env node
 // Bot holding a single counter, allowing anyone to increment it and see its value.
// Usage: ./counter.js <auth token>

var botgram = require("..");
var bot = botgram(process.argv[2]);
const get = require('simple-get')
var url = "https://script.google.com/macros/s/AKfycbw-GBAvvLoquYfg_rwYa_OwNB6KP27Py14G0uFfWWB-2cYtt9iT/exec?id=1lk4oaTTfoI6QnayBSRiPtJYbAHxBENor3vrcndStsVY&sheet=sheet1"

bot.command("start", function(msg, reply, next) {
    reply.text("KKQue Foreva!");
});

bot.command("hi", function(msg, reply, next) {
    reply.text("Hi juga :)");
});

bot.command("mhs", function(msg, reply, next) {
    reply.text("Tunggu bentar yah...")
    var param = msg.args.raw
    get.concat(url, function(err, res, buffer) {
        if (err) throw err
        var response = JSON.parse(buffer.toString());
        var strResult = "";
        if (response.data.length > 0) {
            var counter = 0;
            var temp = "";
            for (var i in response.data) {
                obj = response.data[i];
                if (param == "" || obj.Nama_.toLowerCase().indexOf(param.toLowerCase()) > -1 || obj.nama_lengkap.toLowerCase().indexOf(param.toLowerCase()) > -1) {
                    temp += "\n- " + obj.NPM + ": " + obj.Nama_ + " (" + obj.Phone + ")";
                    counter++;
                }
            }

            if (counter == 0)
                strResult = "Aku udah nyari, tapi gak nemu data yang ada kata  <i>'" + param + "'</i>-nya.\nMaaf ya :(";
            else
                strResult += "Alhamdulillah aku udah nyari, ini hasilnya:" + temp;
        } else {
            strResult = "Aku udah nyari, tapi gak nemu datanya\nMaaf ya :(";
        }
        reply.html(strResult)
    })
});