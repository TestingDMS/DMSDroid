/**
 * Created by maomao on 2020/4/23.
 */
Java.perform(function() {
    var cn = "java.util.jar.JarEntry";
    var target = Java.use(cn);
    if (target) {
        target.getName.implementation = function(dest) {
            var myArray=new Array()
            myArray[0] = "INTERESTED"  //INTERESTED & SENSITIVE
            myArray[1] = cn + "." + "getName";
            myArray[2] = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()).split('\n\tat');
            send(myArray);
            return this.getName.apply(this, arguments);
        };
    }
});