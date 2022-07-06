const mysql = require('mysql2');

const conection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'datos'
});

conection.connect((err, con) => {
    if(err) {
        console.log('Ha ocurrrido un error: ' + err);
    } else {
        console.log('Conexión exitosa a la BD');
    }
    return con;
});

module.exports = conection;
