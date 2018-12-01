const crypto = require('crypto')
const puppeteer = require('puppeteer')
const path = require('path')
const Knex = require('knex')

const config = require('./config')
const maxPages = 3

const sleep = (millsec) => new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve()
  }, millsec)
})

const md5 = (contents) => crypto.createHash('md5').update(contents).digest('hex')
const randomStr = () => Math.random().toString(36).slice(2)

const connectMySQL = () => {
  const knex = Knex({
    client: 'mysql',
    connection: {
      host : config.MYSQL_HOST,
      user : config.MYSQL_USER,
      password : config.MYSQL_PASSWORD,
      database : config.MYSQL_DB
    },
    pool: { min: 0, max: 1024 }
  })
  return knex
}

const screenshotURL = async (knex, shootData) => {
  const browser = await puppeteer.launch({
    args: [
      '--media-cache-size=1',
      '--disk-cache-size=1',
      '--headless',
      '--disable-gpu',
      '--remote-debugging-port=0',
      '--no-sandbox',
      '--disable-setuid-sandbox'
    ]
  })
  const imgName = md5(shootData.uid + shootData.shooturl + randomStr()) + '-' + (+ new Date()).toString() + '.png'
  const savePath = path.resolve(config.IMAGE_PATH, md5(shootData.uid), imgName)
  const page = await browser.newPage()
  try {
    await page.setExtraHTTPHeaders(JSON.parse(shootData.headers))
    await page.goto(shootData.shooturl)
    await page.screenshot({ path: savePath })
    await browser.close()
    await knex('screenshots')
      .insert({
        uid: shootData.uid,
        name: imgName,
        path: savePath.replace(path.resolve(config.IMAGE_PATH), '')
      })
  } catch (err) {
    console.log('save screenshots error', err)
  }
}


const takePhoto = async (knex, shootData) => {
  await knex('shooting')
    .where({ id: shootData.id })
    .del()
  await screenshotURL(knex, shootData)
}

const checkAllScreenshots = async (knex) => {
  const shootDatas = await knex('shooting')
    .select('id', 'uid', 'shooturl', 'headers')
    .where({ is_view: false })

  let i = 0
  const shootQueue = []
  while(i < shootDatas.length) {
    shootQueue.push(shootDatas.slice(i, i+maxPages))
    i += maxPages
  }

  for (let shoots of shootQueue) {
    const takePhotoes = shoots.map(r => takePhoto(knex, r))
    await Promise.all(takePhotoes).catch(e => console.log('takePhotoes', e))
  }
}

(async () => {
  const knex = connectMySQL()
  while (true) {
    await checkAllScreenshots(knex)
    await sleep(3000)
  }
})()