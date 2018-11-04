## 1pwnch's Bakery
Category: Web challenge  
Date: 11/04/2018  
Type of Exploit: Code review + Web Cache Poisoning  

## Exploit  
[Blog post](http://blog.1pwnch.com/web/2018/11/04/Wut-to-learn-from-1pwnch-Bakery/#more)

## Source code of server.js  
```
'use strict'

var express = require('express');
var app = express();
var mcache = require('memory-cache');
var mkdirp = require('mkdirp');
var busboy = require('connect-busboy');
var path = require('path');
var fs = require('fs');

app.set('view engine', 'jade');

app.use(express.static('public'))
app.use(busboy());

app.enable('trust proxy');

var cache = (duration) => {
  return (req, res, next) => {
    let key = req.hostname
    let cachedBody = mcache.get(key)
    if (cachedBody) {
      res.send(cachedBody)
      return
    } else {
      res.sendResponse = res.send
      res.send = (body) => {
        mcache.put(key, body, duration * 1000);
        res.sendResponse(body)
      }
      next()
    }
  }
}

app.post('/upload', function(req, res){
	var fsstream;
	var b = new Buffer(req.ip)
	var r = __dirname + '/public/' + b.toString('base64') + '/view/'
  	req.pipe(req.busboy);
	req.busboy.on('file', function(fieldname, file, filename){
		console.log('uploading' + filename);
		fsstream = fs.createWriteStream(r + filename)
		file.pipe(fsstream)
		fsstream.on('close', function(){
			res.redirect('back')
		})
	})
})

app.get('/', cache(0.1), (req, res) => {
  // static ip
  var bread = 'flag{Go Guess it!!}'
  if(req.ip){
        var buffer = new Buffer(req.ip)
        var route = __dirname + '/public/' + buffer.toString('base64') + '/view'
	mkdirp(route, function(){})
  }
  if(req.query.p){
	app.set("views", req.query.p + "view")
  }else{
	app.set("views", __dirname + "/views")
  } 
  setTimeout(() => {
    res.render('index', { title: 'Hey', message: 'Hello there', place: route, bakery: bread})
  }, 5000)
})

app.use((req, res) => {
  res.status(404).send('')
})

app.listen(8888, function () {
  console.log(`Example app listening on port 8888`)
})
```
