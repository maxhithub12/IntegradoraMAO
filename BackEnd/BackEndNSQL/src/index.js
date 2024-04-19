const express = require("express");
const morgan = require("morgan");
const database = require("./database");
const swaggerSetup = require("./swagger");
const {MongoClient} = require("mongodb");
const app = express();
app.set("port", 4000);
console.log("http://localhost:4000/api-docs");

// Middleware
app.use(morgan("dev"));
swaggerSetup(app); // Integra Swagger en tu aplicación



/**
 * @swagger
 * /seguimiento_queja:
 *   get:
 *     summary: Obtiene seguimiento de quejas
 *     responses:
 *       '200':
 *         description: Respuesta exitosa
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   
 */
app.get("/seguimiento_queja", async (req, res) => {
    try {
        // Conexión a la base de datos MongoDB
        const client = new MongoClient("mongodb://localhost:27017", { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();

        // Seleccionar la base de datos
        const database = client.db("bd_gimnasio_8b_idgs_MAO");
        
        // Obtener la colección de seguimiento de quejas
        const seguimientoCollection = database.collection("seguimiento_queja");
        
        // Consultar el seguimiento de quejas (limitando a 30 por ahora)
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

// Escuchar en el puerto
app.listen(app.get("port"), () => {
    console.log("Servidor en ejecución en el puerto " + app.get("port"));
});
