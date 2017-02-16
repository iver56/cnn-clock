/*
 This file includes a copyrighted code snippet by Refsnes Data
 Original: http://www.w3schools.com/graphics/tryit.asp?filename=trycanvas_clock_start

 This code repository is for non-profit educational purposes only,
 hence the doctrine of fair use applies
 */
'use strict';
const Canvas = require('canvas');
const fs = require('fs');
const path = require('path');

function drawClock(ctx, radius, hour, minute, second) {
  drawFace(ctx, radius);
  drawNumbers(ctx, radius);
  drawTime(ctx, radius, hour, minute, second);
}

function drawFace(ctx, radius) {
  let grad;
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, 2 * Math.PI);
  ctx.fillStyle = 'white';
  ctx.fill();
  grad = ctx.createRadialGradient(0, 0, radius * 0.95, 0, 0, radius * 1.05);
  grad.addColorStop(0, '#333');
  grad.addColorStop(0.5, 'white');
  grad.addColorStop(1, '#333');
  ctx.strokeStyle = grad;
  ctx.lineWidth = radius * 0.1;
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, radius * 0.1, 0, 2 * Math.PI);
  ctx.fillStyle = '#333';
  ctx.fill();
}

function drawNumbers(ctx, radius) {
  let ang;
  let num;
  ctx.font = radius * 0.15 + "px arial";
  ctx.textBaseline = "middle";
  ctx.textAlign = "center";
  for (num = 1; num < 13; num++) {
    ang = num * Math.PI / 6;
    ctx.rotate(ang);
    ctx.translate(0, -radius * 0.85);
    ctx.rotate(-ang);
    ctx.fillText(num.toString(), 0, 0);
    ctx.rotate(ang);
    ctx.translate(0, radius * 0.85);
    ctx.rotate(-ang);
  }
}

function drawTime(ctx, radius, hour, minute, second) {
  //hour
  hour = hour % 12;
  hour = (hour * Math.PI / 6) +
    (minute * Math.PI / (6 * 60)) +
    (second * Math.PI / (360 * 60));
  drawHand(ctx, hour, radius * 0.5, radius * 0.07);
  //minute
  minute = (minute * Math.PI / 30) + (second * Math.PI / (30 * 60));
  drawHand(ctx, minute, radius * 0.8, radius * 0.07);
  // second
  second = (second * Math.PI / 30);
  drawHand(ctx, second, radius * 0.9, radius * 0.02);
}

function drawHand(ctx, pos, length, width) {
  ctx.beginPath();
  ctx.lineWidth = width;
  ctx.lineCap = "round";
  ctx.moveTo(0, 0);
  ctx.rotate(pos);
  ctx.lineTo(0, -length);
  ctx.stroke();
  ctx.rotate(-pos);
}

const numImages = 500;
for (let i = 0; i < numImages; i++) {
  let hour = parseInt(12 * Math.random());
  let minute = parseInt(60 * Math.random());
  let second = parseInt(60 * Math.random());

  let fileName = `clock_${hour}_${minute}_${second}.png`;
  let filePath = path.join(__dirname, 'data', fileName);
  if (fs.existsSync(filePath)) {
    continue;
  }

  let canvas = new Canvas(32, 32);
  let ctx = canvas.getContext("2d");
  let radius = canvas.height / 2;
  ctx.translate(radius, radius);
  radius = radius * 0.90;
  drawClock(ctx, radius, hour, minute, second);

  let out = fs.createWriteStream(filePath)
    , stream = canvas.pngStream();

  stream.on('data', function(chunk) {
    out.write(chunk);
  });
  stream.on('end', function(){
    console.log(`${i}: Saved ${filePath}`);
  });
}
