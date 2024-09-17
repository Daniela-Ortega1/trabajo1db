CREATE TABLE ClientesPQRS (
    IdCliente INT PRIMARY KEY,
    NombreCompleto VARCHAR(100),
    Sexo CHAR(1),
    Edad INT,
    Ciudad VARCHAR(50),
    Idpqrs INT,
    Tipo VARCHAR(50),
    FechaCaso DATE,
    Asunto VARCHAR(100),
    Estado VARCHAR(20),
    FechaCierre DATE,
    Urgencia VARCHAR(20)
);
