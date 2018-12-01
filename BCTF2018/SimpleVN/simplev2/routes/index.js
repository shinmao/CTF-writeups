const express = require('express')
const fs = require('fs')
const path = require('path')
const router = express.Router()

const utils = require('../common/utils')
const config = require('../common/config')

router
  .get('/', (req, res) => {
    const remoteIP = req.connection.remoteAddress
    res.render('index', { remoteIP })
  })

  .get('/shoot', (req, res) => res.render('shoot'))
  .post('/shoot', async (req, res) => {
    console.log('shoot post')

    const shooturl = req.body.shooturl
    const queryHeaders = req.headers
    if ('content-type' in queryHeaders) delete queryHeaders['content-type']
    if ('content-length' in queryHeaders) delete queryHeaders['content-type']
    console.log('queryHeaders', queryHeaders)

    console.log('check URL')
    if (!shooturl || !utils.checkURL(shooturl)) {
      return res.render('shoot', { error: 'ShootURL error'})
    }

    console.log('add shooturl', shooturl)
    const uid = req.session.user.uid
    try {
      await req.knex('shooting')
        .insert({
          uid,
          shooturl,
          headers: JSON.stringify(queryHeaders),
          is_view: false
        })
    } catch (err) {
      console.log('add shooturl error', err)
      return res.render('shooting', { error: 'ShootURL error'})
    }

    return res.render('shoot', { success: 'Screenshot will generator soon'})
  })

  .get('/photo', async (req, res) => {
    console.log('screenshots get')
    const uid = req.session.user.uid

    console.log('get all screenshots for', uid, req.session.user.username)
    const images = await req.knex('screenshots')
      .select('name', 'path')
      .where({ uid })
    console.log(images)

    return res.render('photo', { images })
  })

  .get('/upug', (req, res) => res.render('upug'))
  .post('/upug', async (req, res) => {
    console.log('upug post')

    const upug = req.body.upug
    console.log(upug)

    console.log('check User\'s PUG template')
    if (!upug || !utils.checkPUG(upug)) {
      return res.render('upug', { error: 'Upug error' })
    }

    console.log('Generator pug template')
    const uid = req.session.user.uid
    const body = `#{${upug}}`
    console.log('body', body)
    const upugPath = path.join('users', utils.md5(uid), `${uid}.pug`)
    console.log('upugPath', upugPath)
    try {
      console.log(config.VIEWS_PATH)
      console.log(path.resolve(config.VIEWS_PATH, upugPath))     // views/users/md5uid/uid.pug 
      fs.writeFileSync(path.resolve(config.VIEWS_PATH, upugPath), body)
    } catch (err) {
      console.log(err)
      return res.render('upug', { error: 'Upug error' })
    }
    return res.render('upug', { success: 'Your PUG template changed'})
  })

module.exports = router
