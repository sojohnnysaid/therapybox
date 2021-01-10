$(document).ready(function() {
    $('.js-example-basic-multiple').select2();
});


function checkAll(){
    $('#select_all').change(function () {
        var checkboxes = $(this).closest('form').find(':checkbox');
        checkboxes.prop('checked', $(this).is(':checked'));
    });
}







function set_cookie(key, value){
    return `${key}=${value}`
}

function get_cookie(key){
    return document.cookie.split('; ').find(row=>row.startsWith(key)).split('=')[1];
}




function addToCart(id){
    cart = get_cookie('cart')
    console.log(cart)
    cart = {'items': []}
    document.cookie = `cart=${JSON.stringify(cart)}`
}