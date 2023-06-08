SELECT SUM(e.cantidad), p.nombre, e.id_articulo
FROM Proveedor p JOIN Envio e ON p.id_proveedor = e.id_proveedor
GROUP BY e.id_proveedor, e.id_articulo;