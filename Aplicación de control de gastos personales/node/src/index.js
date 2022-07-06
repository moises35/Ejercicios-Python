// Import modules
const express = require('express');
const app = express();
const movimientosRoutes = require('./routes/movimientos');

// Middlewares
app.use(express.urlencoded({extended: false}));
app.use(express.json());

// Settings
app.set('port', process.env.PORT || 5000);

// Routes
app.use('/movimientos', movimientosRoutes);

// Server
app.listen(app.get('port'), () => console.log('Server running in port ' + app.get('port')));