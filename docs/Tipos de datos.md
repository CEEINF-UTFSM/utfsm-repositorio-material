# Tipos de datos



**Usuario**:

+ ROL(pk)
+ nombre (varchar )
+ apellido (varchar)
+ email (email)
+ carrera (fk)
+ contrasena
+ admin: (int)

**Archivo **

+ path
+ nombre
+ tipo 
+ ID (pk)
+ usuario (fk)
+ aceptado (bool)
+ ramo(fk)
+ peso(int)
+ fecha de subida 
+ semestre (varchar)

**Ramo**

+ id (pk)
+ sigla 
+ nombre

**Carrera_Ramo**

+ id (pk)
+ id_carrera (fk)
+ id_ramo (fk)

**Carrera**

+ id (pk)

+ nombre 

  



