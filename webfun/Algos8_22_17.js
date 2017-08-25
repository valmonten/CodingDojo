function invertHash (object){
    var key_list=[];
    var val_list=[];
    for(var key in object){
        if(typeof (object[key])==="array"){
            for(var k=0; k<object[key].length;k++){
                key_list.push(key);
                val_list.push(object[key][k]);
            }

        }else{
            key_list.push(key);
            val_list.push(object[key]);
            }
    }
    object={};
    for(var i=0;i<key_list.length; i++){
        if(object[val_list[i]]){
            if (typeof object[val_list[i]]==="array"){
                object[val_list[i]].push(key_list[i]);

            }else{
                object[val_list[i]]=[object[val_list[i]],key_list[i]];
            }
        }else{
            object[val_list[i]]=key_list[i];
        }
    }
    console.log(object);
    return object;
}

invertHash()