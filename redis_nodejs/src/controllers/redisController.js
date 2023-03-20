const getAllKeys = (req, res) => {
  res.send('get all keys PPC');
};

const getAKey = (req, res) => {
  req.send('Get a key');
};

const postAKey = (req, res) => {
  req.send('Post a key');
};

const deleteAKey = (req, res) => {
  res.send('Delete a key');
};

module.exports = {
  getAllKeys,
  getAKey,
  postAKey,
  deleteAKey,
};
