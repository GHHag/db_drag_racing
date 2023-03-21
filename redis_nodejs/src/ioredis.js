const Redis = require('ioredis');

const redis = new Redis({
  host: '127.0.0.1',
  port: 6379,
});

redis.set('mykey', 'myvalue', (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Value set successfully!');
  }
  redis.quit();
});
