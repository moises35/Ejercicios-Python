const express = require('express');
const routes = express.Router();
const ventasControllers = require('./../controllers/ventas');

// Rutas
routes.post('/create', ventasControllers.crear);
routes.get('/all', ventasControllers.verTodo);
routes.get('/search/:id', ventasControllers.buscar);
routes.post('/update/:id', ventasControllers.actualizar);
routes.post('/delete/:id', ventasControllers.eliminar);

module.exports = routes;