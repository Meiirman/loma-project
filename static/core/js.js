document.querySelector('#logo').addEventListener('click', function(){
    window.open('/', '_blank');

})


document.querySelector("#user").addEventListener('click', function(){
    var ddd = document.getElementsByClassName("accordion_element")
    ddd[0].classList.toggle("accordion_element_show");
    ddd[1].classList.toggle("accordion_element_show");
    ddd[2].classList.toggle("accordion_element_show");
    ddd[3].classList.toggle("accordion_element_show");
    
});
document.querySelector("#orders").addEventListener('click', function(){
    location.href='/orders';
});
document.querySelector("#couriers").addEventListener('click', function(){
    location.href='/couriers';
});
document.querySelector("#products").addEventListener('click', function(){
    location.href='/products';
});

document.querySelector("#settings").addEventListener('click', function(){
    location.href='/settings';
});



function change_stage_on_table(order_obj) {
    alert(order_obj.id)
    alert(order_obj.name)
}