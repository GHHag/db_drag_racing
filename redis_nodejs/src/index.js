const express = require('express');
const redis = require('redis');
const client = redis.createClient('redis://127.0.0.1:6379');

const app = express();
const PORT = process.env.PORT || 3000;

// Parse incoming JSON data
app.use(express.json());

// GET all keys
app.get('/keys', (req, res) => {
  client.keys('*', (err, keys) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error retrieving keys from Redis');
    } else {
      res.send(keys);
    }
  });
});

// GET a value by key
app.get('/get/:key', (req, res) => {
  const key = req.params.key;
  client.get(key, (err, value) => {
    if (err) {
      console.error(err);
      res.status(500).send(`Error retrieving value for key ${key}`);
    } else if (value === null) {
      res.status(404).send(`No value found for key ${key}`);
    } else {
      res.send(value);
    }
  });
});

// POST a value with a key
app.post('/set', (req, res) => {
  const { key, value } = req.body;
  client.set(key, value, (err, reply) => {
    if (err) {
      console.error(err);
      res.status(500).send(`Error setting value for key ${key}`);
    } else {
      res.send(`Value set for key ${key}`);
    }
  });
});

// DELETE a value by key
app.delete('/delete/:key', (req, res) => {
  const key = req.params.key;
  client.del(key, (err, reply) => {
    if (err) {
      console.error(err);
      res.status(500).send(`Error deleting value for key ${key}`);
    } else if (reply === 0) {
      res.status(404).send(`No value found for key ${key}`);
    } else {
      res.send(`Value deleted for key ${key}`);
    }
  });
});

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
