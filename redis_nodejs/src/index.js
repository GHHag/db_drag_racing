const express = require('express');
const v1Router = require('./v1/routes/redisRoutes');
const redis = require('redis');
const client = redis.createClient();

const app = express();
const PORT = process.env.PORT || 3000;
// Now we're able to receive the JSON data inside our controllers under req.body.
// app.use(bodyParser.json());

// V1 API ROUTES
app.use('/api/v1/redis', v1Router);

app.listen(PORT, () => {
  console.log(`API listening on port ${PORT}`);
});
