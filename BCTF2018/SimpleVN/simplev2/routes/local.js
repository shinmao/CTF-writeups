const express = require('express')
const fs = require('fs')
const path = require('path')
const router = express.Router()

const utils = require('../common/utils')
const config = require('../common/config')

router
  .get('/render', async (req, res) => {
    const uid = req.session.user.uid
    const upugPath = path.join('users', utils.md5(uid), `${uid}.pug`)   
    if (!fs.existsSync(path.resolve(config.VIEWS_PATH, upugPath))) {
      return res.redirect('/')
    }
    return res.render(upugPath)
  })

module.exports = router
