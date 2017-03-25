const service = (
  JSON.stringify(process.env.MOCK) === 'true'
  ? require('./mock.js') : require('./real.js')
)

export default service.default
