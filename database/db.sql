CREATE TABLE anuncios(
    uid INT NOT NULL,
    titulo CHAR(25) NOT NULL, 
    descripcion varchar(200) NOT NULL,
    fechaInicial timestamp default CURRENT_TIMESTAMP,
    fechaLimite datetime NULL,
    esVisible boolean default 1,
    imagen text NULL,
    primary key("uid")
);

CREATE TABLE categorias(
    uid INT NOT NULl,
    nombre CHAR(25) NOT NULL,
    descripcion VARCHAR(180) NOT NULL,
    primary key("uid") 
);

CREATE TABLE anuncios_categorias(
    anunciosUid INT NULL,
    categoriasUid INT NULL
);

ALTER TABLE anuncios_categorias ADD PRIMARY KEY('anunciosUid') REFERENCES anuncios(uid);
ALTER TABLE anuncios_categorias ADD PRIMARY KEY('categoriasUid') REFERENCES categorias(uid);