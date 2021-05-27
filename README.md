# AOChatServer

Servidor de Chat desacoplado del servidor principal.

De este modo ganamos performance y evitamos bottlenecks en el main game por varios factores:

* A pesar de serializar los datos, las cadenas de texto suelen ser, por lo general, largas.
* Evitamos clock time dedication en splitear las cadenas.
* La librería de sockets, actual, busca por separadores para identificar paquetes.
* Como servidor autoritativo, no necesita validar ni detectar información.
* El Main Server se olvida de procesar paquetes, para él, inútiles.
* Por último y más importante, no es necesario encriptar ni desencriptar, dado que no son datos sensibles. El canal es directo con el usuario.


## Funcionalidades

- [ ] Tick rate constante de actualizaciones.
- [ ] Canales de chat privados.
- [ ] Actualizar usuario.
- [ ] Permisos en los canales.
- [ ] Trabajo a modo caché.

## Funciones técnicas

- [x] User wrapper.
- [ ] Token de validación usuario (con caducidad).
- [x] Buffer queue.
- [ ] Detección del Main Server.
- [ ] Verificación de autenticidad Main Server.
- [ ] Agregar/actualizar/quitar usuario a/en/de un canal.



**DISCONTINUED**
