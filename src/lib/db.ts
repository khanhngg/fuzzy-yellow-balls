import mysql from 'mysql2/promise'
import { DB_PASS } from '$env/static/private'

let mysqlconn: Promise<mysql.Connection>

export const connection = () => {
    if (!mysqlconn) {
        mysqlconn = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: DB_PASS,
            database: 'fuzzy_yellow_balls'
        })
    }
    return mysqlconn
}
