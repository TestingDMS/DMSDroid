/**
 * Created by maomao on 2020/4/23.
 */
Java.perform(function() {
    var cn = "java.text.SimpleDateFormat";
    var target = Java.use(cn);
    if (target) {
        target.applyLocalizedPattern.implementation = function(dest) {
            var myArray=new Array()
            myArray[0] = "INTERESTED"  //INTERESTED & SENSITIVE
            myArray[1] = cn + "." + "applyLocalizedPattern";
            myArray[2] = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()).split('\n\tat');
            send(myArray);
            return this.applyLocalizedPattern.apply(this, arguments);
        };

        target.applyPattern.implementation = function(dest) {
            var myArray=new Array()
            myArray[0] = "INTERESTED"  //INTERESTED & SENSITIVE
            myArray[1] = cn + "." + "applyPattern";
            myArray[2] = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()).split('\n\tat');
            send(myArray);
            return this.applyPattern.apply(this, arguments);
        };
    }
});