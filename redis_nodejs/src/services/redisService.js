const redis = require('redis');
const client = redis.createClient();

const getAllKeys = () => {
  client.keys('*', (err, keys) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error retrieving keys from Redis');
    } else {
      res.send(keys);
    }
  });
};

const getAKey = () => {
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
};

const postAKey = () => {
  const { key, value } = req.body;
  client.set(key, value, (err, reply) => {
    if (err) {
      console.error(err);
      res.status(500).send(`Error setting value for key ${key}`);
    } else {
      res.send(`Value set for key ${key}`);
    }
  });
};

const deleteAKey = () => {
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
};

module.exports = {
  getAllKeys,
  getAKey,
  postAKey,
  deleteAKey,
};
