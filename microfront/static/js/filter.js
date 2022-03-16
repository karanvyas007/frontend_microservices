function filter(code){
    let all_item = document.getElementsByClassName('item-wrap');
    let value = document.getElementsByClassName(code);
    for(i=0;i<all_item.length;i++){
        let matched = false
        for (j=0; j<value.length;j++){
            if(all_item[i] == value[j]){
                all_item[i].style.display = "block" ;
                matched = true
                break
            }
        }
        if (!matched){
            all_item[i].style.display = "none";
        }

        if(code == "#000"){
            all_item[i].style.display = "block" ;
        }
    }
    document.getElementById()
}