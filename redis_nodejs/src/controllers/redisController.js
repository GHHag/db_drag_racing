const redisService = require('../services/redisService');

const getAllKeys = (req, res) => {
  const getKeys = redisService.getAllKeys();
  res.send('get all keys PPC');
};

const getAKey = (req, res) => {
  const key = redisService.getAKey();
  req.send('Get a key');
};

const postAKey = (req, res) => {
  const postAKey = redisService.postAKey();
  req.send('Post a key');
};

const deleteAKey = (req, res) => {
  redisService.deleteAKey();
  res.send('Delete a key');
};

module.exports = {
  getAllKeys,
  getAKey,
  postAKey,
  deleteAKey,
};
