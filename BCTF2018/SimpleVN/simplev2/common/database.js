const Knex = require('knex')

const config = require('./config')

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

module.exports = connectMySQL
