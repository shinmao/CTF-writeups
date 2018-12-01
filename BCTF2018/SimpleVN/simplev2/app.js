const express = require('express')
const session = require('express-session')
const cookieParser = require('cookie-parser')
const logger = require('morgan')

const config = require('./common/config')
const connectMySQL = require('./common/database')
const utils = require('./common/utils')
const indexRouter = require('./routes/index')
const usersRouter = require('./routes/users')
const localRouter = require('./routes/local')

const app = express()

const knex = connectMySQL()
utils.initializeDB(knex)

app
  .set('views', config.VIEWS_PATH)   // /simplev2/views
  .set('view engine', 'pug')

  .use(logger(config.LOG_LEVEL))
  .use(express.json())
  .use(express.urlencoded({ extended: false }))
  .use(cookieParser())
  .use(express.static(config.STATIC_PATH))
  .use(session({
    secret: config.EXPRESS_SECRET,
    resave: false,
    saveUninitialized: false
  }))
  .use(async (req, res, next) => {
    res.locals.session = req.session
    res.config = config
    res.locals.title = 'SimepleVN'
    req.knex = knex
    next()
  })

  .use('/', usersRouter)     // /routes/users.js
  .use((req, res, next) => {
    if (!req.session.user || !req.session.user.uid) {
      return res.redirect('/login')
    }
    next()
  })
  .use('/', indexRouter)      // /routes/index.js
  .use((req, res, next) => {
    const remoteIP = req.connection.remoteAddress
    console.log('Query from', remoteIP)
    if (!config.TRUST_IPS.includes(remoteIP)) {
      return res.redirect('/')
    }
    next()
  })
  .use(express.static(config.FLAG_PATH))
  .use('/local', localRouter)

  .use((err, req, res, next) => {
    res.status(err.status || 500)
    return res.render('error')
  })

module.exports = app
