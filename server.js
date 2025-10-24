// server.js
const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

const DB = path.join(__dirname, 'database.json');

function readDB() {
  try { return JSON.parse(fs.readFileSync(DB,'utf8')||'[]'); }
  catch { return []; }
}

app.post('/register', (req, res) => {
  const { email, password } = req.body;
  const db = readDB();
  db.push({ email, password, ts: new Date().toISOString() });
  fs.writeFileSync(DB, JSON.stringify(db, null, 2));
  res.send('OK');
});

app.use(express.static('public')); // put index.html in ./public
app.listen(process.env.PORT || 3000);
