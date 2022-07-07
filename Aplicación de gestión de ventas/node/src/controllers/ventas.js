const pool = require('./../conection');

const crear = ()=> {
    const nombre = req.body.nombre;
    const descripcion = req.body.descripcion;
    const precio = req.body.precio;
    const sql = `INSERT INTO productos (nombre, descripcion, precio) VALUES ('${nombre}', '${descripcion}', ${precio})`;
    pool.query(sql, (err)=> {
        if(err) {
            res.send('Hubo un error: ' + err);
        } else {
            res.send('Registro exitoso');
        }
    })
}


const verTodo = ()=> {
    const sql = 'SELECT * FROM productos';
    pool.query(sql, (err, result)=> {
        if(err) {
            res.send('Hubo un error: ' + err);
        } else {
            res.send(result.rows);
        }
    })
}


const buscar = ()=> {
    const id = req.params.id;
    const sql =`SELECT * FROM productos WHERE id = ${id}`;
    pool.query(sql, (err, result)=> {
        if(err) {
            res.send('Hubo un error: ' + err);
        } else {
            res.send(result.rows);
        }
    });

}


const actualizar = ()=> {
    const id = req.params.id;
    const campo = req.body.campo;
    const valor = req.body.valor;
    const sql= `UPDATE productos SET ${campo} = '${valor}' WHERE id = ${id}`;
    pool.query(sql, (err)=> {
        if(err) {
            res.send('Hubo un error: ' + err);
        } else {
            res.send('Actualización exitosa');
        }
    });
}


const eliminar = ()=> {
    const id = req.params.id;
    const sql = `DELETE FROM productos WHERE id = ${id}`;
    pool.query(sql, (err)=> {
        if(err) {
            res.send('Hubo un error: ' + err);
        } else {
            res.send('Eliminación exitosa');
        }
    });
}


module.exports = { crear, verTodo, buscar, actualizar, eliminar };