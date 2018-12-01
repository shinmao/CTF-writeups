const IMAGE_PATH = process.env.IMAGE_PATH || '../simplev2/public/screenshots'
const MYSQL_HOST = process.env.MYSQL_HOST || 'localhost'
const MYSQL_USER = process.env.MYSQL_USER || '********'
const MYSQL_PASSWORD = process.env.MYSQL_PASSWORD || '********'
const MYSQL_DB = process.env.MYSQL_DATABASE || 'simplevn'

module.exports = {
  IMAGE_PATH,
  MYSQL_HOST,
  MYSQL_USER,
  MYSQL_PASSWORD,
  MYSQL_DB
}
