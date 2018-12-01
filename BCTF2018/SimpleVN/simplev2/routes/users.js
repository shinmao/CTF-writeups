const express = require('express')
const shortid = require('shortid')
const fs = require('fs')
const path = require('path')
const router = express.Router()

const config = require('../common/config')
const utils = require('../common/utils')


router
  .get('/login', (req, res) => res.render('login'))
  .post('/login', async (req, res) => {
    const username = req.body.username
    const password = req.body.password

    console.log('check username, password')
    if (!username || !password || !utils.checkUsername(username)) {
      return res.render('login', { error: 'Username or Password Error'})
    }

    console.log('user login')
    const user = await req.knex('users')
      .first(
        'uid',
        'username'
      )
      .where({ username, password: utils.encryptPassword(password) })   // can't sql injection?

    if (!user) {
      return res.render('login', { error: 'Username or Password Error'})
    }

    req.session.user = user
    return res.redirect('/')
  })

  .get('/register', (req, res) => res.render('register'))
  .post('/register', async (req, res) => {
    const username = req.body.username
    const password = req.body.password

    console.log('check username, password')
    if (!username || !password || !utils.checkUsername(username)) {
      return res.render('register', { error: 'Username or Password Error'})
    }

    console.log('check repeat username')
    const user = await req.knex('users')
      .first('uid')
      .where({ username })
    if (user) {
      return res.render('register', { error: 'Username already exist'})
    }

    console.log('register user for', username)
    const uid = shortid.generate()
    try {
      await req.knex('users')
        .insert({
          uid,
          username,
          password: utils.encryptPassword(password),
        })
    } catch (err) {
      console.log('register user error', err)
      return res.render('register', { error: 'Username or Password Error'})
    }

    console.log('create user directory')
    const static_Dirname = path.resolve(config.SCREENSHOT_PATH, utils.md5(uid))
    console.log('static', static_Dirname)
    fs.mkdirSync(static_Dirname)
    const viewDirname = path.resolve(config.VIEWS_PATH, 'users', utils.md5(uid))
    console.log('views', viewDirname)
    fs.mkdirSync(viewDirname)

    return res.redirect('/login')
  })

  .get('/logout', (req, res) => {
    req.session.user = null
    res.redirect('/')
  })

module.exports = router
