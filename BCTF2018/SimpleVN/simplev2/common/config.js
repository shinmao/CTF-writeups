const path = require('path')

const constant = require('../constant')

const STATIC_PATH = path.resolve(constant.ROOT_PATH, 'public')    // /simplev2/public
const FLAG_PATH = path.resolve(constant.ROOT_PATH, '********')    // /simplev2/********
const SCREENSHOT_PATH = path.resolve(STATIC_PATH, 'screenshots')   // /simplev2/public/screenshots
const VIEWS_PATH = path.resolve(constant.ROOT_PATH, 'views')    // /simplev2/views

const EXPRESS_SECRET = process.env.EXPRESS_SECRET || '********'
const SECRET_KEY = process.env.SECRET_KEY || '********'
const SERVER_HOST = process.env.SERVER_HOST || 'localhost'
const TRUST_IPS = JSON.parse(process.env.TRUST_IPS || '["127.0.0.1","::ffff:127.0.0.1"]')
const FLAGFILENAME = process.env.FLAGFILENAME || '********'
const MYSQL_HOST = process.env.MYSQL_HOST || 'db'
const MYSQL_USER = process.env.MYSQL_USER || '********'
const MYSQL_PASSWORD = process.env.MYSQL_PASSWORD || '********'
const MYSQL_DB = process.env.MYSQL_DATABASE || 'simplevn'
const LOG_LEVEL = process.env.LOG_LEVEL || 'dev'

module.exports = {
  FLAG_PATH,
  FLAGFILENAME,
  EXPRESS_SECRET,
  LOG_LEVEL,
  MYSQL_HOST,
  MYSQL_USER,
  MYSQL_PASSWORD,
  MYSQL_DB,
  VIEWS_PATH,
  SCREENSHOT_PATH,
  SECRET_KEY,
  STATIC_PATH,
  SERVER_HOST,
  TRUST_IPS
}
