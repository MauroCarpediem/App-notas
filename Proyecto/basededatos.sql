CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuario(
id              int(25) auto_increment not null,
nombre          varchar(100),
apellido        varchar(255), 
email           varchar(255) not null,
password        varchar(255) not null,
fecha_registro  date not null,
CONSTRAINT pk_usuario PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email) 
)ENGINE=InnoDB; --Motor de almacenamiento

CREATE TABLE nota(
id          int(25) auto_increment not null,
usuario_id  int(25) not null,
titulo      varchar(255) not null,
descripcion MEDIUMTEXT ,
fecha_nota  date not null,
CONSTRAINT pk_nota PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)ENGINE=InnoDB;

-- Luego se debe copiar el codigo en el servidor wamp para crear u ocupar la base de datos 