var merge = require('webpack-merge')
var prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  API_BASE_URL: '"http://localhost:5000/v0"',
  MOCK: process.env.MOCK || 'false',
  NODE_ENV: '"development"'
})
