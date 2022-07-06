const express = require('express');
const app = express();
const ventasRoutes = require('./routes/ventas');

// Middlewares
app.use(express.urlencoded({extended: false}));
app.use(express.json());

// Settings
app.set('port', process.env.PORT || 3000);

// Routes
app.use('/ventas', ventasRoutes);	

// Server
app.listen(app.get('port'), () => {
    console.log(`Server running on port ${app.get('port')}`);
});