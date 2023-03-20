const express = require('express');
const redis = require('redis');
const client = redis.createClient();

const app = express();
const PORT = process.env.PORT || 3000;
// Now we're able to receive the JSON data inside our controllers under req.body.
// app.use(bodyParser.json());

// For testing purposes
app.get('/', (req, res) => {
  res.send("<h2>It's Working!</h2>");
});

app.listen(PORT, () => {
  console.log(`API listening on port ${PORT}`);
});
