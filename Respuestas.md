## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
Consulta precisa:  Al momento de hacer una petición, el cliente recibirá exactamente los datos que necesita sin necesidad de recibir todo el objeto completo.  Por ejemplo, si el cliente quiere recibir el correo de un usuario, con GraphQL recibirá sólo el correo al menos de que el usuario pida más pero si fuera con REST y el usuario sólo necesita el correo, aun así recibiría el nombre, apellido, correo, edad, etc.

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
Los tipos son como modelos de datos que indican la forma de los objetos disponibles en la API mientras que los resolvers son funciones que indican cómo obtener los datos definidos en los tipos. Se asocian a queries, mutations o campos individuales:

## ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?
No siempre es buena idea confiar solamente en el frontend ya que puede ser manipulado.  También es importante tener la lógica del stock real en el backend.

## ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
Centralizar la lógica en el backend (no en el frontend) y actualiza siempre el campo disponible en función del stock dentro de la misma operación. Por último también se debeería de agregar validaciones dentro de la lógica para garantizar su funcionamiento.