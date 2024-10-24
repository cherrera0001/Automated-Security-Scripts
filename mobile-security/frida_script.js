// Este script intercepta una función específica en una app de iOS o Android y registra sus parámetros
// Debes tener Frida instalado y ejecutarlo con el comando: frida -U -l frida_script.js -f com.ejemplo.app --no-pause

Java.perform(function () {
    console.log("Frida script iniciado!");

    // Reemplaza el nombre de la clase y método por los de la app que estás probando
    var TargetClass = Java.use("com.ejemplo.app.TargetClass");
    
    // Intercepta una función llamada 'login'
    TargetClass.login.implementation = function (username, password) {
        console.log("Interceptado el login con:");
        console.log("Usuario: " + username);
        console.log("Contraseña: " + password);

        // Modificar el comportamiento original
        var result = this.login(username, password);
        console.log("Resultado original: " + result);
        
        // Devolver un valor falso si quieres modificar el comportamiento
        return result;
    };
});
