function cambiarImagenSrcsetPorSrc(obj) {
    var temp = obj.src;
    obj.src = obj.srcset;
    obj.srcset = temp;
 }