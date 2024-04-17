const express = require("express");
const morgan = require("morgan");
const database= require("./database");
const { MongoClient } = require("mongodb");


//Config inicial
const app = express();
app.set("port",4000);
app.listen(app.get("port"));


//Middlewares
app.use(morgan("dev"))

console.log("escuchando al puerto "+app.get("port"));

//Rutas
app.get("/usuarios", async (req, res) => {
    try {
        const connection = await database.getConnection();
        const result = await connection.query("SELECT * FROM usuarios LIMIT 30");
        console.log(result);
        res.json(result); // Envía los resultados como JSON al cliente
    } catch (error) {
        console.error("Error al consultar la base de datos:", error);
        res.status(500).send("Error interno del servidor");
    }
});


// Rutas conexion MONGODB
app.get("/seguimiento_queja", async (req, res) => {
    try {
        // Conexión a la base de datos MongoDB
        const client = new MongoClient("mongodb://localhost:27017", { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();

        // Seleccionar la base de datos
        const database = client.db("bd_gimnasio_8b_idgs_MAO");
        
        // Obtener la colección de usuarios
        const seguimientoCollection = database.collection("seguimiento_queja");
        
        // Consultar los usuarios (limitando a 30 por ahora)
        const seguimiento = await seguimientoCollection.find().limit(30).toArray();
        console.log(seguimiento);
        
        // Enviar la respuesta JSON al cliente
        res.json(seguimiento);
        
        // Cerrar la conexión con la base de datos
        await client.close();
        
        
    } 
    catch (error) {
        console.error("Error al consultar la base de datos:", error);
        res.status(500).send("Error interno del servidor");
    }
});