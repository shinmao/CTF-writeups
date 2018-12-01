const crypto = require('crypto')

const config = require('./config')

const md5 = (contents) => crypto.createHash('md5').update(contents).digest('hex')

const encryptPassword = (password) => {
  return crypto.createHash('sha256').update(password + config.SECRET_KEY).digest('hex')
}

const checkUsername = (username) => {
  return /^[a-zA-Z0-9]{6,}$/g.test(username)
}

const checkURL = (shooturl) => {
  const myURL = new URL(shooturl)
  return config.SERVER_HOST.includes(myURL.host)
}

const checkPUG = (upug) => {
  const fileterKeys = ['global', 'require']
  return /^[a-zA-z0-9\.]*$/g.test(upug) && !fileterKeys.some(t => upug.toLowerCase().includes(t))
}

const initializeDB = (knex) => {
  console.log('initializeDB')
  knex.schema.hasTable('users').then((exists) => {
    console.log('users is exist: ', exists)
    if (!exists) {
      return knex.schema.createTable('users', (t) => {
        t.increments('id').primary(),
        t.string('uid', 14),
        t.string('username', 100),
        t.string('password', 64),
        t.unique(['id', 'uid', 'username'])
      })
    }
  })
  knex.schema.hasTable('screenshots').then((exists) => {
    console.log('screenshots is exist: ', exists)
    if (!exists) {
      return knex.schema.createTable('screenshots', (t) => {
        t.increments('id').primary(),
        t.string('uid', 14),
        t.string('name', 100),
        t.string('path', 255),
        t.unique(['id', 'path'])
      })
    }
  })
  knex.schema.hasTable('shooting').then((exists) => {
    console.log('shooting is exist: ', exists)
    if (!exists) {
      return knex.schema.createTable('shooting', (t) => {
        t.increments('id').primary(),
        t.string('uid', 14),
        t.text('shooturl'),
        t.text('headers'),
        t.boolean('is_view')
      })
    }
  })
}

module.exports = {
  md5,
  checkPUG,
  checkURL,
  checkUsername,
  initializeDB,
  encryptPassword
}