var data = 0;

//printing default value of data that is 0 in h2 tag
//document.getElementById("counting").innerText = data;

//creation of increment function
let incr_count;
function increment(ele) {
 	incr_count = ele.previousElementSibling.children[0];
 	incr_count.innerHTML = parseInt(incr_count.innerHTML) + 1;
 	console.log(incr_count.innerHTML);
}

//creation of decrement function
function decrement(ele) {
    if(incr_count.innerHTML != 0){
 	    incr_count.innerHTML = parseInt(incr_count.innerHTML) - 1;
 	    console.log(incr_count.innerHTML);
    }
}
