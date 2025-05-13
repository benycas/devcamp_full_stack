// Cree una función JS que acepte 4 argumentos. Suma los dos primeros argumentos, luego los dos segundos y multiplícalos. Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". Si es más pequeño, la consola registra "¡El número es menor que 50!"

function calculo(a, b, c, d) {
    const x = a + b;
    const y = c + d;
    const result_total = x * y;
  
    if (result_total > 50) {
      console.log("¡El número es mayor que 50!");
    } else {
      console.log("¡El número es menor que 50!");
    }
  }

calculo(1, 3, 2, 5); // ¡El número es menor que 50!
calculo(10, 20, 1, 6); // ¡El número es mayor que 50!





