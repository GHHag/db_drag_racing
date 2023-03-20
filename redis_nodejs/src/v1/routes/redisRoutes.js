// In src/v1/routes/workoutRoutes.js
const express = require('express');
const redisController = require('../../controllers/redisController');
const router = express.Router();

// GET ALL keys
router.get('/keys', redisController.getAllKeys);

// GET a value by key
router.get('/keys/:key', redisController.getAKey);

// POST a value with a key
router.post('/set', redisController.postAKey);

// DELETE a valye by key
router.delete('/delete/:key', redisController.deleteAKey);

module.exports = router;
